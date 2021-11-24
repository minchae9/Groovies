<template>
  <div id="CommunityArticle">
    <div id="community-article">
      <div id="article-body">
        <h1>{{ article.title }}</h1>
        <div id="article-header">
          <div>
            <img v-if="article.profile_path >= 0" :src="require(`@/assets/profile_img_${article.profile_path}.jpg`)" 
            class="profile-img" alt="profile_img">
            <span class="article-list-item-user" @click="moveToUserProfile(article.user)">{{ article.nickname }}</span>
          </div>
          <div>
            <p>작성  |  {{ article.created_at | convertFormat }}</p>
            <p>수정  |  {{ article.updated_at | convertFormat }}</p>
            <button @click="updateArticle(article)" v-if="(userInfo && article.user === userInfo.user_id)">수정</button>
            <button @click="deleteArticle(article)" v-if="(userInfo && article.user === userInfo.user_id)">삭제</button>
          </div>
        </div>
        <div id="article-content-box">
          <div v-if="article.movie_title">
            <p>영화: <b>《 {{ article.movie_title }} 》</b></p>
          </div>
          <p id="article-content">
            {{ article.content }}
          </p>
        </div>
      </div>

        <button v-if="userInfo" id="like-button" @click="toggleLike">
          <i class="fa-heart" :class="[{ fas: likeState }, { far: !likeState }]"></i>
          <span>{{likeUsersCount}}</span>
        </button>
        <button v-else id="like-button" @click="toggleLike" disabled>
          <i class="fa-heart" :class="[{ fas: likeState }, { far: !likeState }]"></i>
          <span>{{likeUsersCount}}</span>
        </button>

      <div id="article-comments-box">
        <div id="article-comment-title">댓글 ({{comments.length}})</div>
          <ul id="article-comments">
            <li class="article-comment" v-for="(comment, index) in comments" :key="index">
              <div>
                <img :src="require(`@/assets/profile_img_${comment.profile_path}.jpg`)" 
              class="profile-img comment-profile-img" alt="profile_img">
              </div>
              <div class="comment-username">{{ comment.username }}</div>
              <div class="comment-content">{{ comment.content }}</div>
              <div class="comment-created-at">{{ comment.created_at | convertFormat }}</div>
              <button @click="deleteComment(comment)" v-if="(userInfo && comment.user === userInfo.user_id)">삭제</button>
            </li>
          </ul>
        </div>


      <div id="comment-input-box">
        <textarea v-if="login" id="comment-input" placeholder="댓글을 입력해주세요 :)"
        :commentInput="commentInput" @input="onCommentInput" @keypress.enter="createComment"
        ></textarea>
        <textarea v-else id="comment-input" placeholder="로그인 후 이용 가능한 기능입니다."
        :commentInput="commentInput" @input="onCommentInput" @keypress.enter="createComment"
        ></textarea>
        <button id="comment-button" @click="createComment" class="btn btn-primary">작성</button>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'CommunityArticle',
    data: function () {
      return {
        article: {},  // 게시글 정보 + 유저 id (as 'user), username, nickname, profile_path
        comments: [],
        commentInput: '',
        likeState: false,
        likeUsersCount: 0,
      }
    },
    methods: {
      onCommentInput: function (event) {
        this.commentInput = event.target.value
      },
      moveToUserProfile: function (user_id) {
        this.$router.push({ name: 'UserProfile', params: { user_id: user_id }})
      },
      createComment: function () {
        if (this.commentInput) {
          axios({
            method: 'post',
            url: `http://127.0.0.1:8000/community/${this.article.id}/comment/create/`,
            data: { content: this.commentInput },
            headers: { Authorization : `JWT ${localStorage.getItem('jwt')}`}
          })
            .then(() => {
              this.$router.go()
            })
            .catch(() => {
              console.log(this.commentInput)
            })

          // reset commentInput
          this.commentInput = ''
          const commentInputElem = document.querySelector('#comment-input')
          commentInputElem.value = ''
        }
      },
      toggleLike: function () {
        // 좋아요 정보 저장하기
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/community/${this.article.id}/like/${this.$store.state.loginUser.user_id}/`,
          headers: { Authorization : `JWT ${localStorage.getItem('jwt')}`}
        })
          .then(() => {})
          .catch(err => {
            console.log(err)
          })
        // 하트와 좋아요 수 변경
        if (localStorage.getItem('jwt')) {
          if (this.likeState) {
          this.likeState = false
          if (this.likeUsersCount > 0) {
            this.likeUsersCount--
            }
          } else {
            this.likeState = true
            this.likeUsersCount++
          }
        }
      },
      deleteComment: function (comment) {
        axios({
          method: 'delete',
          url: `http://127.0.0.1:8000/community/${this.article.id}/comment/${comment.id}/`,
          headers: { Authorization : `JWT ${localStorage.getItem('jwt')}`}
        })
          .then(() => {
            this.$router.go()
          })
          .catch(err => {
            console.log(err)
          })
      },
      updateArticle: function (article) {
        this.$router.push({ name: 'CommunityArticleCreate', query: {article: article.id}})
      },
      deleteArticle: function (article) {
        axios({
          method: 'delete',
          url: `http://127.0.0.1:8000/community/${article.id}/`,
          headers: { Authorization : `JWT ${localStorage.getItem('jwt')}`}
        })
          .then(() => {
            this.$router.push({ name: 'Community' })
          })
          .catch(err => {
            console.log(err)
          })
      },
      getLikeState: function (article_id) {
        axios.get(`http://127.0.0.1:8000/community/${article_id}/like/${this.$store.state.loginUser.user_id}/`)
          .then(res => {
            // console.log(res)
            this.likeState = res.data.liked
            this.likeUsersCount = res.data.count
          })
          .catch(err => {
            console.log(err)
          })
      },
    },
    created: function () {
      const article_id = this.$route.params.article_id
      // axios
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/${article_id}`
      })
        .then(res => {
          // console.log(res.data)
          this.article = res.data
          this.likeUsersCount = res.data.like_article_users.length
        })
        .catch(err => {
          console.log(err)
        })
      
      // 댓글
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/${article_id}/comment/`
      })
        .then(res => {
          // console.log(res)
          this.comments = res.data
        })
        .catch(err => {
          console.log(err)
        })  
      // 좋아요 상태
      this.getLikeState(article_id)
    },
    // updated: function () {
    //   this.getLikeState(this.article.id)
    // },
    filters: {
      convertFormat: function (string) {
        return string? `${string.slice(0,4)}년 ${string.slice(5,7)}월 ${string.slice(8,10)}일 ${string.slice(11,16)}` : ''
      }
    },
    computed: {
      login: function () {
        return (this.$store.state.loginUser !== null)
      },
      userInfo: function () {
        return this.$store.state.loginUser
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

  #like-button {
    background-color: transparent;
    height: 2rem;
    width: 4rem;
    border-radius: 1rem;
    border: 1px solid rgb(165, 165, 165);
    color: white;
    margin-top: 4rem;
  }

  .fa-heart {
    color: crimson;
    margin-right: 0.5rem;
  }

  #article-comments-box {
    margin-top: 3rem;
  }

  #article-comment-title {
    font-family: scd6;
    /* font-size: 1.25rem; */
    text-align: left;
    margin-bottom: 0.25rem;
  }

  #article-comments {
    list-style: none;
    padding: 0;
    border-top: 1px solid white;
    border-bottom: 1px solid white;
    
  }

  .article-comment {
    padding: 2rem 0;
    border-bottom: 1px solid rgb(165, 165, 165);
    display: flex;
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

  .comment-content {
    flex-grow: 1;
    text-align: left;
    border-left: 1px solid white;
    padding: 0 1rem;
  }

  #article-header > div:last-child,
  .comment-created-at {
    font-size: 0.75rem;
    color: rgb(151, 151, 151);
  }

  .comment-username,
  .comment-content,
  .comment-created-at {
    display: flex;
    align-items: center;
  }

  #comment-input-box {
    display: flex;
  }

  #comment-input {
    width: 100%;
    height: 4rem;
    resize: none;
    padding: .5rem;
    border: none;
  }

  #comment-button {
    width: 128px;
    height: 4rem;
    border: none;
    border-radius: 0 0.25rem 0.25rem 0;
  }



</style>