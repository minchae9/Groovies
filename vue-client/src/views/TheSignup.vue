<template>
  <div id="signup">
    <!-- <img src="@/assets/logo.png" alt="logo" class="logo"> -->
    <div class="page-title">
      <div>회원가입</div> 
      <div class="line"></div>
    </div>
    <div id="signup-form">
      <div>
        <label for="username">이름:</label>
        <input type="text" id="username" @input="[checkValidUsername(), onInputUsername()]"
        :value="credentials.username"
        :class="{ red: isInvalidUsername }">
      </div>
      <div>
        <label for="id">아이디:</label>
        <input type="text" id="id" v-model="credentials.id">
        <p class="tag">사용 가능한 아이디입니다.</p>
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
          isInvalidUsername: false,
          isInvalidId: false,
          isInvalidPW: false,
          isNotSamePW: false,
        }
    },
    methods: {
      signup: function () {
        const agreed = document.querySelector('#agree').checked
        if (!this.isInvalidUsername && !this.isInvalidId && !this.isInvalidPW && !this.isNotSamePW && agreed) {
          // 회원가입 가능
          console.log(this.credentials)
          console.log('회원가입!')

        } else {
          // 회원가입 불가능
          console.log('회원가입 불가! 정보 입력을 모두 완료해주세요.')
        }
      },
      onInputUsername: function () {
        const usernameInput = document.querySelector('#username')
        this.credentials.username = usernameInput.value
        console.log(this.credentials.username)
      },
      checkValidUsername: function () {
        if (this.credentials.username.length) {
          this.isInvalidUsername = false
        } else {
          this.isInvalidUsername = true
        }
      },
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

    },
}
</script>

<style>
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