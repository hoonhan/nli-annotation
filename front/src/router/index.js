import Vue from 'vue'
import VueRouter from 'vue-router'
import Instruction from '../views/Instruction.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Instruction',
    component: Instruction
  },
  {
    path: '/annotation',
    name: 'Annotation',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Annotation.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
