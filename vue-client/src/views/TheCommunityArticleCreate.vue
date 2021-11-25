<template>
  <div id="CommunityArticleCreate">
    <div id="community-article">
      <div id="article-body">
        <label for="title">제목: </label>
        <input v-model="article.title" type="text" id="title" style="width: 20rem;" placeholder="제목을 입력하세요">
        <div id="article-header">
          <div>
            작성자: {{ loginUser.nickname ? loginUser.nickname : loginUser.username }} ({{ loginUser.username }})
          </div>
        </div>
      </div>
      <div>
        <p>
          <label for="movie_title">영화 제목:</label>
          <input v-model="article.movie_title" type="text" id="movie_title" placeholder="영화 제목을 입력하세요">
        </p>
      </div>
      <div id="article-content-box">
        <p id="article-content">
          <label for="content">내용:</label>
          <textarea v-model="article.content" class="textarea" id="content" placeholder="내용을 입력하세요"></textarea>
        </p>
      </div>
      <div id="article-footer">
        <button v-if="this.$route.query.article > 0" @click="updateArticle">수정</button>
        <button v-else @click="createArticle" class="btn btn-primary">작성</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL
const AUTH_JWT_TOKEN = { Authorization : `JWT ${localStorage.getItem('jwt')}`}

export default {
  name: 'CommunityArticleCreate',
  data: function () {
    return {
      article: {
        title: '',
        movie_title: '',
        content: '',
      },
    }
  },
  methods: {
    createArticle: function () {
      axios({
        method: 'post',
        url: `${SERVER_URL}/community/create/`,
        headers: AUTH_JWT_TOKEN,
        data: this.article
      })
        .then((res) => {
          console.log(res)
          this.$router.push({ name: 'CommunityArticle', params: { article_id: res.data.id }})
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateArticle: function () {
      axios({
        method: 'put',
        url: `${SERVER_URL}/community/${this.$route.query.article}/`,
        headers: AUTH_JWT_TOKEN,
        data: this.article
      })
        .then(res => {
          this.$router.push({ name: 'CommunityArticle', params: { article_id: res.data.id }})
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created: function () {
    // 유저 정보 받아오기
    if (localStorage.getItem('jwt')) {
        // 유저 정보 추출
      const JWTtoken = localStorage.getItem('jwt')
      const base64Payload = JWTtoken.split('.')[1]; //value 0 -> header, 1 -> payload, 2 -> VERIFY SIGNATURE 
      const payload = Buffer.from(base64Payload, 'base64'); 
      const result = JSON.parse(payload.toString()) 
      // console.log(result)
      this.userId = result.user_id
      this.username = result.username
    }
    // 업데이트인 경우, 게시글 정보 받아오기
    if (this.$route.query.article) {
      // console.log(this.$route.query.article)
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/${this.$route.query.article}/`
      })
        .then(res => {
          // console.log(res)
          this.article.title = res.data.title
          this.article.movie_title = res.data.movie_title
          this.article.content = res.data.content
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  computed: {
    ...mapState([
      'login',
      'loginUser',
    ])
  }

}
</script>

<style>

</style>
