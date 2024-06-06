<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { VOnboardingWrapper, useVOnboarding } from 'v-onboarding'
import 'v-onboarding/dist/style.css'

const wrapper = ref(null)
const { start, goToStep, finish } = useVOnboarding(wrapper)
const steps = [
  { attachTo: { element: '#selectByID' }, content: { title: 'Welcome! This is the first step' } },
  {
    attachTo: { element: '.selectByClass' },
    content: {
      title: 'This is the second step, placed on the bottom of the target',
      description: "This is a description field and I really don't know what to write here..."
    }
  },
  {
    attachTo: { element: '#foo' },
    content: {
      title: 'This is the third step',
      description: 'Click to reset'
    }
  }
]

onMounted(() => {
  start()
})

const jaysonToString = () => {
  let hi;
  console.log(JSON.stringify(steps));
} 
</script>

<template>
  <div class="flex flex-col md:flex-row-reverse items-center place-content-around bg-green-300">
    <div>
      <h1 class="text-center">Marguarna</h1>
      <h3 class="text-center">Margaritas + Guarana = Marguarna</h3>
      <p class="text-center">Marguarna.The drink tha causes the MOST health issues. Hands. Down.</p>
      <p class="uppercase font-bold">DEPRICATED DEPS</p>
      <p class="uppercase font-bold">Preferred ✅</p>

      <ul class="list-disc">
        <li>Vue3 compatible</li>
        <li>TypeScript compatible</li>
        <li>Styling works well</li>
        <li>Simple and meets needs</li>
      </ul>
    </div>
    <img id="selectByID" class="md:w-1/2" src="/img/platypus.jpeg" alt="platypus" />
  </div>
  <div class="bg-blue-300 py-4 px-2">
    <h1 class="text-center">Why drink Marguarana?</h1>
    <div
      class="flex flex-col md:flex-row gap-8 items-center place-content-center md:place-content-around"
    >
      <div class="flex flex-col items-center gap-4">
        <img class="w-4/5 md:w-72 rounded" src="/img/drink.jpeg" alt="drink" />
        <p class="text-center">Looks suspiciously good.</p>
      </div>
      <div class="flex flex-col items-center gap-4 selectByClass">
        <img class="w-4/5 md:w-72 rounded" src="/img/koala-suit.png" alt="koala-suit" />
        <p class="text-center">Designed by the best mixologists this side of Coober Pedy.</p>
      </div>
      <div class="flex flex-col items-center gap-4">
        <img class="w-4/5 md:w-72 rounded" src="/img/wired-koala.jpeg" alt="wired-koala" />
        <p class="text-center">Gives you the energy to be mashing it all night.</p>
      </div>
    </div>
  </div>
  <div class="flex flex-col md:flex-row items-center place-content-around bg-indigo-300">
    <img class="md:w-1/2" src="/img/heart-attack.jpeg" alt="heart-attack" />
    <div class="flex flex-col items-center">
      <p>Not fit for human consumption</p>
      <button
        class="bg-blue-700 px-4 py-2 rounded text-white"
        type="button"
        @click.prevent="start()"
      >
        Reset
      </button>
      <button
        class="bg-blue-700 px-4 py-2 rounded text-white"
        type="button"
        @click.prevent="jaysonToString()"
      >
        JSON
      </button>
    </div>
  </div>
  <div class="space-y-4 px-4 py-2">
    <h2 class="text-center">Contact Us</h2>
    <p>In hospital and the doctors need to know what you drank? Get in touch</p>
    <form class="flex flex-col gap-4 px-4">
      <div class="flex items-center flex-col">
        <label for="name" class="w-full">Name</label>
        <input
          type="text"
          name="name"
          class="border border-black rounded px-4 py-1 w-full"
          placeholder="Name"
          required
        />
      </div>
      <div class="flex items-center flex-col">
        <label for="email" class="w-full">Email</label>
        <input
          type="text"
          name="email"
          class="border border-black rounded px-4 py-1 w-full"
          placeholder="Name"
          required
        />
      </div>
      <div class="flex items-center flex-col">
        <label for="comment" class="w-full">Comment</label>
        <textarea
          name="comment"
          class="border border-black rounded px-4 py-1 w-full"
          placeholder="Comment"
          required
        ></textarea>
      </div>

      <button
        id="foo"
        disabled
        type="submit"
        class="bg-blue-700 px-4 py-2 rounded text-white disabled:bg-blue-100"
      >
        Submit
      </button>
    </form>
  </div>
  <VOnboardingWrapper ref="wrapper" :steps="steps" />
</template>
