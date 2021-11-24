<template>
  <div class="modal fade" data-backdrop="static" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">

        <!-- header -->
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">
            {{ selectedMovie.title }} ({{ selectedMovie.original_title }})
    
            <!-- cart button -->
            <button @click="toggleCart" class="cart-button" :data-bs-dismiss="ratingModal" :aria-label="ratingClose">
              <img src="@/assets/cart_add_2.svg" v-if="!isAddedToCart" alt="cart_add" class="cart-button-icon">
              <img src="@/assets/cart_remove.png" v-if="isAddedToCart" alt="cart_add" class="cart-button-icon">
            </button>

          </h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>

        <!-- sub-header -->
        <div class="modal-sub-header">
          <div>
            {{ selectedMovie.release_date | getYear }}년 <span class="split-bar">|</span>
            <span v-if="selectedMovie.runtime">{{ selectedMovie.runtime | convertToTime }}</span> <span class="split-bar">|</span>
            
            <!-- average rate -->
            <span>평점 {{ selectedMovie.vote_average }}</span>
            <!-- <span class="rating" @click="rate" :data-bs-dismiss="ratingModal" :aria-label="ratingClose">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 21.07 20.23"
              v-for="(star_src, idx) in new Array(5)" :key="idx"
              class="detail-star-icon" :data-score="Number(idx)+1">
                  <defs>
                  </defs>
                  <g id="레이어_2" data-name="레이어 2">
                  <g id="레이어_1-2" data-name="레이어 1">
                  <path class="cls-1" 
                  @click="rate" :data-bs-dismiss="ratingModal" :aria-label="ratingClose" :data-score="Number(idx)+1"
                  :class="{ 'fullStar': idx < ratingScore }" 
                  d="M11.81,1.29l2,4.05a1.44,1.44,0,0,0,1.07.78l4.47.65a1.42,1.42,0,0,1,.79,2.43l-3.23,3.15a1.41,1.41,0,0,0-.41,1.26l.76,4.45a1.42,1.42,0,0,1-2.06,1.5l-4-2.1a1.42,1.42,0,0,0-1.33,0l-4,2.1a1.42,1.42,0,0,1-2.07-1.5l.77-4.45a1.47,1.47,0,0,0-.41-1.26L.93,9.2a1.43,1.43,0,0,1,.79-2.43l4.47-.65a1.44,1.44,0,0,0,1.07-.78l2-4A1.43,1.43,0,0,1,11.81,1.29Z"/></g></g>
              </svg>
            </span> -->
          </div>

          <div>
            <span class="genre-button" v-for="(genre, index) in splited_genres" :key="index" 
            @click="moveToSearch(genre)" data-bs-dismiss="modal" aria-label="Close">
              {{ genre }}
            </span>
          </div>
        </div>

        <hr style="margin: 1rem; color: rgba(165, 165, 165, 0.5);">
        
        <!-- body -->
        <div class="modal-body">
          <div id="movie-trailer-box" v-if="trailer_src">
            <iframe id="movie-trailer" :src="trailer_src" title="YouTube video player" frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen></iframe>
          </div>
          <div class="movie-info"> 
            <div class="movie-info-left">
              <img :src="poster_path" :alt="selectedMovie.title" class="poster">
              <div class="staffs">
                <div>
                  <span class="movie-info-left-title">감독</span> <span class="split-bar">|</span> {{ directors | getNames }}
                </div>
                <div>
                  <span class="movie-info-left-title">배우</span> <span class="split-bar">|</span> {{ actors | getNames }}
                </div>
              </div>
            </div>
            <div v-if="selectedMovie.overview" class="movie-info-overview">
              <h6>줄거리</h6>
              <p>{{ selectedMovie.overview }}</p>
            </div>
          </div>
          <button id="close-button-bottom" type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>

        <!-- footer -->
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
import axios from 'axios'
import { mapState } from 'vuex'

