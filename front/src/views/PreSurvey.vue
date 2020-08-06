<template>
  <v-row justify="center" align-content="center" align="center" style="height:100%">

      <v-progress-circular
        v-if="loading===true"
        :size="70"
        :width="7"
        color="purple"
        indeterminate/>
      <iframe :src=form_url width="100%" height="80%" frameborder="0" marginheight="0" marginwidth="0" @load="offProgressBar"/>

      <div style="width:40%; text-align:center;">
        <br>
        <v-divider/>
        <v-form
          ref="form"
          v-model="valid"
          style='width:50%;'
        >
        <v-text-field
          v-model="token"
          :rules="tokenRules"
          placeholder="xxxxx-xxxxx-xxxxx"
          label="Complete pre-task questionnaire above to get token"
          required
        ></v-text-field>
        </v-form>
        <v-btn
          :disabled="!valid"
          @click="onClickNext"
          color="deep-purple accent-2"
          class="mr-4 right_button"
        >
          Next
        </v-btn>


      </div>
    </v-row>
</template>

<script>
export default {
  name: 'PreSurvey',
  data: () => ({
    loading: true,
    valid: true,
    token: '',
    tokenRules: [
      v => (v.trim().replace(/-/g,'') === 'strawapplepuppy') || 'The token is incorrect! Check again.',
    ]
  }),
  computed: {
    form_url: function () {
      return "https://docs.google.com/forms/d/e/1FAIpQLSdbnAxt1bi3MJP7UJm3PPt36n0SA3g7svcw0yGu4qrl2xDErw/viewform?embedded=true&usp=pp_url&entry.154727120=" + this.$store.state.mturk_id
    }
  },
  methods: {
    onClickNext: function () {
      const self = this;
      self.$refs.form.validate()
      self.$helpers.server_call(self, function(self, res){ // eslint-disable-line no-unused-vars
        self.$router.push('/annotation')
      }, "/record_pre_done")
    },
    offProgressBar: function () {
      this.loading = false
    }
  },
  beforeMount() {
    this.$helpers.isWrongAccess(this)
  }
}
</script>

<style scoped>

</style>