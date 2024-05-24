<script setup lang="ts">
import Shepherd from 'shepherd.js'
import { onMounted } from 'vue'

const tour = new Shepherd.Tour({
  useModalOverlay: true,
  defaultStepOptions: {
    classes: 'shadow-md bg-purple-dark',
    scrollTo: true
  }
})

tour.addStep({
  id: 'First Step',
  text: 'This step is attached to the bottom of the <code>.example-css-selector</code> element.',
  attachTo: {
    element: '.example-css-selector',
    on: 'bottom'
  },
  classes: 'example-step-extra-class',
  buttons: [
    {
      text: 'Next',
      action: tour.next
    }
  ]
})

tour.addStep({
  id: 'Second Step',
  text: 'This step is attached to the bottom of the <code>.example-css-selector</code> element.',
  attachTo: {
    element: '#foo',
    on: 'bottom'
  },
  classes: 'example-step-extra-class',
  buttons: [
    {
      text: 'Finish',
      action: tour.complete
    }
  ]
})

onMounted(() => {
  tour.start()
})
</script>

<template>
  <div class="flex flex-col md:flex-row-reverse items-center place-content-around bg-green-300">
    <div>
      <h1 class="text-center">Marguarna</h1>
      <h3 class="text-center">Margaritas + Guarana = Marguarna</h3>
      <p class="text-center">Marguarna.The drink tha causes the MOST health issues. Hands. Down.</p>
      <p class="uppercase font-bold">DEPRICATED DEPS</p>
    </div>
    <img class="md:w-1/2" src="/img/platypus.jpeg" alt="platypus" />
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
      <div class="flex flex-col items-center gap-4">
        <img class="w-4/5 md:w-72 rounded" src="/img/koala-suit.png" alt="koala-suit" />
        <p class="text-center">Designed by the best mixologists this side of Coober Pedy.</p>
      </div>
      <div class="flex flex-col items-center gap-4 example-css-selector">
        <img class="w-4/5 md:w-72 rounded" src="/img/wired-koala.jpeg" alt="wired-koala" />
        <p class="text-center">Gives you the energy to be mashing it all night.</p>
      </div>
    </div>
  </div>
  <div class="flex flex-col md:flex-row items-center place-content-around bg-indigo-300">
    <img class="md:w-1/2" src="/img/heart-attack.jpeg" alt="heart-attack" />
    <div class="flex flex-col items-center">
      <p>Not fit for human consumption</p>
      <button class="bg-blue-700 px-4 py-2 rounded text-white" type="button" @click.prevent="">
        Reset
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
</template>
