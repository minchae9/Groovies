<template>
  <div id="signup">
    <div class="page-title">
      <div v-if="this.$store.state.loginUser">회원 정보 수정</div> 
      <div v-else>회원가입</div> 
      <div class="line"></div>
    </div>
    <div id="signup-form">
      <div>
        <p>프로필 사진</p>
        <br>
        <a href="#"><img :class="{ click: credentials.profile_path === 0 }" @click="setProfilePath(0)" src="@/assets/profile_img_0.jpg" alt="0번_프로필" class="profile"></a>
        <a href="#"><img :class="{ click: credentials.profile_path === 1 }" @click="setProfilePath(1)" src="@/assets/profile_img_1.jpg" alt="1번_프로필" class="profile"></a>
        <a href="#"><img :class="{ click: credentials.profile_path === 2 }" @click="setProfilePath(2)" src="@/assets/profile_img_2.jpg" alt="2번_프로필" class="profile"></a>
        <a href="#"><img :class="{ click: credentials.profile_path === 3 }" @click="setProfilePath(3)" src="@/assets/profile_img_3.jpg" alt="3번_프로필" class="profile"></a>
        <a href="#"><img :class="{ click: credentials.profile_path === 4 }" @click="setProfilePath(4)" src="@/assets/profile_img_4.jpg" alt="4번_프로필" class="profile"></a>
      </div>
      <br>
      <br>
      <div>
        <label for="nickname">닉네임:</label>
        <input v-if="this.$store.state.loginUser" type="text" id="nickname" v-model="credentials.nickname" :class="{ red: checkValidNickname }" :placeholder="this.$store.state.loginUser_nickname">
        <input v-else type="text" id="nickname" v-model="credentials.nickname" :class="{ red: checkValidNickname }">
        <p class="tag" v-if="credentials.nickname" v-show="!checkValidNickname">사용 가능한 닉네임입니다.</p>
        <p class="tag invalid" v-if="credentials.nickname" v-show="checkValidNickname">이미 사용중인 닉네임입니다.</p>
      </div>
      <div>
        <label for="username">아이디:</label>
        <input v-if="this.$store.state.loginUser" type="text" id="username" :value="this.$store.state.loginUser.username" :class="{ red: checkValidUsername }" readonly>
        <input v-else type="text" id="username" v-model="credentials.username" :class="{ red: checkValidUsername }">
        <p class="tag" v-if="credentials.username" v-show="!checkValidUsername">사용 가능한 아이디입니다.</p>
        <p class="tag invalid" v-if="credentials.username" v-show="checkValidUsername">이미 사용중인 아이디입니다.</p>
      </div>
      <div>
        <label for="password">비밀번호:</label>
        <input type="password" id="password" v-model="credentials.password" @input="[checkValidPW(), checkSamePW()]"
        :class="{ red: isInvalidPW }">
        <p class="tag">* 영문, 숫자를 모두 포함하여 8자리 이상</p>
      </div>
      <div>
        <label for="passwordConfirmation">비밀번호 확인:</label>
        <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation" 
        @input="[checkValidPW(), checkSamePW()]" :class="{ red: isNotSamePW }">
      </div>
      <p class="notice" :class="{ shown: isNotSamePW }">비밀번호가 일치하지 않습니다!</p>
      <div v-if="!this.$store.state.loginUser">
        <input type="checkbox" id="agree">
        <label for="agree" style="cursor: pointer;">회원가입에 동의합니다!</label>
      </div>
      <button v-if="this.$store.state.loginUser !== null" @click="update">회원정보 수정</button>
      <button v-else @click="signup">회원가입</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Signup',
    data: function () {
        return {
          credentials: {
            nickname: '',
            username: '',
            password: '',
            passwordConfirmation: '',
            profile_path: null,
          },
          isInvalidPW: false,
          isNotSamePW: false,
          existingUsername: [],
          existingNickname: [],
        }
    },
    methods: {
      signup: function () {
        const agreed = document.querySelector('#agree').checked
        if (!this.checkValidUsername && !this.checkValidNickname && !this.isInvalidPW && !this.isNotSamePW && agreed) {
          // 회원가입 가능
          // console.log(this.credentials)
          // console.log('회원가입!')
          axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/accounts/signup/',
            data: {
              profile_path: this.credentials.profile_path,
              nickname: this.credentials.nickname,
              username: this.credentials.username,
              password: this.credentials.password,
              passwordConfirmation: this.credentials.passwordConfirmation
            }
          })
            .then(() => {
              this.$router.push({ name: 'Login' })
            })
            .catch(() => {
              this.$router.go()
            })

        } else {
          // 회원가입 불가능
          console.log('회원가입 불가! 정보 입력을 모두 완료해주세요.')
        }
      },
      // 프로필 사진
      setProfilePath (num) {
        this.credentials.profile_path = num
        this.clickedImg = num
        console.log(this.credentials.profile_path)
      },
      // 비밀번호
      checkValidPW: function () {
        if (this.credentials.password.length) {
          if (/^(?=.*[a-zA-Z])(?=.*[0-9]).{8,}$/.test(this.credentials.password)) {
            this.isInvalidPW = false
          } else {
            this.isInvalidPW = true
          }
        } else {
          this.isInvalidPW = false
        }
      },
      checkSamePW: function () {
        if (this.credentials.passwordConfirmation.length) {
          if (this.credentials.password !== this.credentials.passwordConfirmation) {
            this.isNotSamePW = true
          } else {
            this.isNotSamePW = false
          }
        } else {
          this.isNotSamePW = false
        }
      },
      getAllUsername: function () {
        //axios
        axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/accounts/profile/'
        })
          .then(res => {
            // console.log(res)
            const userList = []
            for (let i=0; i < res.data.length ; i++) {
              userList.push(res.data[i].username)
            }
            this.existingUsername = userList
          })
          .catch(err => {
            console.log(err)
          })
      },
      getAllNickname: function () {
        //axios
        axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/accounts/profile/'
        })
          .then(res => {
            // console.log(res)
            const userList = []
            for (let i=0; i < res.data.length ; i++) {
              userList.push(res.data[i].nickname)
            }
            this.existingNickname = userList
          })
          .catch(err => {
            console.log(err)
          })
      },
      update: function () {
        //axios
        if (this.credentials.nickname !== '') {
          axios({
            method: 'put',
            url: `http://127.0.0.1:8000/accounts/profile/${this.$store.state.loginUser.user_id}/update/`,
            headers: { Authorization: `JWT ${localStorage.getItem('jwt')}` },
            data: {
              profile_path: this.credentials.profile_path,
              nickname: this.credentials.nickname,
              password: this.credentials.password,
              passwordConfirmation: this.credentials.passwordConfirmation
            }
          })
            .then(() => {
              this.$router.push({ name: 'UserProfile', params: { user_id: this.$store.state.loginUser.user_id }})
            })
            .catch(err => {
              console.log(err)
            })
        } else {
          axios({
            method: 'put',
            url: `http://127.0.0.1:8000/accounts/profile/${this.$store.state.loginUser.user_id}/update/`,
            headers: { Authorization: `JWT ${localStorage.getItem('jwt')}` },
            data: {
              profile_path: this.credentials.profile_path,
              nickname: this.$store.state.loginUser_nickname,
              password: this.credentials.password,
              passwordConfirmation: this.credentials.passwordConfirmation
            }
          })
            .then(() => {
              this.$router.push({ name: 'UserProfile', params: { user_id: this.$store.state.loginUser.user_id }})
            })
            .catch(err => {
              console.log(err)
            })
        }
        
      },
    },
    created: function () {
      this.getAllUsername()
      this.getAllNickname()
      this.credentials.profile_path = this.$store.state.loginUser_profile_path
    },
    computed:{
      checkValidUsername(){
        if (this.credentials.username.length > 0) {
          let usedUsername = this.existingUsername.includes(this.credentials.username)
        // let apples = this.selectedProducts.includes("Apples")
        if (this.existingUsername.length > 0 && usedUsername) return true
        // if (this.selectedProducts.length === 1 && (apples || pears)) return true
        return false
        } else {
          return false
        }
      },
      checkValidNickname(){
        if (this.credentials.nickname.length > 0) {
          let usedNickname = this.existingNickname.includes(this.credentials.nickname)
          if (this.existingNickname.length > 0 && usedNickname) return true
          return false
        } else {
          return false
        }
        
      },
    },
}
</script>

<style>
  .invalid {
    color: red;
  }

  .click {
    box-shadow: 0 0 0 0.9rem rgb(112,34,171, 0.5);
  }

  .profile {
    width: 120px;
    height: 120px;
    object-fit: cover;
    border-radius: 50%;
    margin-right: 2rem;
  }

  .page-title {
    font-family: scd6;
    font-size: 1.75rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 192px 0 64px 0;
  }

  .line {
    height: 2px;
    width: 192px;
    background-color: white;
    margin-top: 12px;
  }

  .tag {
    font-size: 0.75rem;
    display: inline-block;
  }

  .notice {
    font-size: 0.75rem;
    display: none;
  }

  .shown {
    display: block;
  }

  input.red {
    border: none;
    background-color: rgb(255, 139, 139);
  }
</style>