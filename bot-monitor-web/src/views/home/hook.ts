import { onMounted, ref } from 'vue'
import BotApi, { BotInfo } from '@/api/bot'

export function useBotInfo () {
  const info = ref(new BotInfo())

  async function getInfo () {
    const res = await BotApi.getInfo()
    info.value = res.data
  }

  onMounted(async function () {
    await getInfo()
  })

  return {
    info,
    getInfo
  }
}

export function useBotPlugins () {
  const plugins = ref([])
  async function listPlugins () {
    const res = await BotApi.listPlugins()
    plugins.value = res.data
  }

  onMounted(async function () {
    await listPlugins()
  })
  return {
    plugins,
    listPlugins
  }
}
