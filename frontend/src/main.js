import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import '@babel/polyfill'
import axios from 'axios'
import Notifications from 'vue-notification'
Vue.use(Notifications)
import VueAxios from "vue-axios"
Vue.use(VueAxios, axios)
import router from './router'

const api = axios.create({
  params: {
    t: new Date().getTime()
  }
})

Vue.prototype.$api = api

Vue.config.productionTip = false


new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
