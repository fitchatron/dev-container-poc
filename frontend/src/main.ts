import './assets/base.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import VueJsTour from '@globalhive/vuejs-tour'
import '@globalhive/vuejs-tour/dist/style.css'

import VPageGuide from 'vue-page-guide'

// import 'shepherd.js/dist/css/shepherd.css'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.use(VueJsTour)
app.use(VPageGuide)

app.mount('#app')
