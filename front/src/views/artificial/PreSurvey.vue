<template>
  <v-row justify="center" align-content="center" align="center" style="height:100%">
    <v-col cols="8">
      <h2> Informed Consent for Experiment </h2>
      <h3> </h3>
      1. This research is conducted for the sake of research only.<br><br>

      2. This research is to improve the quality of dataset by introducing appropriate interventions to crowd workers. From the annotation data collected from this experiment, we will justify the effective and efficient way to mitigate the spurious patterns presented in the dataset from crowdsourcing.<br><br>

      3. In this experiment, you will complete a questionnaire and write a sentence corresponding to the given condition.<br><br>

      4. As "questionnaire and annotation platform" to be used in this research does not include an invasive treatment, you are informed that no side effects are known or expected. However, you may experience unexpected risks by participating in the research.<br><br>

      5. Your private and personal information will be kept confidential and access to it by the general public will be restricted. However, as long as the relevant law or regulation allows, your personal information can be made available to the review board and to governmental institutions with the aim of verifying the reliability of the experiment procedures and data. However, even in such a case, the information will be kept in the strictest confidence. If the results of this research are published, your identity will remain confidential.<br><br>

      6. The final decision regarding whether or not to participate in the clinical research is to be made by you. You can always decide not to participate in the tasks and can withdraw your participation anytime. Even if you refuse to participate in this research, you will not be disadvantaged at all.<br><br>

      7. Contact Information<br>
      If you have any questions or wish to express any discomfort related to this research, please feel free to contact the researcher below. <br><br>
      <b>&lt;Name of researcher: Donghoon Han, Contact: <a>hoonhan.d@kaist.ac.kr</a>&gt; <br><br></b>

      <v-divider/>
      <h4>I have read this Informed Consent and received a response to each and every question. I hereby confirm that I would like to voluntarily participate in the research.<br><br></h4>

      <v-btn
        @click="onClickNext"
        color="deep-purple accent-2"
        class="mr-4 right_button"
        dark
      >
        Agree & Next
      </v-btn>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'PreSurvey',
  methods: {
    onClickNext: function () {
      const self = this;
      self.$helpers.server_call(self, function(self, res){ // eslint-disable-line no-unused-vars
        self.$router.push('annotation')
      }, "/record_pre_done")
    }
  },
  beforeMount() {
    this.$helpers.isWrongAccess(this)
  }
}
</script>
