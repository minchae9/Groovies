<template>
  <div id="login">
    <div class="page-title">
      <div>로그인</div> 
      <div class="line"></div>
    </div>
    <div id="login-form">
      <div>
        <label for="username">아이디:</label>
        <input type="text" id="username" v-model="credentials.username">
      </div>
      <div>
        <label for="id">비밀번호:</label>
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

export default {
    name: 'Login',
    data: function () {
        return {
          credentials: {
            username: '',
            password: '',
          },
          token: null,
          error_message: '',
        }
    },
    methods: {
      login: function () {
        // axios 요청 보내기
        axios.post(`http://127.0.0.1:8000/accounts/api-token-auth/`, this.credentials)
          .then((res) => {
            // console.log(res)
            // 토큰을 로컬 저장소에 저장하기
            localStorage.setItem('jwt', res.data.token)
            this.token = res.data.token
            
            // 유저 정보 추출
            const JWTtoken = this.token
            var base64Payload = JWTtoken.split('.')[1]; //value 0 -> header, 1 -> payload, 2 -> VERIFY SIGNATURE 
            var payload = Buffer.from(base64Payload, 'base64'); 
            var result = JSON.parse(payload.toString()) 
            // console.log(result);
            this.$emit('getUserInfo', result)

            // App.vue에 로그인됐음을 알림
            this.$emit('login')
            this.$router.push({ name: 'Home' })
          })
          .catch(() => {
            // console.log(err)
            this.error_message = "로그인 정보가 틀렸습니다."
          })
        // 유저 정보(아이디 정보)
        


      }
    },
}
</script>

<style>
  #error-message {
    color: red;
  }
</style>