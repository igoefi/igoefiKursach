<template>
    
</template>

<script>
export default{
    data() {
        return {
            categories: []
        }
    },
    mounted(){

    },
    methods: {
      getCategories(){
      axios
        .get("/api/v1/categories/")
        .then(response => {
          this.categories = response.data
        }) 
    },
    }
}
</script>
