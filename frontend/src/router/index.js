import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home')
  },
  {
    path: '/auth',
    name: 'Auth',
    component: () => import('../views/Auth')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  },
  {
    path: '/repo/:reponame',
    name: 'RepoSystem',
    component: () => import('../views/RepoSystem.vue')
  },
  {
    path: '/search/:username',
    name: 'SearchResult',
    component: () => import('../views/SearchResult.vue')
  },
  {
    path: '/logout',
    name: 'Logout',
    component: () => import('../views/Logout.vue')
  }
]



const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.name !== 'Auth' && !localStorage.getItem('token')) next({ name: 'Auth' })
  // if the user is not authenticated, `next` is called twice
  next()
})

export default router
