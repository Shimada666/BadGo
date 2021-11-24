<script lang="ts" setup>
import { useBotInfo, useBotPlugins } from '@/views/home/hook'

const { info } = useBotInfo()
const { plugins } = useBotPlugins()
</script>

<template>
  <a-typography>
    <a-typography-title>{{ info.name }}</a-typography-title>
    <a-typography-paragraph>
      Working Directory: {{ info.dir }}
    </a-typography-paragraph>
  </a-typography>
  <a-card title="插件总览" class="mt-8">
    <!--<template #extra><a href="#">刷新</a></template>-->
    <a-row>
      <a-col
        v-for="(item,index) in plugins"
        :key="index"
        :span="6">
        <a-card class="m-2" :title="item.name">{{ item.module }}</a-card>
      </a-col>
    </a-row>
  </a-card>
</template>

<style scoped>

</style>
