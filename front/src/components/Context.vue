<template>
  <v-row align="end">
  <v-col cols="9">
    <h3> Context Words: </h3>
    <v-card 
      class="context_panel">
        <v-chip-group
          v-model="context"
          column
          active-class="primary--text"
        >
        <v-chip v-for="word in context_words" :key="word" @click="onChipClick(word)">
          {{ word }}
        </v-chip>
        </v-chip-group>
    </v-card>
  </v-col>
  <v-col cols="3">
    <v-spacer/>
    <v-btn color="deep-purple accent-2" dark class="btn_style" @click="getNewWords" :loading="loading">
      GET NEW WORDS
    </v-btn>
  </v-col>
  </v-row>

</template>

<script>
export default {
  data: () => {
    return {
      context: ''
    }
  },
  props: [
    'context_words',
    'loading'
  ],
  methods: {
    onChipClick: function (word) {
      this.$emit('click-chip', word)
    },
    getNewWords: function () {
      this.$emit('get-new-word')
    }
  },
  watch: {
    context_words: function () {
      this.context = ''
    }
  },
  created() {
    this.context = ''
    this.$emit('click-chip', '')
  }
}
</script>

<style scoped>
.context_panel {

  padding-left: 1em;
  display: flex;
  align-items: center;
  font-weight: bold;
}

.btn_style {
  float: right;
}
</style>