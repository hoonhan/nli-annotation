<template>
  <v-container fill-height>
    <v-row justify="center">
    <v-col style="text-align: center;">
      <v-card>
        <v-card-text>
        <h2>Please carefully read the introduction below.<br>
        As it is expected to take a minute to read, 
        <span v-if="time_now < 60" class="red">you can leave this page after {{60 - time_now}} seconds from now.</span>
        <span v-else class="red"> you can leave this page now.</span>
        </h2>
        </v-card-text>
      </v-card>
      <br>
      <v-divider/>
    </v-col>
    </v-row>
    <v-row justify="center" align="start">
    <v-col style="text-align: center;">
      <v-carousel 
        hide-delimiter-background
        :continuous="false"
        height="36rem"
        style="width:100%; margin-left:auto; margin-right:auto;">
        <v-carousel-item
          v-for="(item,i) in items"
          :key="i">

        <v-img v-if="i<4" :src="item.src" :contain="true" style="width:auto; max-height:100%; max-width:100%;">
          <template v-slot:placeholder>
            <v-row
              class="fill-height ma-0"
              align="center"
              justify="center"
            >
              <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
            </v-row>
          </template>  
        </v-img>
        <v-row v-else justify="center" align='center' style="height: 100%;"><v-col>
        <v-card class="endPanel">
          <v-card-text>
            <div v-if="passOneMinute === false">
              <h2>You may read the instruction too fast.<br><br>
              Why don't you read it again? :-)</h2>
            </div>
            <div v-else>
              <h2>Introduction Ended!<br><br>
              Click the button to proceed to the next page.</h2>
            </div>
          </v-card-text>
          <v-card-actions>
          <v-btn
            :disabled="!passOneMinute"
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
    time_now: 0,
    passOneMinute: false,
    items: [
      {src: require('@/assets/tutorial_a_1.png')},
      {src: require('@/assets/tutorial_a_2.png')},
      {src: require('@/assets/tutorial_a_3.png')},
      {src: require('@/assets/tutorial_a_4.png')},
      {}
    ]
  }),
  methods: {
    onClickNext: function () {
      const self = this;

      self.$helpers.server_call(self, function(self, res){ // eslint-disable-line no-unused-vars
        self.$router.push('presurvey')
      }, "/record_intro_done")
    }
  },
  beforeMount: function () {
    this.$helpers.isWrongAccess(this)
  },
  created: function () {
    setTimeout(() => {
      this.passOneMinute = true
    }, 60*1000);
    setInterval(() => {
      this.time_now += 1
    }, 1000);
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

.red {
  color:red;
  background-color:white !important;
}
</style>