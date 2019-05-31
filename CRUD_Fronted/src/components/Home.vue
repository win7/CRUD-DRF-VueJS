<template>
	<div class="jumbotron mt-1">
		<link rel="stylesheet" 
        href="https://use.fontawesome.com/releases/v5.2.0/css/all.css" 
        integrity="sha384-hWVjflwFxL6sNzntih27bfxkr27PmbbK/iSvJ+a4+0owXq79v+lsFkW54bOGbiDQ" 
		crossorigin="anonymous">

		<h1 class="display-4"> {{ msg }} <i class="far fa-smile text-danger"></i> </h1>
		<p class="lead"> Tus amigos...  </p>
		<hr class="my-4">
		<p>
			Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
			tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
			quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
			consequat.
		</p>
		<router-link :to="{name: 'CreateFriend'}" class="btn btn-primary btn-lg"> Agregar </router-link>
	</div>
</template>

<script>
	export default {
		name: 'Home',
		data () {
			return {
				msg: 'Agenda 2019'
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
