<template>
  <v-container fill-height>
    <v-row justify="center">
    <v-col style="text-align: center;">
      <v-carousel 
        hide-delimiter-background
        :continuous="false"
        height="36rem"
        style="width:100%; margin-left:auto; margin-right:auto;">
        <v-carousel-item
          v-for="(item,i) in items"
          :key="i">

        <v-img v-if="i<4" :src="item.src" :contain="true" style="width:auto; max-height:100%; max-width:100%;"/>
        <v-row v-else justify="center" align='center' style="height: 100%;"><v-col>
        <v-card class="endPanel">
          <v-card-text>
          <h2>Tutorial Ended!<br><br>
          Click the button below to proceed to the pre-task questionnaire.</h2>
          </v-card-text>
          <v-card-actions>
          <v-btn
            @click="onClickNext"
            color="deep-purple accent-2"
            class="mr-4"
            style="margin-left: auto;"
            large
          >
            Next
          </v-btn>
          </v-card-actions>
        </v-card>
        </v-col></v-row>

        </v-carousel-item>
      </v-carousel>
    </v-col>
    </v-row>
  </v-container>
</template>


<script>
export default {
  name: 'Introduction',
  data: () => ({
    items: [
      {src: require('@/assets/tutorial_1.png')},
      {src: require('@/assets/tutorial_2.png')},
      {src: require('@/assets/tutorial_3.png')},
      {src: require('@/assets/tutorial_4.png')},
      {}
    ]
  }),
  methods: {
    onClickNext: function () {
      const self = this;
      console.log()

      self.$helpers.server_call(self, function(self, res){ // eslint-disable-line no-unused-vars
        self.$router.push('/presurvey')
      }, "/record_intro_done")
    }
  },
  beforeMount() {
    this.$helpers.isWrongAccess(this)
  }
}
</script>

<style scoped>
.v-responsive__content {
  align-content: center !important;
  display: flex !important;;
}

.v-card__text {
  color:black !important;
}

.endPanel {
  margin-left: auto;
  margin-right: auto;
  width: 70%;
  background-color: white !important;
}
</style>