<template>
  <div id="app">
  <v-app>
    <v-app-bar app
      color="deep-purple accent-2"
      dark>
      <v-toolbar-title>Annotation</v-toolbar-title>
      <v-spacer/>
      <div style="margin-right:5%">
        {{msg}}
        <v-btn class="ma-2" text icon @click="goBack" style="margin-left:20px;" >
        <v-icon large>home</v-icon>
        </v-btn>
      </div>
    </v-app-bar>

    <v-main>
    <router-view/>
    </v-main>

    <v-footer app>
    </v-footer>
  </v-app>
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/annotation">About</router-link>
    </div> -->
  </div>
</template>

<script>
export default {
  computed: {
    msg: function () {
      var id = this.$store.state.mturk_id;
      if (this.$route.name === 'Landing') {
        return 'Welcome!'
      } else if (id === null) {
        return 'Your ID is not registered!!! ___ GO BACK HOME to register your ID'
      }
      else {
        return 'MTurk ID: ' + id
      }
    }
  },
  methods: {
    goBack: function() {
      this.$router.push('/')
    }
  }
}
</script>