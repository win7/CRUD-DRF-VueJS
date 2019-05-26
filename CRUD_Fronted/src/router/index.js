import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/Home'
import ListFriends from '@/components/Friend/ListFriends/'
import UpdateFriend from '@/components/Friend/UpdateFriend/'
import DeleteFriend from '@/components/Friend/DeleteFriend/'
import CreateFriend from '@/components/Friend/CreateFriend/'

Vue.use(Router)

export default new Router({
	routes: [
		{
			path: '/hello',
			name: 'HelloWorld',
			component: HelloWorld
		},
        {
            path: '/',
            name: 'Home',
            component: Home
        },
        {
            path: '/list_friends/:status',
            name: 'ListFriends',
            component: ListFriends
        },
        {
            path: '/update_friend/:id',
            name: 'UpdateFriend',
            component: UpdateFriend
        },
        {
            path: '/delete_friend/:id',
            name: 'DeleteFriend',
            component: DeleteFriend
        },
        {
            path: '/create_friend',
            name: 'CreateFriend',
            component: CreateFriend
        },
	],
    mode: 'history'
})
