<template>
  <div id="search">
      <search-bar></search-bar>
      <movie-list v-if="searchKeyword" :movieItems="movieItems"></movie-list>
      <div v-if="!searchKeyword">관심 있는 키워드 혹은 영화 제목을 검색해보세요!</div>
  </div>
</template>

<script>
import SearchBar from '../components/SearchBar.vue'
import MovieList from '../components/MovieList.vue'

import { mapState } from 'vuex'

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
            // 검색 결과 리스트 가져오기
            console.log('검색어:', this.searchKeyword)
            const temp_search_result = [
                {src: 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDAxMTdfMjY0%2FMDAxNTc5MjQ5MjY5MzIz.u1hs58UcFXw7_K2tsr2apCkdR-PGbZwRinw8Kc9yb7Ig.XNEWNQP2vozHEK9XyuoF9AhNdmDtecULHq_W_LUOVHog.JPEG.0114suji%2FIMG_7760.JPG&type=a340',
                title: 'temp1',
                id: 1},
                {src: 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20140811_95%2Fghostqueen7_1407752073986cOyhr_JPEG%2Fpropa-ganda_co_kr_20140811_173531.jpg&type=a340',
                title: 'temp2',
                id: 2},
                {src: 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxNjEwMjNfMjM0%2FMDAxNDc3MTk1MjcwNzYx.BxDGgZ9I-AS82dFw7pc_k9QaIzgnQN9Wti0fq3v3piEg.faDtUFA2M1tfJytlXD9ZWxbI24n5DAs4J_rheTOBJYkg.PNG.ilovsky%2FIMG_20161023_7.png&type=a340',
                title: 'temp3',
                id: 3},
                {src: 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxNzA2MzBfMTA3%2FMDAxNDk4ODEyNDQ4Mzgw.v3IR9R1b3hIwySH32BV2Evay8qA_WBMYqdKQMSNdBGQg.WoJ-7Gfeg47Rv1wA8t4y6Q5bVwYaPNLgNVbp-LXSRGgg.JPEG.designpress2016%2F4%25B5%25EE3.jpg&type=a340',
                title: 'temp4',
                id: 4},
                {src: 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20111208_252%2Fpyokisix_1323353779185DTi1y_JPEG%2F%25BB%25E7%25C1%25F8.JPG&type=a340',
                title: 'temp5',
                id: 5},
                {src: 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxODEwMjNfMjAy%2FMDAxNTQwMjg2Njk1ODMz.EuZPjKdInUivbXJ7hR6-JRK1QbLElz-5RALG_dAexvwg.nXK2pWqqe3IvSYfnmTYbTeLsMhYwPKQwgzh7pW8AmBwg.JPEG.vnfmatlsgh%2FSoubusenCombi_ver.jpg&type=a340',
                title: 'temp6',
                id: 6},
            ]

            this.movieItems = temp_search_result
        }

    },
    computed: {
        ...mapState([
                'searchKeyword',
            ])
    },
    created: function () {
        if (this.searchKeyword) {
            console.log('검색어:', this.searchKeyword)
            //axios
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