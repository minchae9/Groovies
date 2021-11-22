<template>
  <div id="search">
      <search-bar></search-bar>
      <movie-list v-if="keyword" :movieItems="movieItems"></movie-list>
      <div v-if="!keyword">관심 있는 키워드 혹은 영화 제목을 검색해보세요!</div>
  </div>
</template>

<script>
import SearchBar from '../components/SearchBar.vue'
import MovieList from '../components/MovieList.vue'
import axios from 'axios'

export default {
  components: { SearchBar, MovieList },
    name: 'Search',
    data: function () {
        return {
            movieItems: [],
        }
    },
    props: {
        keyword: String,
    },
    methods: {
        getSearchResult: function() {
            // axios
            // 검색 결과 리스트 가져오기
            // console.log('검색어:', this.keyword)

            axios({
                method: 'get', 
                url: `http://127.0.0.1:8000/movies/search/${this.keyword}`
            })
            .then(res => {
                console.log('search result: ', res)
                this.movieItems = res.data
            })
            .catch(err => {
                console.log(err)
            })
        }

    },
    computed: {
    },
    created: function () {
        if (this.keyword) {
            // console.log('검색어:', this.searchKeyword)
            //axios
            this.getSearchResult()
        }
    },
    watch:  {
        keyword: function () {
            this.getSearchResult()
        },
    },
}
</script>

<style>

</style>