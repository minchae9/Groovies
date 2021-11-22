<template>
  <div>
    <carousel id="carousel" :carouselItems="carousel_items"></carousel>
    <search-bar id="home-search-bar"></search-bar>
    <movie-list :movieItems="recommendations"></movie-list>
  </div>
</template>

<script>
import Carousel from '../components/Carousel.vue'
import SearchBar from '../components/SearchBar.vue'
import MovieList from '../components/MovieList.vue'
import axios from 'axios'
// import _ from 'lodash'

export default {
    components: { 
        Carousel, 
        SearchBar, 
        MovieList, 
    },
    name: 'Home',
    data: function () {
        return {
            recommendations: [],
            carousel_items: [
                {
                    id: 0,
                    title: '',
                    tagline: '',
                    release_date: '',
                    poster_path: '',
                },
                {
                    id: 1,
                    title: '',
                    tagline: '',
                    release_date: '',
                    poster_path: '',
                },
                {
                    id: 2,
                    title: '',
                    tagline: '',
                    release_date: '',
                    poster_path: '',
                },
                {
                    id: 3,
                    title: '',
                    tagline: '',
                    release_date: '',
                    poster_path: '',
                },
                {
                    id: 4,
                    title: '',
                    tagline: '',
                    release_date: '',
                    poster_path: '',
                },
            ],
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
                // console.log(res)
                this.recommendations = res.data.recommendations
                this.carousel_items = res.data.carousel_items
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