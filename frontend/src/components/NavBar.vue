<script setup lang="ts">
import { ref } from 'vue'
import { RouterLink, useRoute } from 'vue-router'

const isExpanded = ref(false)
const route = useRoute()

function toggleIsExpanded() {
  isExpanded.value = !isExpanded.value
}
</script>

<template>
  <nav>
    <div
      class="flex flex-col md:flex-row md:place-content-between md:items-center bg-slate-300 px-1 py-2 border-b-2 border-slate-600"
    >
      <div class="flex place-content-between items-center">
        <RouterLink to="/">
          <h1 class="font-semibold">Marguarana</h1>
        </RouterLink>
        <button
          data-collapse-toggle="navbar-mobile"
          type="button"
          class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-black rounded-lg md:hidden hover:bg-black focus:outline-none focus:ring-2 focus:ring-black dark:text-black dark:hover:bg-black dark:focus:ring-black"
          aria-controls="navbar-mobile"
          :aria-expanded="isExpanded"
          @click.prevent="toggleIsExpanded"
        >
          <span class="sr-only">Open main menu</span>
          <svg
            class="w-5 h-5"
            :aria-hidden="isExpanded"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 17 14"
          >
            <path
              stroke="currentColor"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M1 1h15M1 7h15M1 13h15"
            />
          </svg>
        </button>
      </div>
      <ul class="flex flex-col md:flex-row md:gap-4 gap-1">
        <RouterLink to="/v-tour"
          ><li
            class="ml-2 md:ml-0 hover:bg-slate-500 px-4 py-2 rounded hover:text-white"
            :class="{
              'underline border rounded border-slate-500 hover:cursor-not-allowed':
                route.fullPath === '/v-tour'
            }"
          >
            Vue Tour
          </li></RouterLink
        >
        <RouterLink to="/v-onboarding"
          ><li
            class="ml-2 md:ml-0 hover:bg-slate-500 px-4 py-2 rounded hover:text-white"
            :class="{
              'underline border rounded border-slate-500 hover:cursor-not-allowed':
                route.fullPath === '/v-onboarding'
            }"
          >
            v-onboarding
          </li></RouterLink
        >
        <RouterLink to="/vue-page-guide"
          ><li
            class="ml-2 md:ml-0 hover:bg-slate-500 px-4 py-2 rounded hover:text-white"
            :class="{
              'underline border rounded border-slate-500 hover:cursor-not-allowed':
                route.fullPath === '/vue-page-guide'
            }"
          >
            Vue Page Guide
          </li></RouterLink
        >
        <RouterLink to="/shepherd-view"
          ><li
            class="ml-2 md:ml-0 hover:bg-slate-500 px-4 py-2 rounded hover:text-white"
            :class="{
              'underline border rounded border-slate-500 hover:cursor-not-allowed':
                route.fullPath === '/shepherd-view'
            }"
          >
            Shepherd
          </li></RouterLink
        >
        <li class="ml-2 md:ml-0 px-4 py-2 rounded cursor-not-allowed">Shop</li>
        <RouterLink to="/about">
          <li
            class="ml-2 md:ml-0 hover:bg-slate-500 px-4 py-2 rounded hover:text-white"
            :class="{
              'underline border rounded border-slate-500 hover:cursor-not-allowed':
                route.fullPath === '/about'
            }"
          >
            About
          </li>
        </RouterLink>
      </ul>
      <div>
        <button class="bg-blue-700 px-4 py-2 rounded text-white">Login</button>
      </div>
    </div>
  </nav>
</template>
