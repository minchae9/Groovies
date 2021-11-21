<template>
  <div class="carousel">
    <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="3" aria-label="Slide 4"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="4" aria-label="Slide 5"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="https://24wallpapers.com/app-gateway/wallpaper-uploads/wallpapers/legacyUploads/wi2165da692f6-a82c-4a84-a372-0b089b41fa09868962133.jpg" class="d-block w-100" alt="...">
          <div class="carousel-caption d-none d-md-block">
            <h5>First slide label</h5>
            <p>Some representative placeholder content for the first slide.</p>
            <button @click="openModal">상세정보</button>
          </div>
        </div>
        <div class="carousel-item">
          <img src="https://mblogthumb-phinf.pstatic.net/MjAxNzEyMTdfMTgg/MDAxNTEzNDk1MzkxMDcz.9QowjBcPhoH49YnxJRnoLe_7HUKYlqtRzrTu2gH6JiEg.E-Uw7LGpsZuyY0OUAPhD4frvXbv6Fq-KoqTc4K2XaxYg.JPEG.epik7777/aesthetic-bambi-dark-dark-purple-Favim.com-3838997.jpg?type=w800" class="d-block w-100" alt="...">
          <div class="carousel-caption d-none d-md-block">
            <h5>Second slide label</h5>
            <p>Some representative placeholder content for the second slide.</p>
            <button @click="openModal">상세정보</button>
          </div>
        </div>
        <div class="carousel-item">
          <img src="https://i.pinimg.com/736x/06/80/93/06809351224cf53ebcd1ec649572e48d.jpg" class="d-block w-100" alt="...">
          <div class="carousel-caption d-none d-md-block">
            <h5>Third slide label</h5>
            <p>Some representative placeholder content for the third slide.</p>
            <button @click="openModal">상세정보</button>
          </div>
        </div>
        <div class="carousel-item">
          <img src="https://64.media.tumblr.com/0c051e203cbc69d709e67effb12fe14c/946ec8b1de5337a5-45/s1280x1920/89ef0ac0ea4a965a50ebc25d4715c3af204ec9ad.jpg" class="d-block w-100" alt="...">
          <div class="carousel-caption d-none d-md-block">
            <h5>Fourth slide label</h5>
            <p>Some representative placeholder content for the Fourth slide.</p>
            <button @click="openModal">상세정보</button>
          </div>
        </div>
        <div class="carousel-item">
          <img src="https://wallpaper.dog/large/17133733.jpg" class="d-block w-100" alt="...">
          <div class="carousel-caption d-none d-md-block">
            <h5>Fifth slide label</h5>
            <p>Some representative placeholder content for the fifth slide.</p>
            <button @click="openModal">상세정보</button>
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>

<script>
export default {
    name: 'Carousel',
    data: function () {
        return {

        }
    },
    methods: {
      openModal: function () {
        
      }
    },
}
</script>

<style>
  img {
    height: 700px;
    object-fit: cover;
  }
</style>