import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsxPlugin from '@vitejs/plugin-vue-jsx'
import WindiCSS from 'vite-plugin-windicss'
import { resolve } from 'path'

export default defineConfig({
  plugins: [vue(), vueJsxPlugin(), WindiCSS()],
  resolve: {
    alias: {
      '@': resolve(__dirname, './src')
    }
  },
  server: {
    // 自定义代理规则
    proxy: {
      '/monitor/api': {
        target: 'http://localhost:9080',
        changeOrigin: true
      }
    }
  }
})
