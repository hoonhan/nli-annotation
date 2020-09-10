<template>
  <v-row align="end">
  <v-col>
    <h4> Choose a word that you would like to include in the sentence. </h4>
    <v-card 
      class="context_panel">
        <v-chip-group
          v-model="cword"
          column
          active-class="primary--text"
        >
        <v-chip v-for="word in cwords" :key="word" @click="onChipClick(word)">
          {{ word }}
        </v-chip>
        </v-chip-group>
    </v-card>
  </v-col>
  </v-row>

</template>

<script>
export default {
  data: () => {
    return {
      cword: ''
    }
  },
  props: [
    'cwords'
  ],
  methods: {
    onChipClick: function (word) {
      this.$emit('click-chip', word)
    }
  },
  watch: {
    cwords: function () {
      this.cword = ''
    }
  },
  created() {
    this.cword = ''
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