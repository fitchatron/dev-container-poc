import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
      '@components': fileURLToPath(new URL('./src/components', import.meta.url)),
      '@views': fileURLToPath(new URL('./src/views', import.meta.url)),
      '@services': fileURLToPath(new URL('./src/services', import.meta.url)),
      '@plugins': fileURLToPath(new URL('./src/plugins', import.meta.url)),
      '@stores': fileURLToPath(new URL('./src/stores', import.meta.url)),
      '@assets': fileURLToPath(new URL('./src/assets', import.meta.url)),
      '@lib': fileURLToPath(new URL('./src/lib', import.meta.url))
    }
  },
  server: {
    port: 3000,
    proxy: {
      '^/api/.*': {
        target: 'http://api:80/',
        changeOrigin: true,
        secure: false
      }
    }
  },
  preview: {
    port: 3000,
    proxy: {
      '^/api/.*': {
        target: 'http://api:80/',
        changeOrigin: true,
        secure: false
      }
    }
  }
})
