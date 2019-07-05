<template>
    <div class="card border-primary mt-1">
        <div class="card-header"> Nuevo amigo </div>
        <div class="card-body text-primary">
            <form class="w-50" v-on:submit.prevent="createFriend()">
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
                        <input type="tel" class="form-control" name="phone" pattern="[0-9]{3}[0-9]{3}[0-9]{3}" v-model.trim="form.phone" required>
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
                        <button type="submit" class="btn btn-primary" name="create"> Crear </button>
                        <button type="reset" class="btn btn-secondary" name="reset"> Limpiar </button>
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
            createFriend () {
                var token = localStorage.getItem('access_token')
                const url = `${process.env.BASE_URL}/api/friend/`
                axios.defaults.headers.common['Authorization'] = 'JWT ' + token
                axios.post(url, this.form).then((response) => {
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

        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
