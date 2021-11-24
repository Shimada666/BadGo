declare namespace Ajax {

  interface Error {
    code: number,
    msg: string,
    domain: string
  }

  // axios 返回数据
  interface AxiosResponse<T> {
    data: T,
    error: Error
  }

  // 类型别名
  export type PromiseAxiosResponse<T> = Promise<AxiosResponse<T>>
}
