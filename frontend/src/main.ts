import './assets/base.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

// import 'shepherd.js/dist/css/shepherd.css'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
