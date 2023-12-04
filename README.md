

### 框架安装

```bash
git clone https://github.com/Gr-1m/AWD-Frame-ByGr1m.git
cd AWD-Frame-ByGr1m

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirment.txt
or
python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirment.txt

python3 StartMain.py [Mode]
```



### 命令Tips

```
init:初始化（目前还待完善）

show: 展示全局变量，提供配置，也可以根据需求查看变量

set：设置全局变量，
unset：取消设置全局变量的值

ATTACK:
    getflag: 执行获取flag (dev: 反弹flag功能正测试阶段)
    submit:  提交flag 选项 auto自动提交，无选项则手动提交
    shellin: 目录感染不死马注入

DEFENSE:
    getbackup:  通过ssh连接打包网站源码
    checkme:    检查自己的host是否状态Alive

辅助模块：
    scan:       扫描主机存货情况
    timedown:   用于查看提示比赛进程时间
    clear:      请屏，与shell中功能相同
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
# About MyPage Alive Remind
AliveStr = 'flag{bbcce4088-e7525797-BY_Gr%1m-c716e82}'
AliveTime = 10
```





#### 开发环境：

> OS：Linux  6.5.0-kali3-amd64 
> #1 SMP PREEMPT_DYNAMIC Debian 6.5.6-1kali1 (2023-10-09) x86_64 GNU/Linux
>
> Python 3.11
> 
> Pycharm2023.1.3