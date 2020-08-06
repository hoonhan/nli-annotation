<template>
  <v-container fill-height>
    <v-row justify="center">
    <v-col style="text-align: center;">
      <v-carousel 
        hide-delimiter-background
        :continuous="false"
        height="36rem"
        style="width:70%; margin-left:14%">
        <v-carousel-item
          v-for="(item,i) in items"
          :key="i">

        <img v-if="i<5" :src="item.src" style="width:auto; height:100%;"/>
          <v-btn v-else
            @click="onClickNext"
            color="deep-purple accent-2"
            class="mr-4"
            style="margin-top:20%"
          >
            Next
          </v-btn>
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
      {src: require('@/assets/tutorial_5.png')},
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