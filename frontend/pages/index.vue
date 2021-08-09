<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <v-card flat outlined>
        <v-card-title class="headline text-center d-block">
          Welcome to the Django + Nuxt.js + Docker template
        </v-card-title>
        <v-card-text>
          <p>
            A Django + Nuxt project template (with Vuetify as the UI component
            framework) using Docker. This template has a basic authentication
            system that uses JWT and a
            <NuxtLink to="/private">private page</NuxtLink> to test it, you need
            to
            <a
              href="https://github.com/serivt/django-nuxt-docker-template/README.md"
              target="_blank"
              >create a Django user</a
            >
            to login.
          </p>
          <p>
            For more information on this template, check out the
            <a
              href="https://github.com/serivt/django-nuxt-docker-template/README.md"
              target="_blank"
              rel="noopener noreferrer"
            >
              README.md</a
            >
            on github.
          </p>
          <p>
            Find a bug? Report it on the github
            <a
              href="https://github.com/serivt/django-nuxt-docker-template/issues"
              target="_blank"
              rel="noopener noreferrer"
              title="contribute"
            >
              issue board </a
            >.
          </p>
          <div class="text-xs-right">
            <em><small>&mdash; Sergio Torrado</small></em>
          </div>
          <hr class="my-3" />
          <a
            href="https://nuxtjs.org/"
            target="_blank"
            rel="noopener noreferrer"
          >
            Nuxt Documentation
          </a>
          <br />
          <a
            href="https://github.com/nuxt/nuxt.js"
            target="_blank"
            rel="noopener noreferrer"
          >
            Nuxt GitHub
          </a>
          <br />
          <a
            href="https://vuetifyjs.com"
            target="_blank"
            rel="noopener noreferrer"
          >
            Vuetify Documentation
          </a>
          <br />
          <a
            href="https://chat.vuetifyjs.com/"
            target="_blank"
            rel="noopener noreferrer"
          >
            Vuetify Discord
          </a>
          <br />
          <a
            href="https://github.com/vuetifyjs/vuetify/"
            target="_blank"
            rel="noopener noreferrer"
          >
            Vuetify GitHub
          </a>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  auth: 'guest',
}
</script>
