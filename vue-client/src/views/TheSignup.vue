<template>
  <div id="signup">
    <!-- <img src="@/assets/logo.png" alt="logo" class="logo"> -->
    <div class="page-title">
      <div>회원가입</div> 
      <div class="line"></div>
    </div>
    <div id="signup-form">
      <div>
        <label for="username">닉네임:</label>
        <input type="text" id="username" v-model="credentials.username" :class="{ red: checkValidUsername }">
        <p class="tag" v-if="credentials.username" v-show="!checkValidUsername">사용 가능한 닉네임입니다.</p>
        <p class="tag invalid" v-if="credentials.username" v-show="checkValidUsername">이미 사용중인 닉네임입니다.</p>
      </div>
      <div>
        <label for="id">아이디:</label>
        <input type="text" id="id" v-model="credentials.id" :class="{ red: checkValidId }">
        <p class="tag" v-if="credentials.id" v-show="!checkValidId">사용 가능한 아이디입니다.</p>
        <p class="tag invalid" v-if="credentials.id" v-show="checkValidId">이미 사용중인 아이디입니다.</p>
      </div>
      <div>
        <label for="id">비밀번호:</label>
        <input type="password" id="password" v-model="credentials.password" @input="[checkValidPW(), checkSamePW()]"
        :class="{ red: isInvalidPW }">
        <p class="tag">* 영문, 숫자를 모두 포함하여 8자리 이상</p>
      </div>
      <div>
        <label for="id">비밀번호 확인:</label>
        <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation" 
        @input="[checkValidPW(), checkSamePW()]" :class="{ red: isNotSamePW }">
      </div>
      <p class="notice" :class="{ shown: isNotSamePW }">비밀번호가 일치하지 않습니다!</p>
      <div>
        <input type="checkbox" id="agree">
        <label for="agree" style="cursor: pointer;">회원가입에 동의합니다!</label>
      </div>
      <button @click="signup">회원가입</button>
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
            username: '',
            id: '',
            password: '',
            passwordConfirmation: '',
          },
          isInvalidPW: false,
          isNotSamePW: false,
          existingId: [],
          existingUsername: [],
        }
    },
    methods: {
      signup: function () {
        const agreed = document.querySelector('#agree').checked
        if (!this.checkValidUsername && !this.checkValidId && !this.isInvalidPW && !this.isNotSamePW && agreed) {
          // 회원가입 가능
          // console.log(this.credentials)
          // console.log('회원가입!')
          axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/accounts/signup/',
            data: {
              nickname: this.credentials.username,
              username: this.credentials.id,
              password: this.credentials.password,
              passwordConfirmation: this.credentials.passwordConfirmation
            }
          })
            .then(() => {
              // console.log(res)
            })
            .catch(err => {
              console.log(err)
            })

        } else {
          // 회원가입 불가능
          console.log('회원가입 불가! 정보 입력을 모두 완료해주세요.')
        }
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
      getAllIDs: function () {
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
            this.existingId = userList
            // console.log(this.existingUsername)
          })
          .catch(err => {
            console.log(err)
          })
      },
      getAllUsernames: function () {
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
            this.existingUsername = userList
            // console.log(this.existingUsername)
          })
          .catch(err => {
            console.log(err)
          })
      },
    },
    created: function () {
      this.getAllIDs()
      this.getAllUsernames()
    },
    computed:{
      checkValidId(){
        let usedId = this.existingId.includes(this.credentials.id)
        // let apples = this.selectedProducts.includes("Apples")
        if (this.existingId.length > 0 && usedId) return true
        // if (this.selectedProducts.length === 1 && (apples || pears)) return true
        return false
      },
      checkValidUsername(){
        let usedUsername = this.existingUsername.includes(this.credentials.username)
        if (this.existingUsername.length > 0 && usedUsername) return true
        return false
      },
    },
}
</script>

<style>
  .invalid {
    color: red;
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