export default {
    name: 'MovieModal',
    data: function () {
        return {
          isAddedToCart: false,
          myCart: [],
          ratingModal: '',
          ratingClose: '',
          ratingScore: 0,
          directors: [],
          actors: [],
        }
    },
    methods: {
      moveToDetail: function () {
        this.$router.push({ name: 'MovieDetail',  params: { movie_id: this.selectedMovie.id }})
      },
      setToken: function () {
        const token = localStorage.getItem('jwt')
        const config = {
          Authorization: `JWT ${token}`
        }
        return config
      },
      toggleCart: function () {
        if (this.loginUser && this.loginUser.user_id) {
          // 로그인한 사용자면
          axios({
            method: 'post',
            url: `http://127.0.0.1:8000/movies/${this.selectedMovie.id}/cart/`,
            headers: this.setToken()
          })
          .then(() => {
            this.updateCartState()
          })
          .catch(err => {
            console.log(err)
          })
        } else {
          this.$router.push({ name: 'Login' })
        }
      },
      rate: function (event) {
        if (this.loginUser && this.loginUser.user_id) {
          // 로그인된 상태면
          const targetScore = event.target.dataset.score

          if (targetScore) {
            // 별 눌렀을 때 (빈공간x)
            if (this.ratingScore > 0) {
              // 이미 줬던 점수가 있으면 -> 수정 (put)
                axios({
                  method: 'put',
                  url: `http://127.0.0.1:8000/movies/${this.selectedMovie.id}/rating/`,
                  headers: this.setToken(),
                  data: { rate : targetScore },
                })
                .then(() => {
                  this.updateRatingState()
                })
                .catch(err => {
                  console.log(err)
                })
  
            } else {
              // 준 점수가 없으면 -> 새로 등록 (post)
              axios({
                method: 'post',
                url: `http://127.0.0.1:8000/movies/${this.selectedMovie.id}/rating/`,
                headers: this.setToken(),
                data: { rate : targetScore },
              })
              .then(() => {
                this.updateRatingState()
              })
              .catch(err => {
                console.log(err)
              })
            }
          }

        } else {
          // 로그인을 안했으면
          this.$router.push({ name: 'Login' })
        }
      },
      moveToSearch: function (genre) {
        this.$router.push({name: 'Search', params: {keyword: genre}})
        this.$store.dispatch('onSearch', genre)
      },
      updateCartState: function () {
        // cart data
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/accounts/mycart/`,
          headers: this.setToken()
        })
        .then((res) => {
          this.myCart = res.status === 204? [] : res.data
          this.isAddedToCart =  this.myCart.map(item => item.id).includes(this.selectedMovie.id) ? true : false
        })
        .catch(err => {
          console.log(err)
        })
      },
      updateRatingState: function () {
        // cart data
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/movies/${this.selectedMovie.id}/rating/`,
          headers: this.setToken()
        })
        .then((res) => {
          this.ratingScore = ((res.status >= 200 && res.status <= 202) && res.data.rate) ? res.data.rate : 0
        })
        .then(() => {
          const stars = document.querySelectorAll('.detail-star-icon')
          stars.forEach((item, idx) => {
            if (idx < this.ratingScore) {
              item.classList.add('fullStar')
            } else {
              item.classList.remove('fullStar')
            }
          })
        })
        .catch(err => {
          if (err.response.status === 404) {
            this.ratingScore = 0
          } else {
            console.log(err)
          }
        })
      },
      updateLoginState: function () {
        if (this.loginUser && this.loginUser.user_id) {
          //ratings 버튼
          this.ratingModal = ''
          this.ratingClose = ''
        } else {
          //ratings 버튼
          this.ratingModal = 'modal'
          this.ratingClose = 'Close'
        }
      },
      updateStates: function () {
        this.updateLoginState(this.loginUser)

        // 로그인한 경우만 로그인 정보 업데이트
        if (this.loginUser && this.loginUser.user_id) {
          this.updateCartState()
          this.updateRatingState()
        }
      },
      getDirectors: function () {
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/movies/${this.selectedMovie.id}/director/`,
        })
        .then((res) => {
          this.directors = res.data
        })
        .catch(err => {
          console.log(err)
        })
      },
      getActors: function () {
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/movies/${this.selectedMovie.id}/actor/`,
        })
        .then((res) => {
          this.actors = res.data
        })
        .catch(err => {
          console.log(err)
        })
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
      },
      getNames: function (arr) {
        return arr.map(person => person.name).join(', ')
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
    watch: {
      loginUser: function () {
        this.updateStates()
      },
      selectedMovie: function () {
        this.updateStates()

        this.getDirectors()
        this.getActors()
      },
    },
    created: function () {
      if (this.selectedMovie.id) {
        this.updateStates()
      }
    }
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
  .modal-footer,
  .detail-header,
  .detail-sub-header, 
  .detail-body {
    padding: 32px;
  }

  .modal-header,
  .detail-header {
    padding-bottom: 0;
    text-align: left;
    align-items: start;
  }

  .modal-body,
  .detail-body {
    padding-top: 0.5rem;
    padding-bottom: 0;
  }

  .modal-sub-header,
  .detail-sub-header {
    text-align: left;
    font-size: 0.875rem;
    padding-top: 0;
    padding-bottom: 0;
  }

  .modal-sub-header > div:first-child,
  .detail-sub-header > div:first-child {
    padding-bottom: 0.5rem;
  }

  .rating {
    cursor: pointer;
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

  .modal-title,
  .detail-title {
    font-family: scd6;
    font-size: 1.5rem;
    word-break: keep-all;
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

  .movie-info .poster {
    margin-right: 1rem;
    margin-bottom: 1rem;
  }

  .movie-info-left {
    text-align: left;
    font-size: 0.875rem;
  }

  .movie-info-left-title {
    font-family: scd6;
  }

  .movie-info-overview {
    text-align: justify;
    padding-right: 10%;
    word-break: break-all;
  }

  .movie-info-overview > h6 {
    text-align: left;
    font-size: 1.25rem;
    font-family: scd6;
  }

  .movie-info-overview > p {
    margin: 0;
  }

  .staffs {
    margin-right: 1rem;
  }

  .modal-body .staffs {
    width: 210px;
  }

  .poster {
    height: 300px;
    width: 210px;
    object-fit: cover;
  }

  .item > div {
    width: 138px;
    word-break: keep-all;
    text-align: left;
  }

  #close-button-bottom {
    position: absolute;
    bottom: -2rem;
    right: 0.5rem;
    padding: 2rem;
    padding-bottom: 0;
  }

  /* star */
  .cls-1{fill:none;stroke:#fbb03b;stroke-linecap:round;stroke-miterlimit:10;}
  .fullStar {
          fill: #fbb03b;
      }

</style>
