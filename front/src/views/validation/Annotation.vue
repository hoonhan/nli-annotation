<template>
  <v-container fill-height>
    <v-row align="stretch">
      <v-col cols="5" class="instr_box">
        <instruction-panel-validation/>
      </v-col>
      <v-col cols="7" class="bounding_box">
        <v-row><v-col>
          <h1> Annotation </h1>
          <h3> {{rewardMsg}} </h3>
          <br><v-divider/><br>
          <sentence-pairs :premise="premise" :hypothesis="hypothesis"/>
          <v-radio-group v-model="label">
            <v-radio
              v-for="n in 4"
              :key="n"
              :label="button_labels[n-1]"
              :value="n"
            ></v-radio>
          </v-radio-group>
        </v-col></v-row>
        <v-divider/><br>
        <v-row justify="space-between" class="no-margin">
        <v-btn color="deep-purple accent-2" dark @click="onSubmit">
          Submit
        </v-btn>
        <v-btn color="error" @click.stop="dialog = true">
          Quit
        </v-btn>
        </v-row>
        <span :class="warningMsg != '' ? 'error_txt' : '' ">
          {{warningMsg}}  
        </span>
        <v-dialog v-model="dialog" persistent max-width="500">
          <v-card>
            <v-card-title class="headline">Do you really want to quit?</v-card-title>
            <v-card-text>Once you quit the task, you cannot join the task anymore.</v-card-text>
            <v-card-actions>
              <v-btn color="primary" outlined @click="dialog = false">Back to the task</v-btn>
              <v-spacer></v-spacer>
              <v-btn color="error" text @click="quitTask">Quit</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

      </v-col>
    </v-row>



    <v-snackbar
      v-model="snackbar"
      timeout="2000"
    > 
     {{snackbar_msg}}
    </v-snackbar>

  </v-container>
</template>

<script>
// @ is an alias to /src
// import SentenceLabel from '@/components/SentenceLabel.vue'
import SentencePairs from '@/components/SentencePairs.vue'
import InstructionPanelValidation from '@/components/InstructionPanelValidation.vue'
import axios from 'axios'

export default {
  name: 'Annotation',
  components: {
    // SentenceLabel,
    SentencePairs,
    InstructionPanelValidation
  },
  data: () => ({
    step: 1,
    premise: '',
    hypothesis: '',
    snackbar: false,
    dialog: false,
    snackbar_msg: 'Your response has been recorded!',
    button_labels: ['entailment', 'neutral', 'contradiction', 'inappropriate'],
    label: null,
    pair_id: null,
    warningMsg: ''
  }),
  computed: {
    rewardMsg: function() {
      if (this.step < 21) {
        return 'You should label ' + (21-this.step).toString() + ' more pairs to get rewards.'
      } else {
        return 'Rewards: $ ' + ((this.step - 1) / 20).toString()
      }
    }
  },
  methods: {
    loadPair: function () {
      const self = this;
      axios.get(self.$store.state.server_url + "/get_pair_val", {
        params: {
          mturk_id: self.$store.state.mturk_id
        }
      }).then(function (res) {
        if (res.data.is_quit === true) {
          alert('You finished the task already.\n Or there are no more tasks left.');
          self.$router.push('after-done')
        }
        self.step = res.data.step
        self.pair_id = res.data.pair_id
        self.premise = res.data.premise
        self.hypothesis = res.data.hypothesis
      }).catch(function(err) {
        alert('Please refresh this page.\n' + err);
      });
    },
    onSubmit: function () {
      const self = this;
      if(self.label === null) {
        self.warningMsg = "** You must choose one of the option."
        setTimeout(() => {
          self.warningMsg = ''
        }, 3000);
        return;
      }
      axios.post(self.$store.state.server_url + "/submit_val/", {
          mturk_id: self.$store.state.mturk_id,
          step: self.step,
          pair_id: self.pair_id,
          label: self.label
      }).then(function (res) {
        self.snackbar_msg = 'Your response has been recorded!'
        self.snackbar = true
        
        self.step = res.data.step
        self.label = null
        self.loadPair()
      }).catch(function(err) {
        alert(err);
      });
    },
    quitTask: function () {
      const self = this;
      axios.post(self.$store.state.server_url + "/quit_val/", {
          mturk_id: self.$store.state.mturk_id
      }).then(function () {
        self.dialog = false
        self.$router.push('after-done')
      }).catch(function(err) {
        self.dialog = false
        alert(err);
      });
    }
  },
 beforeMount(){
    this.$helpers.isWrongAccess(this)
    this.loadPair()
 },
}
</script>

<style scoped>
.instr_box {
  border: 2px solid black;
  padding: 1em;
}
.bounding_box {
  border-top: 2px solid black;
  border-right: 2px solid black;
  border-bottom: 2px solid black;
  padding: 1em;
}
.statement {
  height: 3em;
  padding-left: 1em;
  display: flex;
  align-items: center;
  font-weight: bold;
}
.no-margin {
  margin-left: 0;
  margin-right: 0;
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