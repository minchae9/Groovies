<template>
  <div id="CommunityArticle">
    <div id="community-article">
      <div id="article-body">
        <h1>{{ article.title }}</h1>
        <div id="article-header">
          <div>
            <img v-if="article.profile_path" :src="require(`@/assets/profile_img_${article.profile_path}.jpg`)" 
            class="profile-img" alt="profile_img">
            {{ article.username }}
          </div>
          <div>
            <p>작성  |  {{ article.created_at | convertFormat }}</p>
            <p>수정  |  {{ article.updated_at | convertFormat }}</p>
          </div>
        </div>
        <div id="article-content-box">
          <p id="article-content">
            {{ article.content }}
          </p>
          <div v-if="article.movie_title">
            <p>{{ article.movie_title }}</p>
          </div>
        </div>
      </div>

        <button id="like-button" @click="toggleLike">
          <i class="fa-heart" :class="[{ fas: isLikeUser }, { far: !isLikeUser }]"></i>
          <span>{{likeUsersCount}}</span>
        </button>

      <div id="article-comments-box">
        <div id="article-comment-title">댓글</div>
        <ul id="article-comments" v-if="comments==[]">
          <li class="article-comment" v-for="(comment, index) in comments" :key="index">
            <div>
              <img :src="require(`@/assets/profile_img_${comment.profile_path}.jpg`)" 
            class="profile-img comment-profile-img" alt="profile_img">
            </div>
            <div class="comment-username">{{ comment.username }}</div>
            <div class="comment-content">{{ comment.content }}</div>
            <div class="comment-created-at">{{ comment.created_at | convertFormat }}</div>
          </li>
        </ul>
        <div v-else>
          첫 댓글을 작성해보세요!
        </div>
        <br>
      </div>

      <div id="comment-input-box">
        <textarea id="comment-input" placeholder="댓글을 입력해주세요 :)"
        :commentInput="commentInput" @input="onCommentInput"
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
        article: {},
        comments: [],
        commentInput: '',
        isLikeUser: false,
        likeUsersCount: 0,
      }
    },
    methods: {
      onCommentInput: function (event) {
        this.commentInput = event.target.value
      },
      createComment: function () {
        if (this.commentInput) {
          // axios
          // console.log('댓글 작성!: ', this.commentInput)
          // axios({
          //   method: 'post',
          //   url: `http://127.0.0.1:8000/${this.article.id}/comment/create/`,
          //   data: { comment: {
          //     content : this.commentInput,
          //     article_id: this.article.id,
          //     user_id: 
          //   }}
          // })
          //   .then(res => {
          //     console.log(res)
          //   })
          //   .catch(err => {
          //     console.log(err)
          //   })
          

          // comments에 작성 댓글 추가

          // reset commentInput
          this.commentInput = ''
          const commentInputElem = document.querySelector('#comment-input')
          commentInputElem.value = ''
        }
      },
      toggleLike: function () {
        if (this.isLikeUser) {
          // 좋아요 취소
          // axios
          console.log('좋아요 취소')
          this.isLikeUser = false
          if (this.likeUsersCount > 0) {
            this.likeUsersCount--
          }
          

        } else {
          // 좋아요 누르기
          // axios
          console.log('좋아요 누르기')
          this.isLikeUser = true
          this.likeUsersCount++
        }
      }
    },
    created: function () {
      const article_id = this.$route.params.article_id
      // console.log(article_id)
      // axios
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/${article_id}`
      })
        .then(res => {
          // console.log(res)
          this.article = res.data
          this.likeUsersCount = res.data.like_article_users | length
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
    },
    filters: {
      convertFormat: function (string) {
        return string? `${string.slice(0,4)}년 ${string.slice(5,7)}월 ${string.slice(8,10)}일 ${string.slice(11,16)}` : ''
      }
    },
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