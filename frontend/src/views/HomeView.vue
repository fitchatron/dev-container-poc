<script setup lang="ts">
import { getHomeRoute } from '@services/backend_service'
async function getHomeData() {
  await getHomeRoute()
}
</script>

<template>
  <main>
    <h1 class="text-2xl font-bold">Main Page</h1>
    <button
      title="fetch home"
      @click.prevent="getHomeData"
      class="rounded bg-sky-800 text-white w-full py-8 text-lg hover:bg-sky-600"
    >
      Fetch Home
    </button>
  </main>
</template>
