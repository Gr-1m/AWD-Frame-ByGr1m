

### 框架安装

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirment.txt
or
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirment.txt
```



### 命令Tips

```
init:初始化（目前还待完善）

show: 展示全局变量，提供配置，也可以根据需求查看变量

set：设置全局变量，
unset：取消设置全局变量的值


```



### 配置模块（Configs/edit_config.py）

```python
# 凡是带有ReplaceStr字样的变量都是后续在函数中需要替换的字符串，（建议避开命名）
# 缩写：Ey -> Enemy
# AliveStr是探测自己是否存活的字符串，请手动添加到首页的文件中
# 例如php请添加 echo "<!--AliveStr-->";

# About Game Info
TeamReplaceStr = 'XXXTrs'
MyHost = "192.168.122.231"
EyHosts = f"192.168.122.{TeamReplaceStr}"
Token = "test_token1"

API_URL = 'http://kaming/awduse/submit.php'
API_token = 'token'
API_flag = 'flag'
API_method = 'GET'
# SubmitAPI = [URL, token的参数, flag的参数, method], GET: http://????.com/xxx/submit.php?token=111Token1111&flag=Cflag{xxx}
SubmitAPI = [API_URL, API_token, API_flag, API_method]

# About Game Time Info
GSTime = "2023-11-13 20:00:00"  # Game Start Time
RTime = 300  # Round Time
RCount = 20  # Round Count
DFTime = 1800  # Defensive time

# About MY Server Info
MyHostSSH = f'ssh://msfadmin:msfadmin@{MyHost}:222/xx'
MyHostSQL = f'mysql://cms:qwerty;@{MyHost}:3306/xx'

# MyHost.split(':')
# [0] protocol [1] //username [2]password@MyhostIP [3]port/xx


# About MyPage Alive Remind
AliveStr = 'flag{bbcce4088-e7525797-BY_Gr%1m-c716e82}'
AliveTime = 10

```



### 攻击模块（module/Attack.py）

```python
# 全局变量：
# About Flag
Flags 									# 存放flag的变量，请勿修改
FlagLen = 41
FlagPath = '/flag'
FlagRegular = r'flag{\w{32}}'

# Payload INFO
RceRelpaceStr = 'XXXRCEstr'				# RCE 替换字符串，请避开命名
Payloads = [f'/g.php?s=system({RceRelpaceStr});',]	# set add添加Payloads

# Backdoor INFO
BDNameR = "HM_NAME_REPLACE"
BDDataR = "WAIT_FOR_REPLACE"
BDpass = 'x2aom1ng_20231114'

# Flag INFO

```



### 防御模块（module/Defense.py）

```

```





#### 开发环境：

> OS：Linux  6.5.0-kali2-amd64 
> #1 SMP PREEMPT_DYNAMIC Debian 6.5.3-1kali2 (2023-10-03) x86_64 GNU/Linux
>
> Python 3.11