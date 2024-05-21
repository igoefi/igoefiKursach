<template>
  <div class="home">
    <section class="hero is-large is-dark mb-6 is-have-img is-3">
      <div class="hero-body has-text-lefted mb-6 is-marged">
        <p class="title mb-6 is-text-color is-family-sans-serif" >
          SOFT
        </p>
        <p class="subtitle is-text-color is-family-sans-serif">
          Работаем с 1914 года
        </p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered is-text-color-black">Популярное</h2>
      </div>

      <ProductBox
        v-for="product in bestProducts"
        v-bind:key="product.id"
        v-bind:product="product"/>
      
    </div>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered is-text-color-black">Новинки</h2>
      </div>

      <ProductBox
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product"/>

    </div>
      
  </div>
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox.vue'

export default {
  name: 'HomeView',
  data(){
    return{
      latestProducts: [],
      bestProducts: []  
    }
  },
  components: {
    ProductBox
  },
  mounted(){
    this.getLatestProducts()
    this.getBestProducts()
    document.title = "SOFT"
  },
  methods: {
    getLatestProducts(){
      axios
        .get("/api/v1/latest-products/")
        .then(response => {
          this.latestProducts = response.data
        }) 
    },
    getBestProducts(){
      axios
        .get("/api/v1/best-products/")
        .then(response => {
          this.bestProducts = response.data
        }) 
    }
  }
}
</script>

<style lang="scss">
  .is-have-img{
    background-image: url("../assets/mainImg.jpeg");
    background-position: center;
    background-size: cover;
  }
  .is-marged{
    margin-left: 3%;
    margin-right: 3%;
    max-height: 110%;
  }
  .is-text-color{
    color: rgb(255, 255, 255);
  }
</style>
