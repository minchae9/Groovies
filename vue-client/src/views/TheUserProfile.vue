<template>
  <div>
      <div class="page-title" style="margin-bottom: 1.5rem;">
        <h1>{{ isMyself ? '마이페이지' : '유저정보' }} </h1>
        <div class="line"></div>
      </div>

    <div id="basic-profile">
      <img v-if="(profile_path !== undefined) && (profile_path !== null) && (profile_path !== '')" :src="require(`@/assets/profile_img_${profile_path}.jpg`)" class="profile" alt="profile_img">
      <div id="article-body">
        <div>닉네임: <span style="font-family:scd5;">{{ nickname }}</span></div>
        <div>아이디: {{ username }}</div>
        <button @click="updateProfile" class="btn btn-secondary" v-if="isMyself" style="margin-top: 1rem;">회원정보 수정</button>
      </div>
    </div>
    <hr>
    <div id="article-content-box">

      <div>

        <div>
          <h3>별점을 등록한 영화</h3>
          <ul v-if="ratedMovies" class="movieList">
            <li @click="moveToMovie(ratedMovie.id)" 
            v-for="(ratedMovie, index) in ratedMovies" :key="index" class="item profile-movie-item">
              <img v-if="ratedMovie.poster_path" :src="moviePoster(ratedMovie)" class="poster" alt="poster_img">
              <div>
                {{ ratedMovies ? ratedMovie.title : null }}
              </div>
            </li>
          </ul>
          <div v-else>
            {{ isMyself ? '영화에 별점을 등록해 보세요!' : '아직 등록한 별점이 없어요'}}
          </div>
        </div>
        <hr>
        <div>
          <h3>{{ isMyself ? '내가' : `${nickname}님이` }} 찜한 영화</h3>
          <ul v-if="cartMovies" class="movieList">
            <li v-for="(cartMovie, index) in cartMovies" :key="index" @click="moveToMovie(cartMovie.id)" class="item profile-movie-item">
              <img v-if="cartMovie.poster_path" :src="moviePoster(cartMovie)" class="poster" alt="poster_img">
              <div>
                {{ cartMovies ? cartMovie.title : null }}
              </div>
            </li>
          </ul>
          <div v-else>
            {{ isMyself ? '영화를 카트에 담아보세요!' : '아직 찜한 영화가 없어요'}}
          </div>
        </div>
      </div>
      <hr>
      <div id="articleList">
        <h3>{{ isMyself ? '내가' : `${nickname}님이` }} 작성한 게시글</h3> 
        <ul id="article-list" v-if="articleList && !articleList.message">
          <li class="article-list-item" v-for="(article, index) in articleList" :key="index">
            <span class="article-list-item-title" @click="moveToArticle(article.id)">
            {{ articleList ? article.title : null }}</span>
            <div class="article-time">{{ articleList ? article.created_at : null | convertFormat }}</div>
          </li>
        </ul>
        <div v-else>
          {{ isMyself ? '커뮤니티에 게시글을 작성해보세요!' : '아직 작성한 게시글이 없어요'}}
        </div>
      </div>
      <hr>
      <div id="commentList">
        <h3>{{ isMyself ? '내가' : `${nickname}님이` }} 남긴 영화 한마디</h3> 
        <ul id="article-list" v-if="commentList">
          <li class="article-list-item" v-for="(comment, index) in commentList" :key="index">
            <span class="article-list-item-title" @click="moveToMovie(comment.movie)">
            {{ commentList ? comment.content : null }}</span>
            <div>{{ commentList ? findCommentMovie(comment.movie) : null }}</div>
          </li>
        </ul>
        <div v-else>
          {{ isMyself ? '영화에 한마디를 남겨보세요!' : '아직 남긴 영화 한마디가 없어요'}}
        </div>
      </div>
    </div>
    <div>
      <a @click="deleteAccount" href="#" style="color: gray;" v-if="isMyself">회원탈퇴</a>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

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
      deleteAccount: function () {

        axios.delete(`http://127.0.0.1:8000/accounts/profile/${this.user_id}/delete/`)
          .then(() => {
            this.$store.dispatch('logout')
          })
          .then(() => {
            this.$router.push({ name: 'Home' })
          })
          .catch(err => {
            console.log(err)
          })
      },
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
        this.nickname = res.data.nickname ? res.data.nickname : '(없음)'
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
  computed: {
    ...mapState([
      'isMyself'
    ])
  }
}
</script>

<style>
  #article-content-box {
    width: 70%;
    margin: 0 auto;
  }

  #basic-profile > img {
    margin: 0;
    margin-bottom: 1rem;
  }

  h3 {
    font-size: 1.5rem;
  }

  .movieList {
    list-style-type: none;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }

  .item {
    display: inline-block;
    margin: 0.25rem;
  }

  .item.profile-movie-item {
    cursor: pointer;
    margin-bottom: 1rem;
  }


</style>