<template>
    <div class="movieListWrapper">
        <movie-modal></movie-modal>
        <div class="movieList">
            <movie-item v-for="(movieItem, index) in this.movieItems" :key="index" :movieItem="movieItem">
            </movie-item>
        </div>
    </div>
</template>

<script>
import MovieModal from '@/components/MovieModal.vue'
import MovieItem from './MovieListItem.vue'

export default {
    name: 'MovieList',
    components: { MovieModal, MovieItem },
    props: {
        movieItems: Array,
    },
    data: function () {
        return {
        }
    },
}
</script>

<style>
    .movieList {
        padding: 0;
        max-width: 1200px;
        margin: 0 auto;
        /* text-align: left; */

        /* overflow: auto; */
    }

    /* .movieList::after {
        content: "";
        flex: auto;
    } */

</style>