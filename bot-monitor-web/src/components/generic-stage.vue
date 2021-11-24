<template>
  <div class="container">
    <div class="title">
      {{ title }}
    </div>
    <div class="operate">
      <div class="filter">
        <div class="filter-item">
          这里预留给搜索功能
          <slot name="filter" />
        </div>
      </div>
      <div class="operate-button">
        <a-button type="primary" @click="handleClick">
          <template #icon>
            <PlusOutlined />
          </template>
          {{ buttonText }}
        </a-button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, watch } from 'vue'
import { PlusOutlined } from '@ant-design/icons-vue'

export default defineComponent({
  name: 'GenericStage',
  components: {
    PlusOutlined
  },
  props: {
    title: {
      type: String,
      required: true
    },
    buttonText: {
      type: String,
      required: true
    }
  },
  emits: {
    'button-click': null,
    'query-update': (newVal: string) => true
  },
  setup (props, context) {
    const q = ref('')
    const handleClick = _ => context.emit('button-click')
    watch(q, (newVal, oldVal) => context.emit('query-update', newVal))
    return {
      q,
      handleClick
    }
  }
})
</script>

<style scoped lang="scss">
.title {
  font-size: 18px;
  color: #333;
  margin-bottom: 16px;
}
.operate {
  display: flex;
  width: 100%;
  justify-content: space-between;
  margin-bottom: 16px;
  .filter {
    display: flex;
    align-items: center;
  }
  .el-input {
    width: 320px;
  }
  .operate-button {
    font-size: 14px !important;
  }
}
</style>
