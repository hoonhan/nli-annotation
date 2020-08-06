<template>
  <v-row>
  <v-col>
    <h3> Premise: </h3>
    <v-card 
      color="orange lighten-4"
      class="premise_text">
      {{ premise_txt }}
    </v-card>
  </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'Premise',
  props: {
    premise_txt: String
  }
}
</script>

<style scoped>
.premise_text {
  height: 3em;
  padding-left: 1em;
  display: flex;
  align-items: center;
  font-weight: bold;
}
</style>