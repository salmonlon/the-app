import Vue from 'vue'
import VueRouter from 'vue-router'

import store from '@/store'

import Home from '@/views/Home.vue'
import Register from '@/views/Register.vue'
import Login from '@/views/Login.vue'
import Note from '@/views/Note.vue'
import EditNote from '@/views/EditNote.vue'
import Dashboard from '@/views/Dashboard.vue'
import Profile from '@/views/Profile.vue'
import Admin from '@/views/Admin.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: {requiresAuth: true}
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
    meta: {requiresAuth: true}
  },
  {
    path: '/note/:id',
    name: 'Note',
    component: Note,
    meta: {requiresAuth: true},
    props: true,
  },
  {
    path: '/editnote/:id',
    name: 'EditNote',
    component: EditNote,
    meta: {requiresAuth: true},
    props: true,
  },
  {
    path: '/admin',
    name: 'Admin',
    component: Admin,
    meta: {requiresAuth: true, requiresAdmin: true}
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '@/views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// navigation guards https://router.vuejs.org/guide/advanced/navigation-guards.html
router.beforeEach((to, from, next) => {
  // if the router requires auth, check if user is authenticated
  // if not, redirect to login page
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if(store.getters.isAuthenticated) {
      next();
      return;
    }
    store.dispatch('logout');
    next('/login');
  } else {
    next();
  }
});

export default router
