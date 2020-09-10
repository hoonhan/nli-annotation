<template>
  <v-container fill-height>
    <v-row align="stretch">
      <v-col cols="5" class="instr_box">
        <instruction-panel-artificial/>
      </v-col>
      <v-col cols="7" class="bounding_box">
        <v-row><v-col>
          <h1> Annotation </h1>
          <h3> Progress: {{step}} / 15 </h3>
          <v-progress-linear
            :value="100*step/15"
            color="deep-purple accent-2"/>
          <br><v-divider/><br>
          <premise :premise_txt="premise"/>
          <multiple-constraint @click-chip="onClickWord" :cwords="cwords"/>
          <hypothesis-artificial @submit-write="onSubmitWrite" :type="type+1" :cword="cword"/>
          </v-col>
        </v-row>
        <v-row justify="end">
          <v-col cols="6"/>
          <v-col cols="6">
          <v-dialog v-model="dialog" max-width="40%">
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                style="float:right;"
                color="error"
                dark
                v-bind="attrs"
                v-on="on"
              >
                Report / Q&A
              </v-btn>
            </template>
            <v-card>
              <v-card-title class="headline">Anything unclear about the task? Any questions?</v-card-title>
              <v-card-text>
                While we cannot get back to you immediately, your comments would be greatly appreciated.<br><br>
                <v-textarea v-model="issue" label="Any issues?" autofocus hide-details outlined/>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="error" text @click="dialog = !dialog">Close</v-btn>
                <v-btn color="purple" text @click="onSubmitIssue">Submit</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          </v-col>
        </v-row>
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
import Premise from '@/components/Premise.vue'
import HypothesisArtificial from '@/components/HypothesisArtificial.vue'
import InstructionPanelArtificial from '@/components/InstructionPanelArtificial.vue'
import MultipleConstraint from '@/components/MultipleConstraint.vue'
import axios from 'axios'

export default {
  name: 'Annotation',
  components: {
    Premise,
    HypothesisArtificial,
    InstructionPanelArtificial,
    MultipleConstraint
  },
  data: () => ({
    step: 1,
    type: 0,
    premise: '',
    snackbar: false,
    snackbar_msg: 'Your response has been recorded!',
    dialog: false,
    issue: '',
    cwords: [''],
    cword: ''
  }),
  methods: {
    loadPremise: function (first=false) {
      const self = this;
      axios.get(self.$store.state.server_url + "/get_premise", {
        params: {
          mturk_id: self.$store.state.mturk_id
        }
      }).then(function (res) {
        if (res.data.predone === false) {
          alert('You should complete pre-task questionnaire first!\n');
          self.$store.commit('reset_mturk_id')
          self.$router.push('introduction')
        } else if (res.data.step > 15) {
          alert('You already finished the task!\n');
          self.$router.push('after-done')
        }
        self.step = res.data.step
        self.premise = res.data.premise
        if (first) {
          self.loadNewCWord(res.data.type)
        }
      }).catch(function(err) {
        alert('Please refresh this page.\nIf this error repeats, you should go back home as your id is not valid.\n' + err);
      });
    },
    onSubmitWrite: function (text, type) {
      const self = this;
      axios.post(self.$store.state.server_url + "/record_submit_cword/", {
          mturk_id: self.$store.state.mturk_id,
          step: self.step,
          response: text,
          type: type,
          cwords: self.cwords.join('_'),
          cword: self.cword
      }).then(function () {
        self.snackbar_msg = 'Your response has been recorded!'
        self.snackbar = true
        if (type <= 1) {
          self.loadNewCWord(type+1)
        } else if (type === 2 && self.step != 15) {
          self.loadNewCWord(0, true)
        } else {
          self.$router.push('after-done')
        }
        return 'done'
      }).catch(function(err) {
        alert(err);
      });
    },

    loadNewCWord(type, last=false) {
      const self = this;
      self.cwords = []
      console.log(type, self.type, self.step)
      axios.get(self.$store.state.server_url + "/get_cword/", {
        params: {
          mturk_id: self.$store.state.mturk_id,
          type: type
        }
      }).then(function (res) {
        self.type = type
        self.cwords = res.data.cwords
        self.cword = ''
        if (last) {
          self.loadPremise()
        }
      }).catch(function(err) {
        alert(err);
      });      
    },

    onSubmitIssue: function () {
      const self = this;

      axios.post(self.$store.state.server_url + "/record_issue_cword/", {
          mturk_id: self.$store.state.mturk_id,
          step: self.step,
          type: self.type,
          issue: self.issue,
          cwords: self.cwords.join('_'),
          cword: self.cword
      }).then(function () { 
        self.snackbar_msg = 'Thanks! Your issue has been reported!'
        self.snackbar = true
        self.dialog = false
        self.issue = ''
      }).catch(function(err) {
        alert("Sorry but could you submit it again?\n" + err);
      });      
    },

    onClickWord: function (word) {
      const self = this;
      self.cword = word;
    }

  },
 beforeMount(){
    this.$helpers.isWrongAccess(this)
    this.loadPremise(true)
    
    console.log(this.$store.state.user_type)
    if (this.$store.state.user_type != 1) {
      alert("Abnormal access detected.")
    }
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
</style>