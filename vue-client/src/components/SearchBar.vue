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
            // console.log('onSearch! method', this.searchKeyword)

            if (this.searchKeyword) {
                this.$router.push({ name: 'Search', params: { keyword : this.searchKeyword }})
                .then(() => {
                    const searchInput = document.querySelector('#SearchInput')
                    searchInput.blur()
                })
                .catch(()=>{})
            }
        },
        updateInput: function(event) {
            this.searchKeyword = event.target.value
        }
    },
    created: function () {
        console.log('created searchbar')
        if (/^\/search\//.test(this.$route.path)) {
            // console.log('if created')
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