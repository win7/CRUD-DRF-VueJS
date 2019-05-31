<template>
	<div class="card border-primary mt-1">
		<div class="card-header"> Login </div>
		<div class="card-body text-primary">
			<div class="alert alert-info" role="alert" v-show="alert">
  				Usuario | Contraseña con incorrectos
			</div>
			<form class="w-50" v-on:submit.prevent="login()">
				<div class="form-group">
					<label> Usuario </label>
					<input type="text" class="form-control" placeholder="" required v-model="form.username">
				</div>
				<div class="form-group">
					<label> Contraseña </label>
					<input type="password" class="form-control" placeholder="" required v-model="form.password">
				</div>
				<!-- <div class="form-group form-check">
					<input type="checkbox" class="form-check-input" id="exampleCheck1">
					<label class="form-check-label" for="exampleCheck1">Check me out</label>
				</div> -->
				<button type="submit" class="btn btn-primary"> Ingresar </button>
			</form>
		</div>
	</div>
</template>

<script>
	import axios from "axios"
	// import {login, logout, isLoggedIn} from '../../utils/auth'
	export default {
		name: 'Login',
		data () {
			return {
				form: {
					username: "",
					password: ""
				},
				alert: false
			}
		},
		methods: {
			login () {
				// login(this.form.username, this.form.password)
				const url = `${process.env.BASE_URL}/auth/obtain_token/`
				axios.post(url, this.form).then((response) => {
					if (response.data.token) {
						console.log("if")
						console.log(response.data.token)
						localStorage.setItem('access_token', response.data.token)
						console.log("if1")
						this.$router.push({name: 'ListFriends', params: {status: 0}})
						console.log("if2")
					} else {
						console.log("else")
						this.alert = true
					}					
				})
				.catch((err) => {
					console.log("err")
					console.log(err)
					this.alert = true
				})
			},
		},
		computed: {
		},
		created () {
		},
		mounted () {
		},
		beforeUpdate () {
		},
		updated () {
		}
	}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
	
</style>
