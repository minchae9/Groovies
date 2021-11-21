import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Community from '@/views/TheCommunity.vue'
import CommunityArticle from '@/views/TheCommunityArticle.vue'
import Search from '@/views/TheSearch.vue'
import Signup from '@/views/TheSignup.vue'
import Login from '@/views/TheLogin.vue'
import MovieDetail from '@/views/TheMovieDetail.vue'
import UserProfile from '@/views/TheUserProfile.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/movies',
    name: 'Home',
    component: Home
  },
  {
    path: '/community',
    name: 'Community',
    component: Community
  },
  {
    path: '/community/:article_id',
    name: 'CommunityArticle',
    component: CommunityArticle
  },
  {
    // path: '/search/:searchKeyword',
    path: '/movies/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/movies/:movie_id',
    name: 'MovieDetail',
    component: MovieDetail 
  },
  {
    path: '/accounts/:user_id',
    name: 'UserProfile',
    component: UserProfile 
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})


export default router
