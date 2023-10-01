import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/Home.vue'
import MapBoardView from '../views/MapBoard.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/board',
      name: 'Board',
      component: MapBoardView
    },
  ]
})

export default router
