import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    searchKeyword: '',
    selectedMovie: {},
    loginUser: {},  // username과 user_id
    loginUser_nickname: '',
  },
  mutations: {
    ON_SEARCH: function (state, searchKeyword) {
      // console.log('mutations:onSearch', searchKeyword)
      state.searchKeyword = searchKeyword
    },
    RESET_SEARCH_KEYWORD: function (state) {
      state.searchKeyword = ''
    },
    UPDATE_MOVIE_DETAIL: function (state, movieDetail) {
      state.selectedMovie = movieDetail
    },
    STORE_LOGIN_USER: function (state, userInfo) {
      state.loginUser = userInfo
    },
    GET_NICKNAME: function (state, nickname) {
      state.loginUser_nickname = nickname
    }
  },
  actions: {
    onSearch: function ({ commit }, searchKeyword) {
      // console.log('actions:onSearch', searchKeyword)
      commit('ON_SEARCH', searchKeyword)
    },
    resetSearchKeyword: function ({ commit }) {
      commit('RESET_SEARCH_KEYWORD')
    },
    onClickMovieItem: function (context, selectedMovieId) {
      this.getMovieDetail(selectedMovieId)
    },
    getMovieDetail: function({ commit }, movieId) {
      // axios
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${movieId}/`,
      })
        .then(res => {
          // console.log(res)
          commit('UPDATE_MOVIE_DETAIL', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    storeLoginUser: function ({ commit }, userInfo) {
      commit('STORE_LOGIN_USER', userInfo)
    },
    getNickname: function ({ commit }, nickname) {
      commit('GET_NICKNAME', nickname)
    }
  },
  modules: {
  }
})
