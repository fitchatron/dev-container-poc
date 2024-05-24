<script setup lang="ts">
import { RouterView } from 'vue-router'
import NavBar from '@components/NavBar.vue'
import { ref } from 'vue'
import { useCounterStore } from '@stores/counter'

const counterStore = useCounterStore()
</script>

<template>
  <nav-bar />
  <section>
    <router-view />
  </section>
  <footer class="bg-slate-800 text-white">
    <p class="text-sm text-center">copyright 2024</p>
    <p class="text-sm text-center">
      Not fit for human consumption. You really should not drink this under any circumstances ☠️
    </p>
  </footer>
  <VPageGuide v-model="counterStore.$state.showGuide" />
</template>
