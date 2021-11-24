<template>
  <div id="community">
    <h1>커뮤니티</h1>
    <ul id="article-list" v-if="articleList">
      <li class="article-list-item" v-for="(articleListItem, index) in articleList" :key="index">
        <span class="article-list-item-title" 
        @click="moveToArticle(articleListItem.id)">
        {{ articleList ? articleListItem.title : null }}</span>
        <span class="article-list-item-user" 
          @click="moveToUserProfile(articleListItem.user)">
          {{ articleList ? articleListItem.nickname : null }}
        </span>
        <span>{{ articleList ? articleListItem.created_at : null | convertFormat }}</span>
      </li>
    </ul>
    <div v-else>
      <h2>첫 게시글을 남겨주세요.</h2>
    </div>
    <button v-if="this.$store.state.loginUser" @click="createArticle">작성</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Community',
    data: function () {
      return {
        articleList: [],  // 배열. 각 원소에 id(article pk), title, user(user pk), username(아이디) 들어있음.
      }
    },
    methods: {
      moveToArticle: function (article_id) {
        this.$router.push({ name: 'CommunityArticle', params: { article_id: article_id }})
      },
      moveToUserProfile: function (user_id) {
        this.$router.push({ name: 'UserProfile', params: { user_id: user_id }})
      },
      createArticle: function () {
        this.$router.push({ name: 'CommunityArticleCreate' })
      }
    },
    created: function () {
      //axios
      // 게시글 목록
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/community/'
      })
        .then (res => {
          this.articleList = res.data
          // console.log(res.data)      
        })
        .catch (err => {
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

</style>