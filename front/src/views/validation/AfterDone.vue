<template>
  <v-row justify="center" align-content="center" align="center" style="height:100%">
      Thank you for your participation.
      Please submit the token below to the MTurk page, and note that you cannot participate in this task anymore.

      three-think-phone

    </v-row>
</template>

<script>
export default {
  name: 'AfterDone',
  beforeMount() {
    this.$helpers.isWrongAccess(this)
  }
}
</script>
