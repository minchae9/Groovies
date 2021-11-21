<template>
  <div class="carousel">
    <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="3" aria-label="Slide 4"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="4" aria-label="Slide 5"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active" v-if="carouselItems">
          <img :src=getPosterPath(carouselItems[0]) class="d-block w-100" alt="poster image">
          <div class="carousel-caption d-none d-md-block">
            <h5 v-if="carouselItems[0]">{{ carouselItems[0].title }}</h5>
            <p></p>
            <button @click="openModal(0)" data-bs-toggle="modal" data-bs-target="#staticBackdrop">상세정보</button>
          </div>
        </div>
        <div class="carousel-item" v-if="carouselItems">
          <img :src=getPosterPath(carouselItems[1]) class="d-block w-100" alt="poster image">
          <div class="carousel-caption d-none d-md-block">
            <h5 v-if="carouselItems[1]">{{ carouselItems[1].title }}</h5>
            <p></p>
            <button @click="openModal(1)" data-bs-toggle="modal" data-bs-target="#staticBackdrop">상세정보</button>
          </div>
        </div>
        <div class="carousel-item" v-if="carouselItems">
          <img :src=getPosterPath(carouselItems[2]) class="d-block w-100" alt="poster image">
          <div class="carousel-caption d-none d-md-block">
            <h5 v-if="carouselItems[2]">{{ carouselItems[2].title }}</h5>
            <p></p>
            <button @click="openModal(2)" data-bs-toggle="modal" data-bs-target="#staticBackdrop">상세정보</button>
          </div>
        </div>
        <div class="carousel-item" v-if="carouselItems">
          <img :src=getPosterPath(carouselItems[3]) class="d-block w-100" alt="poster image">
          <div class="carousel-caption d-none d-md-block">
            <h5 v-if="carouselItems[3]">{{ carouselItems[3].title }}</h5>
            <p></p>
            <button @click="openModal(3)" data-bs-toggle="modal" data-bs-target="#staticBackdrop">상세정보</button>
          </div>
        </div>
        <div class="carousel-item">
          <img :src=getPosterPath(carouselItems[4]) class="d-block w-100" alt="poster image">
          <div class="carousel-caption d-none d-md-block">
            <h5 v-if="carouselItems[4]">{{ carouselItems[4].title }}</h5>
            <p></p>
            <button @click="openModal(4)" data-bs-toggle="modal" data-bs-target="#staticBackdrop">상세정보</button>
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
    name: 'Carousel',
    props: {
      movieItems: Array,
    },
    data: function () {
        return {
        }
    },
    methods: {
      openModal: function (num) {
        this.$store.dispatch('getMovieDetail', this.carouselItems[num].id)
      },
      getPosterPath: function (carouselItem) {
        if (carouselItem) {
          return `https://image.tmdb.org/t/p/original/${carouselItem.poster_path}`
        } 
      }         
    },
    computed: {
      carouselItems: function () {
          return _.sampleSize(this.movieItems, 5)
      },
    },
}
</script>

<style>
  img {
    height: 700px;
    object-fit: cover;
  }
</style>