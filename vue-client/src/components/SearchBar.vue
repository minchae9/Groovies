<template>
  <div id="searchBar">
      <input type="text" id="SearchInput" 
        class="search-bar"
        placeholder="검색어를 입력하십시오" 
        :value="searchKeyword" @input="updateInput" 
        @keypress.enter="onSearch(searchKeyword)">
      <button @click="onSearch(searchKeyword)" class="search-button">
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
        onSearch: function (searchKeyword) {
            // console.log('onSearch!')
            if (searchKeyword) {
                this.$store.dispatch('onSearch', searchKeyword)
                if (this.$route.path !== '/search') {
                    this.$router.push({ name: 'Search' })
                }
            }
        },
        updateInput: function(event) {
            this.searchKeyword = event.target.value
        },
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