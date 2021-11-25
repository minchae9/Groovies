<template>
  <div id="login">
    <div class="page-title">
      <h1>로그인</h1> 
      <div class="line"></div>
    </div>
    <div id="login-form">
      <div>
        <label for="username">아이디:</label>
        <input type="text" id="username" v-model="credentials.username">
      </div>
      <div>
        <label for="password">비밀번호:</label>
        <input type="password" id="password" v-model="credentials.password"
          @keypress.enter="login(credentials)">
      </div>
      <div v-if="error_message">
        <span id="error-message">{{ error_message }}</span>
      </div>
      <button @click="login(credentials)">로그인</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
    name: 'Login',
    data: function () {
        return {
          credentials: {
            username: '',
            password: '',
          },
          error_message: '',
        }
    },
    methods: {
      login: function () {
        axios.post(`${SERVER_URL}/accounts/api-token-auth/`, this.credentials)
          .then((res) => {
            // 토큰을 로컬 저장소에 저장하기
            localStorage.setItem('jwt', res.data.token)
            
            this.$emit('getUserBasics')
            this.$store.dispatch('login')
            this.$router.push({ name: 'Home' })
          })
          .catch(() => {
            this.error_message = "로그인 정보가 틀렸습니다."
            this.credentials.password = ''
          })
      }
    },
}
</script>

<style>
  #error-message {
    color: red;
  }
</style>
