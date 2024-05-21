<template>
    <div class="column is-2">
        <div class="box is-text-color-black">
            <figure>
                <img :src="product.get_thrumbnail" class="image">
            </figure>

            <h3 class="is-size-4">{{ product.name }}</h3>
            <p class="is-size-6 has-text-grey">От {{ product.price }}₽</p>

            <RouterLink v-bind:to="product.get_absolute_url" class="button is_dark mt-4">Детали</RouterLink>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Productox',
    props: {
        product: Object
    }
}
</script>


<style scoped>
  .image{
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
  .image{
    margin-left: 25%;
  }
</style>