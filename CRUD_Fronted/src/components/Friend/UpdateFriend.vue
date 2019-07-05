<template>
    <div class="card border-primary mt-1">
        <div class="card-header"> Editar amigo </div>
        <div class="card-body text-primary">
            <!-- <form class="w-50" @submit="onSubmit"> -->
            <form class="w-50" v-on:submit.prevent="updateFriend">
                <div class="form-group row">
                    <label class="col-md-4 col-form-label"> Nombres </label>
                    <div class="col-md-8">
                        <input type="text" class="form-control" name="first_name" v-model.trim="form.first_name" required>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-md-4 col-form-label"> Apellidos </label>
                    <div class="col-md-8">
                        <input type="text" class="form-control" name="last_name" v-model.trim="form.last_name" required>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-md-4 col-form-label"> Teléfono </label>
                    <div class="col-md-8">
                        <input type="tel" class="form-control" name="phone" v-model.trim="form.phone" required>
                        <small class="form-text text-muted"> Ejemplo: 973 123 123 </small>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-md-4 col-form-label"> Dirección </label>
                    <div class="col-md-8">
                        <input type="text" class="form-control" name="address" v-model.trim="form.address" required>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-md-4 col-form-label"> Cumpleaños </label>
                    <div class="col-md-8">
                        <input type="date" class="form-control" name="birthday" v-model.trim="form.birthday" required>
                    </div>
                </div>
                <div class="form-group row">
                    <div class="col-md-8">
                        <button type="submit" class="btn btn-primary" name="update"> Actualizar </button>
                        <router-link :to="{name: 'ListFriends', params: {status: 0}}" class="btn btn-secondary"> Cancelar </router-link>
                    </div>
                </div>
            </form>
        </div>
    </div>
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
            getFriend () {
                var token = localStorage.getItem('access_token')
                const url = `${process.env.BASE_URL}/api/friend/${this.id}/`
                axios.defaults.headers.common['Authorization'] = 'JWT ' + token
                axios.get(url).then((response) => {
                    this.form = response.data
                })
                .catch((err) => {
                    console.log(err)
                })
            },
            updateFriend () {
                var token = localStorage.getItem('access_token')
                const url = `${process.env.BASE_URL}/api/friend/${this.id}/`
                axios.defaults.headers.common['Authorization'] = 'JWT ' + token
                axios.put(url, this.form).then((response) => {
                    console.log(response.status)
                    // this.form = response.data
                    // location.href = "/friends"
                    // router.push({ name: 'ListFriends', params: { userId: 123 }})
                    this.$router.push({name: 'ListFriends', params: {status: response.status}})
                })
                .catch((err) => {
                    console.log(err)
                })
            }
        },
        created () {
            this.getFriend()
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
