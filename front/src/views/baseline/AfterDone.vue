<template>
  <v-row justify="center" align-content="center" align="center" style="height:100%">
      <v-progress-circular
        v-if="loading===true"
        :size="70"
        :width="7"
        color="purple"
        indeterminate/>
      <iframe :src=form_url width="100%" height="80%" frameborder="0" marginheight="0" marginwidth="0" @load="offProgressBar"/>
    </v-row>
</template>

<script>
export default {
  name: 'AfterDone',
  data: () => ({
    loading: true,
  }),
  computed: {
    form_url: function () {
      return "https://docs.google.com/forms/d/e/1FAIpQLScJGIzu1oVFIGG25FOsGaQi3HoagnhBSXif1aVhvXPOu4cT0Q/viewform?embedded=true&usp=pp_url&entry.628211538=" + this.$store.state.mturk_id
    }
  },
  methods: {
    offProgressBar: function () {
      this.loading = false
    }
  },
  beforeMount() {
    this.$helpers.isWrongAccess(this)
  }
}
</script>
