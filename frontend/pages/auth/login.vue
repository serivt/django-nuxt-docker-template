<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <v-form @submit.prevent="login">
        <v-card flat outlined>
          <v-card-title class="headline d-block text-center">
            Login
          </v-card-title>
          <v-card-text>
            <v-row>
              <v-col>
                <v-text-field
                  v-model="username"
                  :counter="255"
                  :error="errors.username !== null"
                  :error-messages="errors.username"
                  label="Username"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field
                  v-model="password"
                  :counter="255"
                  :error="errors.password !== null"
                  :error-messages="errors.password"
                  label="Password"
                  type="password"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
            <v-alert
              v-if="generalError"
              class="mt-5"
              border="top"
              color="red lighten-2"
              dark
            >
              {{ generalError }}
            </v-alert>
          </v-card-text>
          <v-card-actions>
            <v-spacer />
            <v-btn color="primary" type="submit" depressed>Login</v-btn>
            <v-spacer />
          </v-card-actions>
        </v-card>
      </v-form>
    </v-col>
  </v-row>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      errors: {
        username: null,
        password: null,
      },
      generalError: '',
    }
  },
  methods: {
    async login() {
      const form = {
        username: this.username,
        password: this.password,
      }
      for (const k in this.errors) this.errors[k] = null
      await this.$auth
        .loginWith('local', { data: form })
        .catch(({ response }) => {
          const { data } = response
          if (!data) return
          for (const k in data) this.errors[k] = data[k][0]
          if ('detail' in data) this.generalError = data.detail
        })
    },
  },
}
</script>
