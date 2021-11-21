<template>
  <div id="community">
    <ul id="article-list">
      <li class="article-list-item" v-for="(articleListItem, index) in articleList" :key="index">
        <span class="article-list-item-title" 
        @click="moveToArticle(articleListItem.id)">
        {{ articleListItem.title }}</span>
        <span class="article-list-item-user" 
        @click="moveToUserProfile(articleListItem.user.user_id)">
          {{ articleListItem.user.username }}</span>
        <span>{{ articleListItem.created_at }}</span>
      </li>
      <!-- list -->
    </ul>
  </div>
</template>

<script>
export default {
    name: 'Community',
    data: function () {
        return {
          articleList: [],
        }
    },
    methods: {
      moveToArticle: function (article_id) {
        this.$router.push({ name: 'CommunityArticle', params: { article_id: article_id }})
      },
      moveToUserProfile: function (user_id) {
        this.$router.push({ name: 'UserProfile', params: { user_id: user_id }})
      },
    },
    created: function () {
      //axios

      const temp_result = [
        {
          id: '1',
          title: '이 영화 재미없어요',
          user: {
            user_id: 1,
            username: 'une9',
          },
          created_at: '2021-11-21'
        },
        {
          id: '2',
          title: '인생작입니다.',
          user: {
            user_id: 2,
            username: 'abcd',
          },
          created_at: '2021-09-01'
        },
        {
          id: '3',
          title: '꼭 보세요',
          user: {
            user_id: 1,
            username: 'une9',
          },
          created_at: '2021-10-30'
        },
        {
          id: '4',
          title: 'ㅇㅇㅇ감독 새 영화 나온다는데 보실건가요?',
          user: {
            user_id: 3,
            username: 'happy',
          },
          created_at: '2021-11-01'
        },
      ]

      this.articleList = temp_result
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

</style>