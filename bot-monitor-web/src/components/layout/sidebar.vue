<script lang="ts" setup>
import { ref } from 'vue'
import { LaptopOutlined } from '@ant-design/icons-vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const clickMenuItem = ({ item, key, keyPath }) => {
  router.push({ name: key })
}

const selectedKeys1 = ref<string[]>(['2'])
const selectedKeys2 = ref<string[]>(['1'])
const collapsed = ref<boolean>(false)
const openKeys = ref<string[]>(['sub1'])
</script>

<template>
  <a-layout-sider width="200" style="background: #fff;">
    <div class="logo">Hi, I'm Ergo</div>
    <a-menu
      v-model:selectedKeys="selectedKeys2"
      v-model:openKeys="openKeys"
      :style="{ height: '100%', borderRight: 0 }"
      mode="inline"
      @click="clickMenuItem">
      <a-menu-item key="home">
        <laptop-outlined />
        Dashboard
      </a-menu-item>
      <a-sub-menu key="sub1">
        <template #title>
          <span>
            <laptop-outlined />
            Bot概览
          </span>
        </template>
        <a-menu-item key="guide">基本信息</a-menu-item>
      </a-sub-menu>
      <!--<a-menu-item key="project">-->
      <!--  <laptop-outlined />-->
      <!--  工程创建-->
      <!--</a-menu-item>-->
    </a-menu>
  </a-layout-sider>
</template>

<style scoped lang="scss">
.logo {
  height: 32px;
  margin: 16px;
  font-size: 24px;
  font-weight: 600;
  text-align: center;
}
//.sidebar-container {
//  position: sticky;
//  left: 0;
//  top: 48px;
//  width: 220px;
//  height: calc(100vh - 48px);
//  background-color: #f7f7f7;
//  border-right: solid 1px #e6e6e6;
//  .sidebar-title {
//    display: inline-block;
//    height: 48px;
//    line-height: 48px;
//    width: 100%;
//    overflow: hidden;
//    .title-text {
//      color: rgba(0, 0, 0, 0.75);
//      font-size: 18px;
//      margin-left: 14px;
//      line-height: 24px;
//      vertical-align: middle;
//      word-break: keep-all;
//    }
//  }
//}
</style>
