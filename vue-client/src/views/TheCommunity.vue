<template>
  <div id="community">
    <div class="page-title">
      <h1>커뮤니티</h1>
      <div class="line"></div>
    </div>
    <button v-if="login == true" @click="createArticle" class="btn btn-primary article-create-button">게시글 작성</button>  
    <ul id="article-list" v-if="articleList && (articleList.length > 0)">
      <li class="article-list-item" v-for="(articleListItem, index) in articleList" :key="index">
        <span class="article-list-item-title" 
        @click="moveToArticle(articleListItem.id)">
        {{ articleList ? articleListItem.title : null }}</span>
        <span class="article-list-item-user" 
          @click="moveToUserProfile(articleListItem.user)">
          {{ articleList ? articleListItem.nickname : null }}
        </span>
        <span class="article-time">{{ articleList ? articleListItem.created_at : null | convertFormat }}</span>
      </li>
      <!-- list -->
    </ul>
    <div v-else style="margin-top: 8rem;">
      <h6 v-if="login == true">첫 게시글을 남겨주세요!</h6>
      <div v-else>
        <h6>아직 게시글이 없어요.</h6>
        <h6>로그인 후 첫 게시글을 남겨주세요!</h6>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
    name: 'Community',
    data: function () {
      return {
        articleList: [],   // 배열. 각 원소에 id(article pk), title, user(user pk), username(아이디) 들어있음.
      }
    },
    methods: {
      moveToArticle: function (article_id) {
        this.$router.push({ name: 'CommunityArticle', params: { article_id: article_id }})
      },
      moveToUserProfile: function (user_id) {
        this.$router.push({ name: 'UserProfile', params: { userid: user_id }})
      },
      createArticle: function () {
        this.$router.push({ name: 'CommunityArticleCreate' })
      }
    },
    filters: {
      convertFormat: function (string) {
        return string? `${string.slice(0,4)}년 ${string.slice(5,7)}월 ${string.slice(8,10)}일 ${string.slice(11,16)}` : ''
      }
    },
    created: function () {
      // 게시글 목록
      axios.get(`${SERVER_URL}/community/`)
        .then (res => {
          this.articleList = res.data   
        })
        .catch (err => {
          console.log(err)
        })
    },
    computed: {
      ...mapState([
        'login'
      ])
    }

  }

</script>

<style>
  #article-list {
    list-style: none;
    padding: 0;
    border-top: 4px solid white;
    border-bottom: 4px solid white;
    width: 70%;
    margin: 32px auto;
  }

  .article-list-item {
    border-bottom: 1px solid white;
    padding: 0.25rem;
    display: flex;
  }

  .article-list-item:hover {
    background-color: rgb(65, 65, 65);
  }

  .article-list-item:last-child {
    border: none;
  }

  .article-list-item > span {
    padding: 0 0.5rem;
  }

  .article-list-item-title {
    flex-grow: 1;
    text-align: left;
  }

  .article-list-item-title,
  .article-list-item-user {
    cursor: pointer;
  }

  .article-create-button {
    margin-top: -2rem;
  }

  .article-time {
    color: rgba(255, 255, 255, 0.5);
    font-size: 0.75rem;
    line-height: 1.5rem;
  }

</style>
