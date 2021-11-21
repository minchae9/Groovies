<template>
  <div id="app">
    <div id="nav">
      <div>
        <router-link :to="{ name: 'Home' }"><img src="@/assets/logo.png" alt="logo" class="mainlogo"></router-link> |
        <router-link :to="{ name: 'Search' }">영화 검색</router-link> |
        <router-link :to="{ name: 'Community' }">커뮤니티</router-link>
      </div>
      <div>
        <router-link :to="{ name: 'Signup' }">회원가입</router-link> |
        <router-link :to="{ name: 'Login' }">로그인</router-link>
      </div>
    </div>
    <router-view id="content" />
    <div id="footer"></div>
  </div>
</template>

<script>
  export default {
    watch: {
          $route (to, from){
              if (!(to.name ==='Search' && from.name === 'Home')) {
                this.$store.dispatch('resetSearchKeyword')
              }
          }
      }
  }
</script>


<style>
@font-face {
     font-family: 'scd8';
     src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-8Heavy.woff') format('woff');
     font-weight: normal;
     font-style: normal;
}

@font-face {
     font-family: 'scd6';
     src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-6Bold.woff') format('woff');
     font-weight: normal;
     font-style: normal;
}

@font-face {
     font-family: 'scd3';
     src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-3Light.woff') format('woff');
     font-weight: normal;
     font-style: normal;
}

.logo {
  width: 224px;
  height: 61px;
  margin: 80px;
}

.mainlogo {
  width: 168px;
  height: 45px;
}

body {
  background-color: #262626;
}

#app {
  font-family: scd3, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;

  display: flex;
  flex-direction: column;
  min-height: 100vh;
  min-width: 768px;
}

#nav {
  box-sizing: border-box;
  display: flex;
  justify-content: space-between;
  position: absolute;
  top: 0;
  width: 100%;
  min-width: 768px;
  padding-bottom: 30px;
  padding: 30px;
  z-index: 100;
  color: white;
  text-decoration: none;

}

#nav > div {
  display: flex;
  align-items: center;
}

#nav a {
  color: white;
  text-decoration: none;
  display: inline-block;
  margin: 0 1rem;
}

#nav a.router-link-exact-active {
  font-weight: bold;
}

#content {
  margin-top: 100px;
  margin-bottom: 48px;
}

#footer {
  height: 12px;
  width: 100%;
  margin-top: 64px;

  margin-top: auto;

  background : -moz-linear-gradient(87.91% -1117.2% -150deg,rgba(43, 156, 215, 1) 0%,rgba(70, 109, 198, 1) 34.74%,rgba(100, 55, 179, 1) 78.25%,rgba(112, 34, 171, 1) 99.44%);
  background : -webkit-linear-gradient(-150deg, rgba(43, 156, 215, 1) 0%, rgba(70, 109, 198, 1) 34.74%, rgba(100, 55, 179, 1) 78.25%, rgba(112, 34, 171, 1) 99.44%);
  background : -webkit-gradient(linear,87.91% -1117.2% ,12.09% 1217.2% ,color-stop(0,rgba(43, 156, 215, 1) ),color-stop(0.3474,rgba(70, 109, 198, 1) ),color-stop(0.7825,rgba(100, 55, 179, 1) ),color-stop(0.9944,rgba(112, 34, 171, 1) ));
  background : -o-linear-gradient(-150deg, rgba(43, 156, 215, 1) 0%, rgba(70, 109, 198, 1) 34.74%, rgba(100, 55, 179, 1) 78.25%, rgba(112, 34, 171, 1) 99.44%);
  background : -ms-linear-gradient(-150deg, rgba(43, 156, 215, 1) 0%, rgba(70, 109, 198, 1) 34.74%, rgba(100, 55, 179, 1) 78.25%, rgba(112, 34, 171, 1) 99.44%);
  -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorstr='#2B9CD7', endColorstr='#7022AB' ,GradientType=0)";
  background : linear-gradient(240deg, rgba(43, 156, 215, 1) 0%, rgba(70, 109, 198, 1) 34.74%, rgba(100, 55, 179, 1) 78.25%, rgba(112, 34, 171, 1) 99.44%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#2B9CD7',endColorstr='#7022AB' , GradientType=1);
}
</style>
