<template>
   
</template>

<script>
    import axios from "axios"

    export default {
        data () {
            return {
                id: this.$route.params.id,
                form: {
                    first_name: "",
                    last_name: "",
                    phone: "",
                    address: "",
                    birthday: ""
                }
            }
        },
        methods: {
            deleteFriend () {
                const url = `${process.env.BASE_URL}/friend/${this.id}/`
                var op = window.confirm('Estas seguro?') 
                if (op) {
                    axios.delete(url).then((response) => {
                        // this.form = response.data
                        this.$router.push({name: 'ListFriends', params: {status: 0}})
                    })
                    .catch((err) => {
                        console.log(err)
                    })
                } else {
                    this.$router.push({name: 'ListFriends', params: {status: 0}})
                }
            }
        },
        created () {
            this.deleteFriend()
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    
</style>
