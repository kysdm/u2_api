# U2-API (迫真)
完全不知道文档应该怎么写，凑合看下吧。 (  
因API不是直接爬网页的，故无法开源。(开源了也没用.avif)  
服务器网络还是挺拉跨的，本地访问平均响应时间750ms，服务器内部访问平均响应时间25ms。🌿🌿🌿

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
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| scope [optional] | str | 魔法类型 `global` `public` `private` `all`<br>默认值 `all`|
| maximum [optional]| int | 返回数据条数<br>默认值 `10`<br>最大 `30` |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/3.png)

****

## 日志
`GET` `https://u2.kysdm.com/api/v1/log`

|  参数   | 数据类型  | 说明  |
|  ----  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| maximum [optional]| int | 返回数据条数<br>默认值 `10`<br>最大 `30` |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/4.png)

****

## 聊天
`GET` `https://u2.kysdm.com/api/v1/msg`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| maximum [optional]| int | 返回数据条数<br>默认值 `10`<br>最大 `50` |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/5.png)

****

## 历史修改
> 5月份u2改了code，忘记更新代码，到6月20日这段时间的bbcode都没换行符。  
> 6月20日前仅通过候选或者直接上传时会写入种子信息，其余修改记录里为空。

`GET` `https://u2.kysdm.com/api/v1/history`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| torrent  | int | 种子id |
| token  | str | 鉴权中返回的值 |
| maximum [optional]| int | 返回数据条数<br>默认值 `3`<br>最大 `50` |

> 弃用 diff  
> 改为 history

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/6.png)

****

## 新种子 (伪RSS)
> 可能你会看到秒发秒删的种子 (丢人操作)

`GET` `https://u2.kysdm.com/api/v1/torrent`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| scope [unused] | str | 种子类型 `new`<br>默认值 `new`|
| maximum [optional]| int | 返回数据条数<br>默认值 `10`<br>最大 `100` |
| simple [optional]| int | `0` 完整信息(包含种子描述等信息)[默认]<br>`1` 简略信息(不包含种子描述等信息) |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/7.png)

****

## 候选
> 此方法返回的种子体积并不精确 <end值为0的种子> (候选区需要 MOD 才有权限下载种子文件)  
> 此方法会返回被拒绝的候选 (暂时不考虑抓取候选状态)

`GET` `https://u2.kysdm.com/api/v1/offer`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| maximum [optional]| int | 返回数据条数<br>默认值 `10`<br>最大 `30` |
| simple [optional]| int | `0` 完整信息(包含种子描述等信息)[默认]<br>`1` 简略信息(不包含种子描述等信息) |
| end [optional]| int | `0` 不包含已经通过候选的种子[默认]<br>`1` 包含已经通过候选的种子 |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/10.png)

****

## 邀请树
> 单用户

`GET` `https://u2.kysdm.com/api/v1/user/`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| user | int | 被查询用户的id |
| direction [optional] | int |  `0` 向上查询邀请树(不包含分支)[默认]<br>`1` 向下查询邀请树(不包含分支) |
| simple [optional]| int | `0` 完整信息(包含改名记录)[默认]<br>`1` 简略信息(不包含改名记录) |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/8.png)

> 多用户

`POST` `https://u2.kysdm.com/api/v1/user/`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| user | str | 被查询用户的id组 (单次最大100个<超长截断>) |
| direction [optional] | int |  `0` 向上查询邀请树(不包含分支)[默认]<br>`1` 向下查询邀请树(不包含分支) |
| simple [optional]| int | `0` 完整信息(包含改名记录)[默认]<br>`1` 简略信息(不包含改名记录) |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/9.png)

> 邀请树

`GET` `https://u2.kysdm.com/api/v1/invite/`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| user | int | 被查询用户的id |
| simple [optional]| int | `0` 完整信息(包含改名记录)[默认]<br>`1` 简略信息(不包含改名记录) |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/10.png)
