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
    server_url: 'http://3.35.47.70:8800/server'
  },
  mutations: {
    set_mturk_id (state, id){
      state.mturk_id = id
    }
  },
  actions: {
  },
  modules: {
  }
})
