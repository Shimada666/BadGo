<template>
  <!--<Login v-if="route.name === 'login'" />-->
  <a-layout id="layout">
    <Nav class="nav" />
    <a-layout class="layout-view">
      <SideBar />
      <a-layout style="padding: 24px 24px;">
        <a-layout-content
          :style="{ background: '#fff', padding: '24px', margin: 0 }">
          <router-view />
        </a-layout-content>
      </a-layout>
    </a-layout>
  </a-layout>
</template>
<script lang="ts" setup>
import Nav from '@/components/layout/nav.vue'
import SideBar from '@/components/layout/sidebar.vue'
import Login from '@/views/login.vue'
import { useRoute } from 'vue-router'

const route = useRoute()
</script>
<style lang="scss" scoped>
#layout {
  .layout-view {
    min-height: calc(100vh - 48px);
  }
}
</style>
