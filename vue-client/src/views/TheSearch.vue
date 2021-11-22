<template>
  <div id="search">
      <search-bar></search-bar>
      <h1 v-if="searchKeyword">검색 결과</h1>
      <br>
      <movie-list v-if="(searchKeyword, movieItems)" :movieItems="movieItems"></movie-list>
      <div v-if="!searchKeyword">관심 있는 키워드 혹은 영화 제목을 검색해보세요!</div>
      <div v-if="!movieItems">조회된 결과가 없습니다. 새로운 검색어를 입력해주세요.</div>
  </div>
</template>

<script>
import SearchBar from '../components/SearchBar.vue'
import MovieList from '../components/MovieList.vue'

import { mapState } from 'vuex'
import axios from 'axios'

export default {
  components: { SearchBar, MovieList },
    name: 'Search',
    data: function () {
        return {
            movieItems: [],
        }
    },
    methods: {
        getSearchResult: function() {
            // axios
            axios({
                method: 'get',
                url: `http://127.0.0.1:8000/movies/search/${this.searchKeyword}`,
            })
                .then(res => {
                    this.movieItems = res.data
                })
                .catch(err => {
                    console.log(err)
                })
        },

    },
    computed: {
        ...mapState([
                'searchKeyword',
            ])
    },
    created: function () {
        if (this.searchKeyword) {
            // console.log('검색어:', this.searchKeyword)
            this.getSearchResult()
        }
    },
    watch:  {
        searchKeyword: function () {
            this.getSearchResult()
        },
    },
}
</script>

<style>

</style>