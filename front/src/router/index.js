import Vue from 'vue'
import VueRouter from 'vue-router'
import Landing from '../views/Landing.vue'
import Introduction from '../views/Introduction.vue'
import PreSurvey from '../views/PreSurvey.vue'
import Annotation from '../views/Annotation.vue'
import AfterDone from '../views/AfterDone.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Landing',
    component: Landing
  },
  {
    path: '/introduction',
    name: 'Introduction',
    component: Introduction
  },
  {
    path: '/presurvey',
    name: 'PreSurvey',
    component: PreSurvey
  },
  {
    path: '/annotation',
    name: 'Annotation',
    component: Annotation
  },
  {
    path: '/after-done',
    name: 'AfterDone',
    component: AfterDone
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
