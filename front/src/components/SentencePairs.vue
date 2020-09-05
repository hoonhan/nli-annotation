<template>
<div>
  <v-row>
  <v-col>
    <h3> Premise: </h3>
    <v-card 
      color="orange lighten-4"
      class="premise_text">
      {{ premise }}
    </v-card>
  </v-col>
  </v-row>
  <v-row>
  <v-col>
    <h3> Hypothesis: </h3>
    <v-card 
      color="orange lighten-4"
      class="premise_text">
      {{ hypothesis }}
    </v-card>
  </v-col>
  </v-row>
</div>
</template>

<script>
export default {
  name: 'SentencePairs',
  props: {
    premise: String,
    hypothesis: String
  }
}
</script>

<style scoped>
.premise_text {
  min-height: 3em;
  padding-left: 1em;
  padding-top: 10px;
  align-items: center;
  font-weight: bold;
}
</style>