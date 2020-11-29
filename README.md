# SDN-firewall
[使用到的指令介绍](https://www.cnblogs.com/xie37/p/14056239.html)

将 firewall.py 和 firewallpolicies.csv 放入 ~/P4/pox/pox/misc/ 目录下
修改 firewall.py 的 第12行为 firewallpolicies.csv 的路径
我这里是 policyFile = "/home/myp4/P4/pox/pox/misc/firewallpolicies.csv"
运行以下代码
```
cd ~/P4/pox/
./pox.py forwarding.l2_learning openflow.discovery openflow.spanning_tree --no-flood --hold-down pox.misc.firewall
```
将 topology.py 放入 ~/P4/mininet/mininet/ 目录下
```
cd ~/P4/mininet/mininet/
sudo mn --custom topology.py --topo mytopo --mac --controller=remote,ip=127.0.0.1,port=6633
```
待第一个终端将防火墙规则加载完成后,即可 pingall 检验结果
ip_0 与 ip_1 的主机将无法相互到达

[详细信息](https://www.cnblogs.com/xie37/p/14056239.html)
