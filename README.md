# U2-API

注意: 当您失去U2的访问权限时，您也会立即失去此API的访问权限。  
token 至多生效7个，每个 token 有效期为45天，每次成功请求 token 自动续期 。  
更新日志：https://u2.dmhy.org/forums.php?action=viewtopic&forumid=7&topicid=13483


<a href="https://u2.dmhy.org/"><img src="https://u2.dmhy.org/pic/logo.png" width="120" alt="U2分享園@動漫花園" title="U2分享園@動漫花園 - 网站只是一个中介|分享靠的是大家"></a>
<a href="https://stats.uptimerobot.com/EBZ2lIljZy"><img src="https://stats.uptimerobot.com/assets/img/uptimerobot-logo-dark.svg" width="120" /></a>

## 鉴权
> 自动化鉴权 `https://greasyfork.org/zh-CN/scripts/428545`  

`POST` `https://u2.kysdm.com/api/v1/token`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | :--:  |
| uid  | int | u2账户id |

请将返回 key 值写入[个人说明](https://u2.dmhy.org/usercp.php?action=personal)中。

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/1.png)

****

`POST` `https://u2.kysdm.com/api/v1/token`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| key | str | 上一步操作返回的 key 值 |

将返回 token，token 请妥善保管。  
~~此 token 暂无有效期。~~ token 闲置超过60天自动失效。  
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
| maximum [optional]| int | 返回数据条数<br>默认值 `10`<br>最大 `60` |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/3.png)

****

## 魔法叠加
> 结果缓存 20s  
> 返回的数据`get_time`时间无法满足需求时，再使用`skip_cache`参数跳过缓存进行请求。

> 为兼容旧结构，保留`ratio`key  
> `ratio`同`public_ratio`

`GET` `https://u2.kysdm.com/api/v1/promotion_super`

|  参数   | 数据类型  | 说明  |
|  ----  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| torrent_id | int | 种子ID |
| valid_uid [optional] | int | 筛选对此用户生效的魔法(包含私有魔法)<br>默认为请求者的UID |
| skip_cache [optional] | int | `0` 正常请求[默认]<br>`1` 跳过缓存请求 |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/17.png)

****

## 特定种子当前有效魔法
> 失效的魔法没什么用，就不返回了。

`GET` `https://u2.kysdm.com/api/v1/promotion_specific`

|  参数   | 数据类型  | 说明  |
|  ----  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| torrent_id | int | 种子ID |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/20.png)

****

## 按种子体积排序

`GET` `https://u2.kysdm.com/api/v1/sort_torrents_size`

|  参数   | 数据类型  | 说明  |
|  ----  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| offset [optional]| int | 数据单次返回10条，通过偏移值查询剩余数据。<br>默认值 `0` |
| sort [optional]| int | 排序方向<br>`0` 从小到大[默认]<br>`1` 从大到小 |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/22.png)

****

## 日志
`GET` `https://u2.kysdm.com/api/v1/log`

|  参数   | 数据类型  | 说明  |
|  ----  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| maximum [optional]| int | 返回数据条数<br>默认值 `10`<br>最大 `60` |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/4.png)

****

## 聊天
`GET` `https://u2.kysdm.com/api/v1/msg`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| maximum [optional]| int | 返回数据条数<br>默认值 `10`<br>最大 `100` |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/5.png)

****

## 历史修改
> 5月份u2改了code，忘记更新代码，到6月20日这段时间的bbcode都没换行符。  
> 6月20日前仅通过候选或者直接上传时会写入种子信息，其余修改记录里为空。

`GET` `https://u2.kysdm.com/api/v1/history`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| torrent_id  | int | 种子id |
| hash  | int | 种子hash |
| maximum [optional]| int | 返回数据条数<br>默认值 `3`<br>最大 `100` |

> 弃用 diff 改为 history  

> `torrent_id` 和 `hash` 并存时，将抛弃 `hash`。  
> 注：~~在候选区的种子，如果种子文件过大，API 会丢失种子文件相关信息 (即通过 `hash` 会查询不到信息,但 `torrent_id` 可以)。~~　　从 2024.4.16 开始此问题不再出现

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/6.png)

****

## 种子当前信息
> ~~注：在候选区的种子，如果种子文件过大，API 会丢失种子文件相关信息 (即通过 `hash` 会查询不到信息,但 `torrent_id` 可以)。~~  
> 注：只包含正常状态的种子，即不包含被删除被屏蔽的种子。

`GET` `https://u2.kysdm.com/api/v1/torrent_info`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| torrent_id  | int | 种子id |
| hash  | str | 种子hash |


> `torrent_id` 和 `hash` 并存时，将抛弃 `hash`。  


![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/23.png)


`POST` `https://u2.kysdm.com/api/v1/torrents_info/`
> 注：此方法只返回基础信息，不包含种子结构和种子简介。

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| torrent_id  | str | 种子id组 (单次最大100个<超长截断>) |
| hash  | str | 种子hash组 (单次最大100个<超长截断>) |


> `torrent_id` 和 `hash` 并存时，将抛弃 `hash`。  


![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/26.png)

****

## 新种子

`GET` `https://u2.kysdm.com/api/v1/torrent`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| scope [unused] | str | 种子类型 `new`<br>默认值 `new`|
| maximum [optional]| int | 返回数据条数<br>默认值 `10`<br>最大 `100` |
| simple [optional]| int | `0` 完整信息(包含种子描述等信息)<br>`1` 简略信息(不包含种子文件树结构)[默认]<br>`2` 极简信息(不包含种子描述等信息) |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/7.png)

