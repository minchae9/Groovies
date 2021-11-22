<template>
  <div id="CommunityArticleCreate">
    <div id="community-article">
      <div id="article-body">
        <label for="title">제목: </label>
        <input type="text" id="title">
        <div id="article-header">
          작성자: {{ user.id }}
        </div>
      </div>
      
    </div>
  </div>
  <!-- <div id="community-article">
    <div id="article-body">
      <label for="title"></label>
      <input type="text" id="title">
      <div id="article-header">
        <div>
          {{ user.username }}
        </div>
      </div>
      <div id="article-content-box">
        <p id="article-content">
          <label for="content"></label>
          <input type="text" id="content">
        </p>
        <div>
          <p>
            <label for="movie_title"></label>
            <input type="text" id="movie_title">
          </p>
        </div>
      </div>
    </div>
  </div> -->

</template>

<script>
export default {
  name: 'CommunityArticleCreate',
  // computed: {
  //   user: function () {
  //     pass
  //   }
  // }

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