# -*- coding: utf-8

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr, IPAddr
import pox.lib.packet as pkt
from collections import namedtuple
import os
import csv

log = core.getLogger()
policyFile = "/home/myp4/P4/pox/pox/misc/firewallpolicies.csv"

class Firewall (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.info("启动防火墙模块")
        # 防火墙规则表
        self.firewall = {}

    def sendRule (self, src, dst, duration = 0):
        """
        删除此数据包,并选择性安装一个流
	在一段时间内继续丢弃类似的数据包
        """
        if not isinstance(duration, tuple):
            duration = (duration,duration)
        msg = of.ofp_flow_mod()
	match = of.ofp_match(dl_type = 0x800,
			     nw_proto = pkt.ipv4.ICMP_PROTOCOL)
        match.nw_src = IPAddr(src)
        match.nw_dst = IPAddr(dst)
        msg.match = match
        msg.idle_timeout = duration[0]
        msg.hard_timeout = duration[1]
        msg.priority = 10
        self.connection.send(msg)

    # 向防火墙规则表中添加规则
    def AddRule (self, src=0, dst=0, value=True):
        if (src, dst) in self.firewall:
            log.info("规则已存在 drop: src %s - dst %s", src, dst)
        else:
            log.info("添加规则 drop: src %s - dst %s", src, dst)
            self.firewall[(src, dst)]=value
            self.sendRule(src, dst, 10000)

    # 从防火墙规则表中删除规则
    def DeleteRule (self, src=0, dst=0):
        try:
            del self.firewall[(src, dst)]
            sendRule(src, dst, 0)
            log.info("删除规则 drop: src %s - dst %s", src, dst)
        except KeyError:
            log.error("无此规则 drop src %s - dst %s", src, dst)

    def _handle_ConnectionUp (self, event):
        ''' 在此处添加逻辑 '''
        self.connection = event.connection

        ifile  = open(policyFile, "rb")
        reader = csv.reader(ifile)
        rownum = 0
        for row in reader:
            # 保存规则
            if rownum == 0:
                header = row
            else:
                colnum = 0
                for col in row:
                    #print '%-8s: %s' % (header[colnum], col)
                    colnum += 1
                self.AddRule(row[1], row[2])
            rownum += 1
        ifile.close()

        log.info("防火墙规则安装在 %s", dpidToStr(event.dpid))

def launch ():
    '''
    启动防火墙模块
    '''
    core.registerNew(Firewall)