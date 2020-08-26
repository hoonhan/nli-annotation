import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState({
    storage: window.sessionStorage,
  })],
  state: {
    mturk_id: null,
    server_url: 'http://localhost:8800/server',
    user_type: null
  },
  mutations: {
    set_mturk_id (state, id){
      state.mturk_id = id
    },
    set_user_type (state, type){
      // type: 0-baseline, 1-artificial, 2-natural
      state.user_type = type
    }
  },
  actions: {
  },
  modules: {
  }
})
