# U2-API (迫真)
完全不知道文档应该怎么写，凑合看下吧。 (  
服务器比较拉跨再加上技术拉跨，无法保证高可用性。 (

****

## 鉴权
`POST` `https://u2.kysdm.com/api/v1/token`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | :--:  |
| uid  | int | u2账户id |

请将返回 key 值写入[个人说明](https://u2.dmhy.org/usercp.php?action=personal)中，并且在使用中不要移除 key。

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/1.png)

****

`POST` `https://u2.kysdm.com/api/v1/token`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| key | str | 上一步操作返回的 key 值 |

将返回 token，token 请妥善保管。  
此 token 暂无有效期。  
如需重置 token ，重复此步骤即可。

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/2.png)

****

## 魔法
`GET` `https://u2.kysdm.com/api/v1/promotion`

|  参数   | 数据类型  | 说明  |
|  ----  | :--:  | ----  |
| Authorization  | str | 将 token 添加到请求头 heraders 中 |
| scope [optional] | str | 魔法类型 `global` `public` `private` `all`<br>默认值 `all`|
| maximum [optional]| int | 返回数据条数<br>默认值 `10`<br>最大 `30` |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/3.png)

****

## 日志
`GET` `https://u2.kysdm.com/api/v1/log`

|  参数   | 数据类型  | 说明  |
|  ----  | :--:  | ----  |
| Authorization  | str | 将 token 添加到请求头 heraders 中 |
| maximum [optional]| int | 返回数据条数<br>默认值 `10`<br>最大 `30` |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/4.png)

****

## 聊天
`GET` `https://u2.kysdm.com/api/v1/msg`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| Authorization  | str | 将 token 添加到请求头 heraders 中 |
| maximum [optional]| int | 返回数据条数<br>默认值 `10`<br>最大 `50` |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/5.png)
