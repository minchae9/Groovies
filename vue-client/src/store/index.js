import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    searchKeyword: '',
    selectedMovie: {},
    loginUser: null,  // username과 user_id
    loginUser_nickname: '',
    loginUser_profile_path: 0,
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
    GET_USER_OTHERS: function (state, nickname, profile_path) {
      state.loginUser_nickname = nickname
      state.loginUser_profile_path = profile_path
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
      // 영화 정보
      let details = `http://127.0.0.1:8000/movies/${movieId}/`
      let actor = `http://127.0.0.1:8000/movies/${movieId}/actor/`
      let director = `http://127.0.0.1:8000/movies/${movieId}/director/`
      let similar = `http://127.0.0.1:8000/movies/${movieId}/similar/`
      
      const requestDetails = axios.get(details)
      const requestActor = axios.get(actor)
      const requestDirector = axios.get(director)
      const requestSimilar = axios.get(similar)

      axios.all([requestDetails, requestActor, requestDirector, requestSimilar])
        .then(axios.spread((...responses) => {
          const requestDetails = responses[0].data
          const requestActor = responses[1].data
          const requestDirector = responses[2].data
          const requestSimilar = responses[3].data
          const allDetails = {
            ...requestDetails,
            Actor: requestActor,
            Director: requestDirector,
            Similar: requestSimilar
          }
          commit('UPDATE_MOVIE_DETAIL', allDetails)
          // console.log(allDetails)
        }))
        .catch(err => {
          console.log(err)
        })
      
    },
    storeLoginUser: function ({ commit }, userInfo) {
      commit('STORE_LOGIN_USER', userInfo)
    },
    getUserOthers: function ({ commit }, nickname, profile_path) {
      commit('GET_USER_OTHERS', nickname, profile_path)
    }
  },
  modules: {
  }
})
