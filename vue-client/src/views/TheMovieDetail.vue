<template>
  <div id="movieDetail">
    <!-- header -->
    <div class="detail-header">
      <h5 class="detail-title" id="exampleModalLabel">
        {{ selectedMovie.title }} ({{ selectedMovie.original_title }})

        <!-- cart button -->
        <button @click="toggleCart" class="cart-button">
          <img src="@/assets/cart_add_2.svg" v-if="!isAddedToCart" alt="cart_add" class="cart-button-icon">
          <img src="@/assets/cart_remove.png" v-if="isAddedToCart" alt="cart_add" class="cart-button-icon">
        </button>

      </h5>
    </div>

    <!-- sub-header -->
    <div class="detail-sub-header">
      <div>
        {{ selectedMovie.release_date | getDate }} <span class="split-bar">|</span>
        <span v-if="selectedMovie.runtime">{{ selectedMovie.runtime | convertToTime }}</span> <span class="split-bar">|</span>
        <span v-if="selectedMovie.vote_average">평점 <span style="font-family:scd5;">{{ selectedMovie.vote_average }}</span></span> <span class="split-bar">|</span>
        
        <!-- rating -->
        <span class="rating" @click="rate">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 21.07 20.23"
          v-for="(star_src, idx) in new Array(5)" :key="idx"
          class="detail-star-icon" :data-score="Number(idx)+1">
              <defs>
              </defs>
              <g id="레이어_2" data-name="레이어 2">
              <g id="레이어_1-2" data-name="레이어 1">
              <path class="cls-1" 
              @click="rate" :data-score="Number(idx)+1"
              :class="{ 'fullStar': idx < ratingScore }" 
              d="M11.81,1.29l2,4.05a1.44,1.44,0,0,0,1.07.78l4.47.65a1.42,1.42,0,0,1,.79,2.43l-3.23,3.15a1.41,1.41,0,0,0-.41,1.26l.76,4.45a1.42,1.42,0,0,1-2.06,1.5l-4-2.1a1.42,1.42,0,0,0-1.33,0l-4,2.1a1.42,1.42,0,0,1-2.07-1.5l.77-4.45a1.47,1.47,0,0,0-.41-1.26L.93,9.2a1.43,1.43,0,0,1,.79-2.43l4.47-.65a1.44,1.44,0,0,0,1.07-.78l2-4A1.43,1.43,0,0,1,11.81,1.29Z"/></g></g>
          </svg>
        </span>
      </div>

      <div>
        <span class="genre-button" v-for="(genre, index) in splited_genres" :key="index" 
        @click="moveToSearch(genre)">
          {{ genre }}
        </span>
      </div>
    </div>

    <hr style="margin: 32px; color: rgba(165, 165, 165, 0.5);">
    
    <!-- body -->
    <div id="detail-body">

      <div id="detail-body-left">
        <div id="movie-trailer-box" v-if="trailer_src">
          <iframe id="movie-trailer" :src="trailer_src" title="YouTube video player" frameborder="0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
          allowfullscreen></iframe>
        </div>
        <div id="movie-info">
          <img :src="poster_path" :alt="selectedMovie.title" class="poster">
          <div v-if="selectedMovie.overview" class="movie-info-overview">
            <h6>줄거리</h6>
            <p>{{ selectedMovie.overview }}</p>
          </div>
        </div>
      </div>

      <div id="detail-body-right">
        <div v-if="selectedMovie.Director.length">
          <h6>감독</h6> 
          <div class="staffs">
            <div v-for="(director, idx) in selectedMovie.Director" :key="idx" class="item">
              <img :src="getImgSrc(director.profile_path)" alt="director_profile_img">
              <div>{{ director.name }}</div>
            </div>
          </div>
        </div>
        <div v-if="selectedMovie.Actor.length">
          <h6>배우</h6> 
          <div class="staffs">
            <div v-for="(actor, idx) in selectedMovie.Actor" :key="idx" class="item">
              <img :src="getImgSrc(actor.profile_path)" alt="actor_profile_img">
              <div><span class="role">{{ actor.character }}</span> <span style="font-size: 0.875rem;">역</span></div>
              <div>{{ actor.name }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>

      <div id="detail-body-similar" v-if="selectedMovie.Similar.length">
        <h6>이 영화와 비슷한 영화들</h6>
        <div id="similar-movie-list">
          <div v-for="(similar, idx) in selectedMovie.Similar" :key="idx" class="item">
            <img :src="getImgSrc(similar.poster_path)" alt="similar_movie_poster">
            <div>{{ similar.title }}</div>
          </div>
        </div>
      </div>

  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

export default {
    name: 'MovieDetail',
    data: function () {
        return {
          movie_id: this.$route.params.movie_id,
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
      getImgSrc: function (key) {
        return key ? `https://www.themoviedb.org/t/p/w138_and_h175_face/${key}` : require('@/assets/default_profile_img.jpg')
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
    },
    filters: {
      convertToTime: function (num) {
        const hour = parseInt(num / 60)
        const minute = num % 60
        return num ? `${hour}시간 ${minute}분` : ''
      },
      getDate: function (string) {
        return string ? string.replace(/-/g, '.') : ''
      },
      getNames: function (arr) {
        return arr.map(person => person.name).join(', ')
      },
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
      },
    },
    created: function () {
      if (this.selectedMovie.id) {
        this.updateStates()
      } else {
        if (this.selectedMovie.id !== this.movie_id) {
          this.$store.dispatch('getMovieDetail', this.movie_id)
        }
      }
    },
    // watch: {
    //   selectedMovie: function () {
    //     const targetMovieId = this.$route.params.movie_id
    //     if (this.selectedMovie.id !== targetMovieId) {
    //       this.$store.dispatch('getMovieDetail', targetMovieId)
    //     }
    //   }
    // }
}
</script>

<style>
    #detail-body {
    padding: 32px;
    padding-top: 0;
  }

  #detail-body-left {
    width: 60%;
    margin-right: 32px;
  }

  #detail-body-right {
    text-align: left;
    padding-left: 32px;
    border-left: 1px solid rgba(165, 165, 165, 0.1);
  }

  #detail-body-right > div {
    margin-bottom: 32px;
  }

  #detail-body .staffs {
    display: flex;
  }

  .staff-title {
    font-family: scd6;
    font-size: 1.25rem;
    margin-bottom: 0.5rem;
  }

  .role {
    font-family: scd6;
  }

  #detail-body,
  #movie-info {
    display: flex;
  }

  #movie-info {
    margin: 1rem;
    margin-left: 0;
  }

  #movie-info .poster {
    margin-right: 1rem;
  }

  #detail-body-similar {
    padding: 32px;
    text-align: justify;
  }

  #similar-movie-list {
    display: flex;
  }

  #detail-body-right h6,
  #detail-body-similar h6 {
    text-align: left;
    font-size: 1.25rem;
    font-family: scd6;
  }

  #detail-body-right img,
  #detail-body-similar img {
    margin-right: 1rem;
    margin-bottom: 0.5rem;
    width: 138px;
    height: 175px;
    object-fit: cover;
  }

</style>