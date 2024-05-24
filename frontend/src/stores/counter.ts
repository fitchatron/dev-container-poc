import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const showGuide = ref(false)
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }

  function toggleShowGuide() {
    showGuide.value = !showGuide.value
  }

  return { count, doubleCount, increment, showGuide, toggleShowGuide }
})
