<template>
  <div id="searchBar">
      <input type="text" id="SearchInput" 
        class="search-bar"
        placeholder="검색어를 입력하세요" 
        :value="searchKeyword" @input="updateInput" 
        @keypress.enter="onSearch">
      <button @click="onSearch" class="search-button">
          <img src="@/assets/search.png" class="search-icon">
      </button>
  </div>
</template>

<script>

export default {
    name: 'SearchBar',
    data: function () {
        return {
            searchKeyword: '',
        }
    },
    methods: {
        onSearch: function () {
            console.log('onSearch!')
            if (this.searchKeyword) {
                this.$store.dispatch('onSearch', this.searchKeyword)
                if (this.$route.path !== '/search') {
                    this.$router.push({ name: 'Search' })
                }
            }
        },
        updateInput: function(event) {
            this.searchKeyword = event.target.value
        }
    },
    created: function () {
        if (this.$route.path === '/search') {
            this.searchKeyword = this.$store.state.searchKeyword
        }
    },
    
}
</script>

<style>
    .search-bar {
        width: 36rem;
        height: 3rem;
        padding: 16px;
        border-radius: 1.5rem 1rem 1rem 1.5rem;
        margin-bottom: 48px;
    }

    .search-icon {
        width: 18px;
        height: auto;
    }

    .search-button {
        position: relative;
        left: -2rem;
        border: none;
        border-radius: 50%;
        background-color: rgb(112,34,171);
        width: 3rem;
        height: 3rem;
    }

</style>