<template>
  <div id="app">
  <v-app>
    <v-app-bar app
      color="deep-purple accent-2"
      dark>
      <v-toolbar-title>Sentence Writing</v-toolbar-title>
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
  </div>
</template>

<script>
export default {
  name: 'app',
  created () {
      document.title = "Writing Sentences";
  },
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
      // var user_type = this.$store.state.user_type
      // if (user_type === 0) {
      //   this.$router.push('/baseline/home')
      // } 
      // else if (user_type === 1) {
      //   this.$router.push('/artificial/home')
      // }
      // else if (user_type === 2) {
      //   this.$router.push('/natural/home')
      // }
      this.$router.push('home')
    }
  }
}
</script>