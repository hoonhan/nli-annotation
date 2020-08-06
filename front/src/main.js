import Vue from 'vue'
import App from './App.vue'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import global from './plugins/global';

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  global,
  render: h => h(App)
}).$mount('#app')
