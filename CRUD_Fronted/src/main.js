// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

// require('@/assets/bootstrap/css/bootstrap.min.css')
import '@/assets/bootstrap/css/bootstrap.min.css'
import 'bootstrap' // after install: npm install bootstrap jquery popper.js

/* import { library } from '@fortawesome/fontawesome-svg-core'
import { faCoffee } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
library.add(faCoffee)
Vue.component('font-awesome-icon', FontAwesomeIcon) */


/* import '@/assets/bootstrap/js/jquery-3.4.1.min.js'
import '@/assets/bootstrap/js/popper.min.js'
import '@/assets/bootstrap/js/bootstrap.js' */

/* import "https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js"
import "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
import "https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" */

/* import jquery from '@/assets/bootstrap/js/jquery-3.4.1.min.js';
Object.defineProperty(Vue.prototype, '$JQuery', { value: jquery }); */

/* import '@/assets/bootstrap/js/a.js'
import '@/assets/bootstrap/js/b.js' */

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
	el: '#app',
	router,
	components: { App },
	template: '<App/>'
})
