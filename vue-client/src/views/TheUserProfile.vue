<template>
  <div>
    <h1>마이페이지</h1>

    <div id="basic_profile">
      <img v-if="profile_path" :src="require(`@/assets/profile_img_${profile_path}.jpg`)" class="profile" alt="profile_img">
      <div id="article-body">
        <p>닉네임: <b>{{ nickname }}</b></p>
        <p>아이디: {{ username }}</p>
        <button @click="updateProfile">회원정보 수정</button>
      </div>
    </div>
    <hr>
    <div id="article-content-box">

      <div id="movieList">

        <div>
          <h3>평점을 등록한 영화</h3>
          <ul v-if="ratedMovies">
            <div v-for="(ratedMovie, index) in ratedMovies" :key="index">
              <button @click="moveToMovie(ratedMovie.id)">
                <img v-if="ratedMovie.poster_path" :src="moviePoster(ratedMovie)" class="poster" alt="poster_img">
              </button>
              <a @click="moveToMovie(ratedMovie.id)" href="#">
                {{ ratedMovies ? ratedMovie.title : null }}
              </a>
            </div>
          </ul>
          <div v-else>
            영화에 평점을 등록해 보세요!
          </div>
        </div>
        <hr>
        <div>
          <h3>내가 찜한 영화</h3>
          <ul v-if="cartMovies">
            <div v-for="(cartMovie, index) in cartMovies" :key="index">
              <button @click="moveToMovie(cartMovie.id)">
                <img v-if="cartMovie.poster_path" :src="moviePoster(cartMovie)" class="poster" alt="poster_img">
              </button>
              <a @click="moveToMovie(cartMovie.id)" href="#">
                {{ cartMovies ? cartMovie.title : null }}
              </a>
            </div>
          </ul>
        </div>
      </div>
      <hr>
      <div id="articleList">
        <h3>내가 작성한 게시글</h3> 
        <ul id="article-list" v-if="articleList">
          <li class="article-list-item" v-for="(article, index) in articleList" :key="index">
            <span class="article-list-item-title" @click="moveToArticle(article.id)">
            {{ articleList ? article.title : null }}</span>
            <span>{{ articleList ? article.created_at : null | convertFormat }}</span>
          </li>
        </ul>
      </div>
      <hr>
      <div id="commentList">
        <h3>내가 남긴 영화 한마디</h3> 
        <ul id="article-list" v-if="commentList">
          <li class="article-list-item" v-for="(comment, index) in commentList" :key="index">
            <span class="article-list-item-title" @click="moveToMovie(comment.movie)">
            {{ commentList ? comment.content : null }}</span>
            <span>{{ commentList ? findCommentMovie(comment.movie) : null }}</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'UserProfile',
    data: function () {
      return {
        user_id: this.$route.params.user_id,
        username: '',
        nickname: '',
        profile_path: '',
        ratedMovies: null,
        cartMovies: null,
        articleList: null,
        commentList: null,
      }
    },
    methods: {
      updateProfile: function () {
        this.$router.push({ name: 'Signup' })
        this.$router.go()
      },
      moviePoster: function (movie) {
        return `https://image.tmdb.org/t/p/original/${movie.poster_path}`
      },
      findCommentMovie: function (movie_id) {
        axios.get(`http://127.0.0.1:8000/movies/${movie_id}/`)
          .then(res => {
            // console.log(res)
            return res.data.title
          })
          .catch(err => {
            console.log(err)
          })
      },
      moveToMovie: function (movie_id) {
        this.$router.push({ name: 'MovieDetail', params: { movie_id: movie_id }})
      },
      moveToArticle: function (article_id) {
        this.$router.push({ name: 'CommunityArticle', params: { article_id: article_id }})
      },
    },
    created: function () {
      // 유저 정보
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/profile/${this.user_id}/`
      })
        .then(res => {
          // console.log(res)
          this.username = res.data.username
          this.nickname = res.data.nickname
          this.profile_path = res.data.profile_path
        })
        .catch(err => {
          console.log(err)
        })
      // 찜한 영화 리스트
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/accounts/mycart/',
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}`}
        })
        .then(res => {
          this.cartMovies = res.data
        })
        .catch(err => {
          console.log(err)
        })
      // 평점을 남긴 영화 리스트
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/accounts/myrated/',
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}`}
        })
        .then(res => {
          this.ratedMovies = res.data
        })
        .catch(err => {
          console.log(err)
        })
      // 작성한 게시글
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/accounts/myarticles/',
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}`}
        })
        .then(res => {
          // console.log(res)
          this.articleList = res.data
        })
        .catch(err => {
          console.log(err)
        })
      // 남긴 한줄 댓글
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/accounts/mycomments/',
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}`}
        })
        .then(res => {
          // console.log(res)
          this.commentList = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    filters: {
      convertFormat: function (string) {
        return string? `${string.slice(0,4)}년 ${string.slice(5,7)}월 ${string.slice(8,10)}일 ${string.slice(11,16)}` : ''
      }
    },
}
</script>

<style>

</style>