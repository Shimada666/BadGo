<template>
  <div class="register">
    <a-row style="width: 90%; margin: 0 auto; display: flex; align-items: center; flex-wrap: wrap;">
      <a-col
        class="slogan"
        :xs="24"
        :sm="14">
        <div>
          Built for<br>
          SJTUers
        </div>
        <!--<div class="help">-->
        <!--  媒体站在已有电影站的基础上 ，使用Jellyfin提供媒体管理服务。<br>-->
        <!--  增加了番剧 、电视剧 、音乐、网课等资源。<br>-->
        <!--  为同学们提供更加丰富的内网生活，希望大家能够喜欢。-->
        <!--</div>-->
      </a-col>
      <a-col
        :xs="24"
        :sm="10">
        <a-form
          class="register-form"
          layout="vertical">
          <a-form-item
            label="用户名"
            v-bind="validateInfos.username">
            <a-input v-model:value="formModel.username" size="large" />
          </a-form-item>
          <a-form-item
            label="密码"
            v-bind="validateInfos.password">
            <a-input
              v-model:value="formModel.password"
              type="password"
              size="large" />
          </a-form-item>
          <a-form-item>
            <a-button
              style="width: 100%;"
              type="primary"
              size="large"
              @click="onSubmit">
              登录
            </a-button>
          </a-form-item>
        </a-form>
      </a-col>
    </a-row>
  </div>
</template>

<script lang="ts">
import { AdminApi } from '@/api/admin'
import Cookies from 'js-cookie'
import { defineComponent, reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useForm } from '@ant-design-vue/use'

export default defineComponent({
  name: 'Login',
  setup (props, context) {
    const router = useRouter()
    const formModel = reactive({
      username: '',
      password: ''
    })
    const rules = reactive({
      username: [
        { required: true, message: '请输入用户名', trigger: 'blur' }
      ],
      password: [
        { required: true, message: '请输入密码', trigger: 'blur' }
      ]
    })
    const { resetFields, validate, validateInfos } = useForm(formModel, rules)
    const onSubmit = async () => {
      await validate()
      const res = await AdminApi.login(formModel)
      Cookies.set('accessToken', res.data.accessToken)
      Cookies.set('refreshToken', res.data.refreshToken)
      await router.replace('/')
    }

    return {
      labelCol: { span: 4 },
      wrapperCol: { span: 14 },
      formModel,
      rules,
      onSubmit,
      validateInfos
    }
  }
})
</script>
<style lang="scss" scoped>
@media (max-width: 768px) {
  .slogan {
    margin: 20px 0;
    font-size: 48px;
    font-weight: 500;
    text-align: center;
    .help {
      margin-top: 20px;
    }
  }
}

@media (min-width: 768px) {
  .register {
    justify-content: center;
    display: flex;
    align-items: center;
    flex: 1;
  }
  .slogan {
    font-size: 64px;
    font-weight: 500;
  }
}
.register {
  width: 100vw;
  height: 100vh;
  .slogan {
    .help {
      text-align: left;
      font-size: 16px;
      font-weight: 400;
    }
  }
  .register-form {
    border-radius: 5px;
    padding: 20px;
    .label {
      height: 30px;
      line-height: 30px;
    }
  }
}
</style>
