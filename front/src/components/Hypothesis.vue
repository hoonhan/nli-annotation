<template>
<div>
  <v-row>
  <v-col>
    <v-stepper
      v-model="step">
      <v-stepper-header>
        <template v-for="n in 3">
          <v-stepper-step
            color="deep-purple accent-2"
            :key="`${n}-step`"
            :complete="step > n"
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

        Please write a sentence that <b>{{condition}} regarding the premise</b>.<br><br>
        <v-text-field 
          v-model = "texts[n-1]"
          full-width
          outlined
          autofocus
          placeholder = "type your sentence here"/> 
          <!-- Listen to enter to do the same thing. -->
        <v-btn @click="nextStep(n)" color="deep-purple accent-2" dark class="btn_style">
          submit
        </v-btn>
        <span :class="warningMsg != '' ? 'error_txt' : '' ">
          {{warningMsg}}  
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
  name: 'Hypothesis',
  data: () => {
    return {
      texts: ['', '', ''],
      types: ['Entailment', 'Neutral', 'Contradiction'],
      step: 1,
      warningMsg: ''
    }
  },
  computed: {
    condition: function () {
      if (this.step == 1) {
        return 'is definitely true'
      }
      else if (this.step == 2) {
        return 'might be true'
      }
      else {
        return 'is definitely false'
      }
    }
  },
  methods: {
    nextStep: function (n) {

        if (this.texts[n-1].trim() === '') {
          this.warningMsg = "** You must fill in the text field above to submit."
          setTimeout(() => {
            this.warningMsg = ''
          }, 10000);
          return;
        }

        if (n <= 2) {
          this.step++;
          this.warningMsg = ''
        }
        else{
          this.$emit('submit-write', this.texts)
          this.texts = ['', '', '']
          this.step = 1
        }
    }
  },
  mounted() {
    var self = this;
    window.addEventListener('keyup', function(event) {
      if (event.keyCode === 13) { 
        self.nextStep(self.step)
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
  color: red;

  position: relative;
  animation: shake .1s linear;
  animation-iteration-count: 3;
}
@keyframes shake {
    0% { left: -5px; }
    100% { right: -5px; }
}
</style>