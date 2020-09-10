<template>
<div>
  <v-row>
  <v-col>
    <v-stepper
      v-model="type">
      <v-stepper-header>
        <template v-for="n in 3">
          <v-stepper-step
            color="deep-purple accent-2"
            :key="`${n}-step`"
            :complete="type > n"
            :step="n"
          >
            {{ types[n-1] }}
          </v-stepper-step>

          <v-divider
            v-if="n !== 3"
            :key="n"
          ></v-divider>
        </template>
      </v-stepper-header>

      <v-stepper-items>
        <v-stepper-content
          v-for="n in 3"
          :key="`${n}-content`"
          :step="n"
        >

        <span v-if="cword===''">
          Please choose a word first from the panel above.
        </span>
        <span v-else>
          Please write a sentence that <b>{{condition[n]}} regarding the premise</b> including the word <span class="redbold">{{cword}}</span>.
        </span>
        <br><br>
        <v-text-field 
          v-model = "text"
          full-width
          outlined
          autofocus
          :placeholder="placeholder"
          :disabled="cword===''"/> 
          <!-- Listen to enter to do the same thing. -->
        <v-btn @click="nextStep(n)" color="deep-purple accent-2" dark class="btn_style">
          submit
        </v-btn>
        <span :class="warningMsg != '' ? 'error_txt' : '' " v-html="warningMsg">
        </span>       

        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </v-col>
  </v-row>
</div>
</template>

<script>

export default {
  name: 'HypothesisArtificial',
  data: () => {
    return {
      text: '',
      types: ['Entailment', 'Neutral', 'Contradiction'],
      warningMsg: '',
      condition: {
        1: 'is definitely true',
        2: 'might be true',
        3: 'is definitely false'
      },
    }
  },
  props: [
    'cword',
    'loading',
    'type'
  ],
  methods: {
    nextStep: function (n) {

        if (this.cword === '') {
          this.warningMsg = "<span style='color: red;'>** You must choose a word among the five words provided above.</span>"
          setTimeout(() => {
            this.warningMsg = ''
          }, 10000);
          return;
        }
        if (this.text.trim() === '') {
          this.warningMsg = "<span style='color: red;'>** You must fill in the text field above to submit.</span>"
          setTimeout(() => {
            this.warningMsg = ''
          }, 10000);
          return;
        }
        if (this.text.toLowerCase().replace(/\./g, '').split(' ').indexOf(this.cword) < 0) {
          this.warningMsg = '** You must exactly include the word <span style="color:red; font-weight:bold;">' + this.cword + '</span> in the sentence.'
          setTimeout(() => {
            this.warningMsg = ''
          }, 10000);
          return;
        }


        this.$emit('submit-write', this.text, n-1)
        this.text = ''
        this.warningMsg = ''
        
    }
  },
  computed: {
    placeholder: function() {
      if (this.cword === '') {
        return 'CHOOSE A WORD FIRST'
      }
      return 'type your sentence here'
    }
  },
  mounted() {
    var self = this;
    window.addEventListener('keyup', function(event) {
      if (event.keyCode === 13) { 
        self.nextStep(self.type)
      }
    });
  }
}
</script>

<style scoped>
.btn_style {
  float: right;
}

.error_txt {
  position: relative;
  animation: shake .1s linear;
  animation-iteration-count: 3;
}

.redbold {
  color: red;
  font-weight: bold;
}
@keyframes shake {
    0% { left: -5px; }
    100% { right: -5px; }
}
</style>