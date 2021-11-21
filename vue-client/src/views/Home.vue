<template>
  <div>
      <carousel id="carousel" :movieItems="movieItems"></carousel>
      <search-bar id="home-search-bar"></search-bar>
      <movie-list :movieItems="movieItems"></movie-list>
  </div>
</template>

<script>
import Carousel from '../components/Carousel.vue'
import SearchBar from '../components/SearchBar.vue'
import MovieList from '../components/MovieList.vue'
import axios from 'axios'
import _ from 'lodash'

export default {
    components: { 
        Carousel, 
        SearchBar, 
        MovieList, 
    },
    name: 'Home',
    data: function () {
        return {
            movieItems: [],
        }
    },
    methods: {
        
    },
    created: function () {
        // axios
        // 추천 영화 가져오기
        axios({
            method: 'get', 
            url: 'http://127.0.0.1:8000/movies/recommendation'
        })
            .then(res => {
                const movies = _.sampleSize(res.data, 15)
                // console.log(movies)
                this.movieItems = movies
            })
            .catch(err => {
                console.log(err)
            })
    },
}
</script>

<style>
    #carousel {
        position: absolute;
        top: -100px;
        width: 100%;
        min-width: 768px;
    }

    #home-search-bar {
        margin-top: 580px;
    }
    
</style>