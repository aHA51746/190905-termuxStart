# 190905-termuxStart
设置termux启动项
最近得到个华为p8老手机，想拿来跑服务，玩了一段时间发现并没有好的开机启动方案...
一开始我是把启动项写入bashrc，后来发现termux只支持单用户，每次ssh连接所有服务均遍历启动，后来通过判断ssh进程是否运行启动其他服务。