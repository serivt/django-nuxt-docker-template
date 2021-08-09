<template>
  <v-app>
    <v-app-bar fixed app flat>
      <v-toolbar-title>
        <NuxtLink to="/" class="app-title">{{ title }}</NuxtLink>
      </v-toolbar-title>
      <v-spacer />
      <span v-if="$auth.loggedIn" class="mr-5">Welcome, {{ $auth.user.username }}</span>
      <v-btn v-if="$auth.loggedIn" depressed @click="logout">Logout</v-btn>
    </v-app-bar>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
    <v-footer absolute app>
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      title: 'Django + Nuxt.js + Docker',
    }
  },
  methods: {
    logout() {
      this.$auth.logout()
    }
  }
}
</script>

<style lang="scss" scoped>
.app-title {
  text-decoration: none !important;
  color: rgba(0, 0, 0, 0.87) !important;
}
</style>
