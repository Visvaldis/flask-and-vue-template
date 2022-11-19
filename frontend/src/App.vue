<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">

        <v-avatar class="mx-3" size="60">
          <v-img src="src/assets/fox_samurai_1.jpg" contain alt="Logo" />
        </v-avatar>
        <v-toolbar-title>Test project</v-toolbar-title>
      </div>
      <v-spacer></v-spacer>
    </v-app-bar>

    <v-main>
      <MainPage />
    </v-main>

    <v-footer app padless color="primary">
      <v-col class="text-center" cols="12">
        {{ new Date().getFullYear() }} — <strong>Vuetify</strong>
      </v-col>
    </v-footer>
  </v-app>
</template>

<script setup>
import MainPage from '@/components/MainPage.vue'
</script>
