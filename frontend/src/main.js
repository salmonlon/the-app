import 'bootstrap/dist/css/bootstrap.css';
import axios from 'axios';
import { createApp } from 'vue'

import App from './App.vue'
import router from './router'
import store from './store'

axios.defaults.withCredentials = true

// set API backend URL
axios.defaults.baseURL = 'http://localhost:5001/'

// Vue.config.productionTip = false

// axios interceptors, redirects to login page if 401 unauthorized
axios.interceptors.response.use(undefined, function (error) {
  if (error) {
    const originalReqesut = error.config;
    if (error.response.status === 401 && !originalReqesut._retry) {
      originalReqesut._retry = true;
      store.dispatch('logout');
      router.push('/login');
    }
  }
});


const app = createApp(App)
app.use(store)
app.use(router)
app.mount('#app')