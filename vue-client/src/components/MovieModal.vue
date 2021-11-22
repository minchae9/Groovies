<template>
  <div class="modal fade" data-backdrop="static" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">
            {{ selectedMovie.title }} ({{ selectedMovie.original_title }})
            <button class="cart-button" @click="toggleCart">
              <img src="@/assets/cart_add_2.svg" alt="cart_add" class="cart-button-icon">
            </button>
          </h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <h1>{{ selectedMovie.id }}</h1>
          <div>
            {{ selectedMovie.runtime | convertToTime }}
          </div>
          <div>({{ selectedMovie.release_date | getYear }})</div>
          <div>{{ selectedMovie.genres }}</div>
          <iframe :src="trailer_src" title="YouTube video player" frameborder="0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
          allowfullscreen></iframe>
          <div class="movie-info">
            <img :src="poster_path" :alt="selectedMovie.title" class="poster">
            <div v-if="selectedMovie.overview">
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
        }
    },
    methods: {
      moveToDetail: function () {
        this.$router.push({ name: 'MovieDetail',  params: { movie_id: this.selectedMovie.id }})
      },
      toggleCart: function () {
        
      }
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
        'selectedMovie'
      ]),
      trailer_src: function () {
        return this.selectedMovie.trailer_key ? `https://www.youtube.com/embed/${this.selectedMovie.trailer_key}`: ''
      },
      poster_path: function () {
        return this.selectedMovie.poster_path ? `https://image.tmdb.org/t/p/original/${this.selectedMovie.poster_path}`: ''
      }
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

  .modal-dialog {
    max-width: 800px;
  }

  div.modal {
    color: white;
  }

  .btn-close {
    color: #fff; 
    opacity: 1;
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

  .poster {
    height: 300px;
    width: 210px;
    object-fit: cover;
  }

</style>