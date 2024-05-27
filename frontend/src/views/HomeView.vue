<script setup lang="ts">
import { getHomeRoute, getItemByIdRoute } from '@services/backend_service'
async function getHomeData() {
  const resp = await getHomeRoute()
  const data = await resp.json()
  console.log('home response is', data)
  alert(JSON.stringify(data))
}
async function getRandomItemData() {
  const id = randomIntFromInterval(1, 100)
  const resp = await getItemByIdRoute(id)
  console.log(`item ${id} response is`, resp.data)
  alert(JSON.stringify(resp.data))
}

function randomIntFromInterval(min: number, max: number) {
  // min and max included
  return Math.floor(Math.random() * (max - min + 1) + min)
}
</script>

<template>
  <main class="flex flex-col gap-2">
    <h1 class="text-2xl font-bold">Main Page</h1>
    <button
      title="fetch home"
      @click.prevent="getHomeData"
      class="rounded bg-sky-800 text-white w-full py-8 text-lg hover:bg-sky-600"
    >
      Fetch Home
    </button>
    <button
      title="fetch home"
      @click.prevent="getRandomItemData"
      class="rounded bg-sky-800 text-white w-full py-8 text-lg hover:bg-sky-600"
    >
      Fetch Item
    </button>
  </main>
</template>