****

## 特定做种人数
> 结果缓存 300s  

`GET` `https://u2.kysdm.com/api/v1/torrent_low_seed`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| minseeder [optional] | int | 最小做种人数<br>默认值 `1`|
| maxseeder [optional] | int | 最大做种人数<br>默认值 `1`|
| maximum [optional]| int | 返回数据条数<br>默认值 `10`<br>最大 `10000` |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/19.png)

****

## 候选

`GET` `https://u2.kysdm.com/api/v1/offer`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| maximum [optional]| int | 返回数据条数<br>默认值 `10`<br>最大 `60` |
| simple [optional]| int | `0` 完整信息(包含种子描述等信息)<br>`1` 简略信息(不包含种子文件树结构)[默认]<br>`2` 极简信息(不包含种子描述等信息) |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/11.png)

****

## 下载列表
> 结果缓存 600s  
> 请勿滥用此方法

> 一个周期(60s)内至多响应6个请求

`GET` `https://u2.kysdm.com/api/v1/torrent_peer`

|  参数   | 数据类型  | 说明  |
|  ----  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| torrent_id | int | 种子ID |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/18.png)

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

> 在线查询 `https://u2invitetree.kysdm.workers.dev/`  

`GET` `https://u2.kysdm.com/api/v1/invite/`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| user | int | 被查询用户的id |
| simple [optional]| int | `0` 完整信息(包含改名记录)[默认]<br>`1` 简略信息(不包含改名记录) |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/10.png)

****

## 邀请价格

`GET` `https://u2.kysdm.com/api/v1/invite_uc`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| maximum [optional]| int | 返回数据条数<br>默认值 `50`<br>最大 `5000` |


![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/12.png)

****

## 版本库
> U2开发日志

`GET` `https://u2.kysdm.com/api/v1/repository`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| maximum [optional]| int | 返回数据条数<br>默认值 `3`<br>最大 `15` |


![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/13.png)

****

## 首页公告
> U2公告

`GET` `https://u2.kysdm.com/api/v1/announcement`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| maximum [optional]| int | 返回数据条数<br>默认值 `3`<br>最大 `10` |


![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/14.png)

****

## 评论
> 较高频率抓取  (前3页新种子 / 候选区 / 论坛第一页帖子)  
> 极低频率抓取  (除较高频率抓取的)  
> 不实时抓取用户编辑操作，仅当帖子/种子出现新评论后，才抓取编辑操作。 (编辑操作只有进入帖子/种子后才能看到，又没有 API 可以 PY，要实时抓取，就要频繁的请求。)  

> 注：评论中的电子邮箱经过脱敏处理

> 最近的评论

`GET` `https://u2.kysdm.com/api/v1/comment`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| maximum [optional]| int | 返回数据条数<br>默认值 `3`<br>最大 `30` |
| type [optional]| str | `forum` 论坛评论[默认]<br>`torrent` 种子评论 |


![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/15.png)

> 通过唯一标识符精确查找

`POST` `https://u2.kysdm.com/api/v1/comment`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| topicid | str | 论坛帖子ID (单次最大15个<超长截断>) |
| pid | str | 论坛楼层ID (单次最大30个<超长截断>) |
| torrent_id | str | 种子ID (单次最大15个<超长截断>) |
| cid | str | 种子楼层ID (单次最大30个<超长截断>) |
| type [optional]| str | `forum` 论坛评论[默认]<br>`torrent` 种子评论 |

> `topicid` 和 `pid` 并存时，将抛弃 `topicid`。  
> `torrent_id` 和 `cid` 并存时，将抛弃 `torrent_id`。  
> `type` 确定唯一标识符类型

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/16.png)


****

## 种子根目录名反查信息

```
模糊搜索使用示例
>> '%ababcc%' 可匹配 "__abcabc__"
>> 'abcabc%' 可匹配 "abcabc__"
>> '%abcabc' 可匹配 "__abcabc"
```

`POST` `https://u2.kysdm.com/api/v1/search_torrent_name/`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| torrent_name | str | 种子根目录名 |
| offset [optional]| int | 数据单次返回5条，通过偏移值查询剩余数据。<br>默认值 `0` |
| fuzzy_search [optional]| int | 模糊搜索 <启用时`torrent_name`字符长度不得小于6><br>`0` 关闭[默认]<br>`1` 打开 |


![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/21.png)


****

## 关键词搜索评论

```
论坛的搜索先摸了，反正U2就有
```

`POST` `https://u2.kysdm.com/api/v1/search_comment/`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| keywords | list | 关键词<br>`注: 当关键词只有一个时，此关键词长度不应小于2。` |
| desired_user | int | 发帖人uid<br>`注: 将无法搜索匿名帖子` |
| offset [optional]| int | 数据单次返回50条，通过偏移值查询剩余数据。<br>默认值 `0` |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/24.png)


****

## SHA256值查询种子文件路径

```
现阶段数据不足以支撑这个功能
```

`GET` `https://u2.kysdm.com/api/v1/filehash/`

|  参数   | 数据类型  | 说明  |
|  :--:  | :--:  | ----  |
| uid  | int | u2账户id |
| token  | str | 鉴权中返回的值 |
| filehash | str | 文件的SHA256值 |

![](https://raw.githubusercontent.com/kysdm/u2_api/main/img/25.png)
