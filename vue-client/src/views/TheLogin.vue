<template>
  <div id="login">
    <div class="page-title">
      <div>로그인</div> 
      <div class="line"></div>
    </div>
    <div id="login-form">
      <div>
        <label for="id">아이디:</label>
        <input type="text" id="id" v-model="credentials.id">
      </div>
      <div>
        <label for="id">비밀번호:</label>
        <input type="password" id="password" v-model="credentials.password">
      </div>
      <button @click="login">로그인</button>
    </div>
  </div>
</template>

<script>
export default {
    name: 'Login',
    data: function () {
        return {
          credentials: {
            id: '',
            password: '',
          }
        }
    },
    methods: {
      login: function () {
        
      }
    },
}
</script>

<style>

</style>