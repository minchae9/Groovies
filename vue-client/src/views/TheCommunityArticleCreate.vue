<template>
  <div id="CommunityArticleCreate">
    <div id="community-article">
      <div id="article-body">
        <label for="title">제목: </label>
        <input v-model="article.title" type="text" id="title" style="width: 20rem;" placeholder="제목을 입력하세요">
        <div id="article-header">
          <div>
            작성자: {{ userNickname }}
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
        <button v-else @click="createArticle">작성</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CommunityArticleCreate',
  data: function () {
    return {
      article: {
        title: '',
        movie_title: '',
        content: '',
      },
      userId: '',
      username: '',
    }
  },
  methods: {
    createArticle: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/community/create/',
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}`},
        data: this.article
      })
        .then((res) => {
          this.$router.push({ name: 'CommunityArticle', params: { article_id: res.data.id }})
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateArticle: function () {
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/community/${this.$route.query.article}/`,
        headers: { Authorization: `JWT ${localStorage.getItem('jwt')}`},
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
    if (this.$route.query) {
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
    userNickname: function () {
      return this.$store.state.loginUser_nickname
    },
  }

}
</script>

<style>
  #community-article {
    width: 70%;
    max-width: 768px;
    margin: 0 auto;
  }

  #article-body h1 {
    font-size: 1.25rem;
    font-weight: normal;
    text-align: left;
  }

  #article-header {
    display: flex;
    padding: 1rem 0.5rem;
    border-top: 1px solid rgb(165, 165, 165);
    border-bottom: 1px solid rgb(165, 165, 165);
    margin: 1rem 0;
  }

  #article-header > div:first-child {
    flex-grow: 1;
    text-align: left;
    display: flex;
    align-items: center;
  }

  #article-content-box {
    margin-bottom: 2rem;
  }

  #article-content {
    text-align: left;
  }

  #article-header > div:last-child > p {
    margin-bottom: 0;
  }

  #article-footer {
    display: flex;
    padding: 1rem 0.5rem;
    border-top: 1px solid rgb(165, 165, 165);
    border-bottom: 1px solid rgb(165, 165, 165);
    margin: 1rem 0;
  }

  .textarea {
    width: 500px;
    height: 200px;
  }

  .fa-heart {
    color: crimson;
    margin-right: 0.5rem;
  }

  .profile-img {
    width: 30px;
    height: 30px;
    object-fit: cover;
    border-radius: 50%;
    margin-right: 0.5rem;
  }

  .comment-username {
    font-family: scd6;
    margin-right: 1rem;
  }

</style>