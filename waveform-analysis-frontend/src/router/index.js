import Main from '../views/index.vue'
import Abstract from '../views/layout/abstract.vue'
import Home from '../views/home/home.vue'
import Login from '../views/login.vue'
import Profile from '../views/profile/profile.vue'
import UserList from '../views/user/user-list.vue'
import NewUserList from '../views/user/new-user-list.vue'
import Table from '../views/table/table.vue'
import Ai from '../components/ai-functions/ai.vue'

export const loginRouter = {
  path: '/login',
  name: 'login',
  meta: {
    title: 'Login'
  },
  component: Login
}

export const appRouter = [
  {
    title: 'Home',
    path: '/home',
    name: 'home',
    icon: 'ios-home',
    component: Home
  },

  {
    title: 'AI Functions',
    path: '/statistics',
    name: 'statistics',
    icon: 'stats-bars',
    component: Abstract,
    children: [
      // {
      //   title: 'AI Function1',
      //   name: 'stats_new',
      //   path: 'new',
      //   icon: 'ios-paper',
      //   component: Login
      // },
      {
        title: 'AI Function1',
        name: 'stats_activated',
        path: 'activated',
        icon: 'images',
        component: Ai
      },
      {
        title: 'AI Function2',
        name: 'stats_time',
        path: 'time',
        icon: 'images',
        component: Ai
      },
      {
        title: 'AI Function3',
        name: 'retention',
        path: 'retention',
        icon: 'images',
        component: Ai
        //component: Table
      }
    ]

  }

]

export const mainRouter = {
  path: '/',
  redirect: '/home',
  name: 'index',
  component: Main,
  children: appRouter
}

export const routers = [
  loginRouter,
  mainRouter,
  // catch all redirect
  {path: '*', redirect: '/home'}

]

