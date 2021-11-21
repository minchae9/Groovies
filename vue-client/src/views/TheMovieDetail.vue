<template>
  <div id="movieDetail">
    movie Detail: {{this.$route.params.movie_id}}
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'MovieDetail',
    data: function () {
        return {
          movie: null,  // 여기에 영화 데이터 넣어 놨습니다!
          movie_id: this.$route.params.movie_id,
        }
    },
    methods: {

    },
    created: function () {
      // axios
      axios({
        method: 'get', 
        url: `http://127.0.0.1:8000/movies/${this.movie_id}`,
      })
        .then(res => {
          // console.log(res)
          this.movie = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
}
</script>

<style>

</style>