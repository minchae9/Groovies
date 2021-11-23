<template>
  <div>
      profile: {{ this.$route.params.user_id }}
      <button @click="updateProfile">회원정보 수정</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'UserProfile',
    data: function () {
      return {
        user_id: this.$route.params.user_id,
        username: '',
        nickname: '',
      }
    },
    created: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/profile/${this.user_id}/`
      })
        .then(res => {
          // console.log(res)
          this.username = res.data.username
          this.nickname = res.data.nickname
        })
        .catch(err => {
          console.log(err)
        })
    },
    methods: {
      updateProfile: function () {
        this.$router.push({ name: 'Signup' })
        this.$router.go()
      },
    },
}
</script>

<style>

</style>