import Vue from 'vue'
import VueRouter from 'vue-router'
import Landing0 from '../views/baseline/Landing.vue'
import Introduction0 from '../views/baseline/Introduction.vue'
import PreSurvey0 from '../views/baseline/PreSurvey.vue'
import Annotation0 from '../views/baseline/Annotation.vue'
import AfterDone0 from '../views/baseline/AfterDone.vue'

import Landing1 from '../views/artificial/Landing.vue'
import Introduction1 from '../views/artificial/Introduction.vue'
import PreSurvey1 from '../views/artificial/PreSurvey.vue'
import Annotation1 from '../views/artificial/Annotation.vue'
import AfterDone1 from '../views/artificial/AfterDone.vue'

import Landing2 from '../views/natural/Landing.vue'
import Introduction2 from '../views/natural/Introduction.vue'
import PreSurvey2 from '../views/natural/PreSurvey.vue'
import Annotation2 from '../views/natural/Annotation.vue'
import AfterDone2 from '../views/natural/AfterDone.vue'

import VLanding from '../views/validation/Landing.vue'
import VIntroduction from '../views/validation/Introduction.vue'
import VGoldTask from '../views/validation/GoldTask.vue'
import VAnnotation from '../views/validation/Annotation.vue'
import VAfterDone from '../views/validation/AfterDone.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/baseline/home',
    name: 'Landing0',
    component: Landing0,
    alias: '/baseline'
  },
  {
    path: '/baseline/introduction',
    name: 'Introduction0',
    component: Introduction0
  },
  {
    path: '/baseline/presurvey',
    name: 'PreSurvey0',
    component: PreSurvey0
  },
  {
    path: '/baseline/annotation',
    name: 'Annotation0',
    component: Annotation0
  },
  {
    path: '/baseline/after-done',
    name: 'AfterDone0',
    component: AfterDone0
  },
  {
    path: '/artificial/home',
    name: 'Landing1',
    component: Landing1,
    alias: '/artificial'
  },
  {
    path: '/artificial/introduction',
    name: 'Introduction1',
    component: Introduction1
  },
  {
    path: '/artificial/presurvey',
    name: 'PreSurvey1',
    component: PreSurvey1
  },
  {
    path: '/artificial/annotation',
    name: 'Annotation1',
    component: Annotation1
  },
  {
    path: '/artificial/after-done',
    name: 'AfterDone1',
    component: AfterDone1
  },
  {
    path: '/natural/home',
    name: 'Landing2',
    component: Landing2,
    alias: '/natural'
  },
  {
    path: '/natural/introduction',
    name: 'Introduction2',
    component: Introduction2
  },
  {
    path: '/natural/presurvey',
    name: 'PreSurvey2',
    component: PreSurvey2
  },
  {
    path: '/natural/annotation',
    name: 'Annotation2',
    component: Annotation2
  },
  {
    path: '/natural/after-done',
    name: 'AfterDone2',
    component: AfterDone2
  },
  {
    path: '/validation/home',
    name: 'VLanding',
    component: VLanding,
    alias: '/validation'
  },
  {
    path: '/validation/introduction',
    name: 'VIntroduction',
    component: VIntroduction
  },
  {
    path: '/validation/gold-task',
    name: 'VGoldTask',
    component: VGoldTask
  },
  {
    path: '/natural/annotation',
    name: 'VAnnotation',
    component: VAnnotation
  },
  {
    path: '/validation/after-done',
    name: 'VAfterDone',
    component: VAfterDone
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
