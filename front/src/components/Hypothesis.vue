<template>
<div>
  <v-row>
  <v-col>
    <v-stepper
      v-model="step">
      <v-stepper-header>
        <template v-for="n in 3">
          <v-stepper-step
            @click="moveStep"
            editable
            color="deep-purple accent-2"
            :key="`${n}-step`"
            :complete="texts[n-1] != null"
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

        Please write a sentence that <b>{{condition}} regarding the premise.</b><br><br>
        <v-text-field 
          v-model = "texts[n-1]"
          full-width
          outlined
          clearable
          autofocus
          placeholder = "type your sentence here"/> 
          <!-- Listen to enter to do the same thing. -->
        <v-btn @click="nextStep(n)" color="deep-purple accent-2" dark class="btn_style">
          {{button_txt}}
        </v-btn>
        <span :class="warningMsg != null ? 'error_txt' : null ">
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
  name: 'SubInstruction',
  data: () => {
    return {
      texts: [null, null, null],
      types: ['Entailment', 'Neutral', 'Contradiction'],
      step: 1,
      warningMsg: null,
    }
  },
  props: {
    classType: String
  },
  computed: {
    button_txt: function () {
      if (this.step <= 2) {
        return 'Continue'
      }
      else {
        return 'Submit'
      }
    },
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
      if (n <= 2) {
        if (this.texts[n-1] === null) {
          this.warningMsg = "** You must fill in all the text field above to continue."
          setTimeout(() => {
            this.warningMsg = null
          }, 10000);
          return;
        }
        else {
          this.step++;
        }
      }
      else if (n == 3) {
        if (this.texts.includes(null)) {
          this.warningMsg = "** You must fill in all three text fields to submit."
          setTimeout(() => {
            this.warningMsg = null
          }, 10000);
          
          return;
        }
        else {
          this.$emit('submit-write', this.texts)
          this.texts = [null, null, null]
          this.step = 1
          // What if I reset the texts earlier?
        }
      }
    },
    moveStep: function () {
      this.warningMsg = null
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
  margin-right: 2em;
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