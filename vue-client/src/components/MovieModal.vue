<template>
  <div class="modal fade" data-backdrop="static" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">
            {{ selectedMovie.title }} ({{ selectedMovie.original_title }})
            <button class="cart-button" @click="toggleCart">
              <img src="@/assets/cart_add_2.svg" v-if="!cart_added" alt="cart_add" class="cart-button-icon">
              <img src="@/assets/cart_remove.png" v-if="cart_added" alt="cart_add" class="cart-button-icon">
            </button>
          </h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-sub-header">
          <div>
            {{ selectedMovie.release_date | getYear }}년 <span class="split-bar">|</span>
            <span v-if="selectedMovie.runtime">{{ selectedMovie.runtime | convertToTime }}</span> <span class="split-bar">|</span>
            <span>
              <img src="@/assets/star_empty.svg" class="detail-star-icon">
              <img src="@/assets/star_empty.svg" class="detail-star-icon">
              <img src="@/assets/star_empty.svg" class="detail-star-icon">
              <img src="@/assets/star_empty.svg" class="detail-star-icon">
              <img src="@/assets/star_empty.svg" class="detail-star-icon">
            </span>
          </div>
          <div>
            <span class="genre-button" v-for="(genre, index) in splited_genres" :key="index" 
            @click="moveToSearch(genre)" data-bs-dismiss="modal" aria-label="Close">
              {{ genre }}
            </span>
          </div>
        </div>

        <hr style="margin: 1rem; color: rgba(165, 165, 165, 0.5);">

        <div class="modal-body">
          <div id="movie-trailer-box" v-if="trailer_src">
            <iframe id="movie-trailer" :src="trailer_src" title="YouTube video player" frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen></iframe>
          </div>
          <div class="movie-info">
            <img :src="poster_path" :alt="selectedMovie.title" class="poster">
            <div v-if="selectedMovie.overview" class="movie-info-overview">
              <h6>줄거리</h6>
              <p>{{ selectedMovie.overview }}</p>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-primary" @click="moveToDetail" data-bs-dismiss="modal" aria-label="Close">
            상세정보 <img src="@/assets/arrow.png" class="arrow">
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
    name: 'MovieModal',
    data: function () {
        return {
          selectedMovie_posterpath: '',
          cart_added: false,
        }
    },
    methods: {
      moveToDetail: function () {
        this.$router.push({ name: 'MovieDetail',  params: { movie_id: this.selectedMovie.id }})
      },
      toggleCart: function () {
        // console.log(this.loginUser)
        // console.log('movie', this.selectedMovie)
        if (this.loginUser) {
          this.cart_added = !this.cart_added

          //axios
        } else {
          this.$router.push({ name: 'Login' })
        }
      },
      moveToSearch: function (genre) {
        this.$router.push({name: 'Search', params: {keyword: genre}})
        this.$store.dispatch('onSearch', genre)
      },
    },
    filters: {
      convertToTime: function (num) {
        const hour = parseInt(num / 60)
        const minute = num % 60
        return num ? `${hour}시간 ${minute}분` : ''
      },
      getYear: function (string) {
        return string ? string.slice(0,4) : ''
      }
    },
    computed: {
      ...mapState([
        'selectedMovie',
        'loginUser'
      ]),
      trailer_src: function () {
        return this.selectedMovie.trailer_key ? `https://www.youtube.com/embed/${this.selectedMovie.trailer_key}`: ''
      },
      poster_path: function () {
        return this.selectedMovie.poster_path ? `https://image.tmdb.org/t/p/original/${this.selectedMovie.poster_path}`: ''
      },
      splited_genres: function () {
        return this.selectedMovie.genres ? this.selectedMovie.genres.split(', ') : []
      },
    },
}
</script>

<style>
  .modal-header, 
  .modal-body, 
  .modal-content,
  .modal-footer {
    background-color: #262626;
    border: none;
  }

  .modal-content {
    box-shadow: 0px 0px 42px rgba(0, 0, 0, 0.75);
  }

  .modal-header,
  .modal-sub-header, 
  .modal-body, 
  .modal-footer {
    padding: 1.25rem;
  }

  .modal-header {
    padding-bottom: 0;
    text-align: left;
    align-items: start;
  }

  .modal-body {
    padding-top: 0.5rem;
    padding-bottom: 0;
  }

  .modal-sub-header {
    text-align: left;
    font-size: 0.875rem;
    padding-top: 0;
    padding-bottom: 0;
  }

  .modal-sub-header > div:first-child {
    padding-bottom: 0.5rem;
  }

  .genre-button {
    background-color: rgb(112,34,171);
    margin: 0.25rem;
    padding: 0 0.75rem;
    height: 1.75rem;
    line-height: 1.75rem;
    display: inline-block;
    border-radius: 0.875rem;
    cursor: pointer;
  }

  .genre-button:first-child {
    margin-left: 0;
  }

  .detail-star-icon {
    width: 1rem;
    height: 1rem;
    margin: 0.125rem;
  }

  .split-bar {
    margin: 0 0.25rem;
    color: rgba(165, 165, 165, 0.5);
  }

  .modal-title {
    font-family: scd6;
    font-size: 1.5rem;
  }

  .modal-dialog {
    max-width: 800px;
  }

  div.modal {
    color: white;
  }

  #movie-trailer-box {
    position: relative;
    width: 100%;
    height: 0;
    padding-top: 56.25%;
  }

  #movie-trailer {
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    width: 100%;
    height: 100%;
  }

  /* bootstrap override */
  .btn-close {
    opacity: 1;
    background: transparent url('../assets/close.svg') center/1em auto no-repeat;
  }

  .cart-button {
    background-color: transparent;
    border: none;
  }

  .cart-button-icon {
    width: 20px;
    height: 20px;
  }

  .movie-info {
    display: flex;
  }

  img.arrow {
    width: 7px;
    height: 14px;
  }

  .movie-info {
    padding-top: 1rem;
  }

  .movie-info > .poster {
    margin-right: 1rem;
  }

  .movie-info-overview {
    text-align: left;
    padding-right: 5%;
  }

  .movie-info-overview > h6 {
    text-align: left;
    font-size: 1.25rem;
    font-family: scd6;
  }

  .movie-info-overview > p {
    margin: 0;
  }

  .poster {
    height: 300px;
    width: 210px;
    object-fit: cover;
  }

</style>