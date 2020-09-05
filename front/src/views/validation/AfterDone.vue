<template>
  <v-container>
  <v-row justify="center" align-content="center" align="center" style="height:100%">
    <v-col>
      <v-card>
      <v-card-title>Thank you for your participation.</v-card-title>
      <v-card-text>
      Please submit the token below to the MTurk page and note that you CANNOT participate in this task anymore.<br><br>
      However, if you submit less than 20 responses, you will not be rewarded although you submit the token to the MTurk.<br><br>
      TOKEN:

      <h3>three-think-phone</h3>
      </v-card-text>
      </v-card>
    </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'AfterDone',
  beforeMount() {
    this.$helpers.isWrongAccess(this)
  }
}
</script>
