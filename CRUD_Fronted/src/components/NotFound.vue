<template>
    <div class="jumbotron jumbotron-fluid text-center">
        <div class="container">
            <h1 class="display-4"> {{ msg }} </h1>
            <p class="lead"> ... </p>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'NotFound',
        data () {
            return {
                msg: "(404) Page NotFound"
            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    /* h1, h2 {
        font-weight: normal;
    }
    ul {
        list-style-type: none;
        padding: 0;
    }
    li {
        display: inline-block;
        margin: 0 10px;
    }
    a {
        color: #42b983;
    } */
</style>
