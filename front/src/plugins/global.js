import Vue from 'vue'
import helpers from './helpers'

const plugin = {
  install () {
    Vue.helpers = helpers
    Vue.prototype.$helpers = helpers
  }
}

export default {
  name: 'global'
}

Vue.use(plugin)