import service from '@/utils/api'

export class BotInfo {
  name: string
  dir: string
}

class BotApi {
  static getInfo (): Ajax.PromiseAxiosResponse<BotInfo> {
    return service.get('/monitor/api/v1/info')
  }
  static listPlugins () {
    return service.get('/monitor/api/v1/plugins')
  }
}

export default BotApi
