<template>
	<div class="container" id="app">
		<!-- <img src="./assets/logo.png"> -->
		<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
			<router-link :to="{name: 'Home'}" class="navbar">
				<img src="./assets/img/agenda.png" width="30" height="30" alt="">
			</router-link>
			<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
				<span class="navbar-toggler-icon"></span>
			</button>

			<div class="collapse navbar-collapse" id="navbarSupportedContent">
				<ul class="navbar-nav mr-auto">
					<li class="nav-item active">
						<router-link :to="{name: 'Home'}" class="nav-link"> Inicio </router-link>
						<!-- <a class="nav-link" href="/"> Inicio <span class="sr-only">(current)</span></a> -->
					</li>
					<!--<li class="nav-item">
						<a class="nav-link" href="#">Link</a>
					</li> -->
					<li class="nav-item dropdown" v-show="isLogin()">
						<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
							Amigos
						</a>
						<div class="dropdown-menu" aria-labelledby="navbarDropdown">
							<!-- <a class="dropdown-item" href="/create_friend"> Agregar </a> -->
							<router-link :to="{name: 'CreateFriend'}" class="dropdown-item"> Agregar </router-link>
							<router-link :to="{name: 'ListFriends', params: {status: 0}}" class="dropdown-item"> Listar </router-link>
							<!-- <a class="dropdown-item" href="/list_friends"> Listar </a> -->
							<!-- OBS router-link -->
							<div class="dropdown-divider"></div>
							<a class="dropdown-item disabled" href="#"> Buscar </a>
						</div>
					</li>
					<li class="nav-item" v-show="!isLogin()">
						<router-link :to="{name: 'Login'}" class="nav-link"> Login </router-link>
					</li>
					<li class="nav-item" v-show="isLogin()">
						<button class="nav-link btn btn-link" v-on:click="logout()"> Logout </button>
					</li>
				</ul>
				<form class="form-inline my-2 my-lg-0">
					<input class="form-control mr-sm-2" type="search" placeholder="Buscar" aria-label="Search">
					<button class="btn btn-outline-warning my-2 my-sm-0" type="submit"> Buscar </button>
				</form>
			</div>
		</nav>
		<router-view/>
	</div>
</template>

<script>
	//import {isLogin, login, logout} from '../utils/auth'
	import decode from 'jwt-decode';
	export default {
		name: 'App',
		methods: {
			logout () {
				clearAccessToken()
				this.$router.push({name: 'Home'})
			},
			isLogin () {				
				//const accessToken = getAccessToken()
                //return !!accessToken && !isTokenExpired(accessToken)
                return isLogin()
			}
		},
		computed: {
        },
	}
	function getTokenExpirationDate(encodedToken) {
		const token = decode(encodedToken);
		if (!token.exp) { 
			return null
		}
		const date = new Date(0)
		date.setUTCSeconds(token.exp)
		return date;
	}
	function isTokenExpired(token) {
		const expirationDate = getTokenExpirationDate(token)
		return expirationDate < new Date()
	}
	function getAccessToken() {
		return localStorage.getItem('access_token')
	}
	function isLogin () {
		const accessToken = getAccessToken()
        return !!accessToken && !isTokenExpired(accessToken)
	}
	function clearAccessToken() {
		localStorage.removeItem('access_token');
	}
</script>

<style>
	#app {
		font-family: 'Avenir', Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		color: #2c3e50;
		/* margin-top: 60px; */
	}
</style>
