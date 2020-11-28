from mininet.topo import Topo

class MyTopo( Topo ):
    "我创建的简单拓扑示例"

    def __init__( self ):
        "创建用户定义拓扑"

        # 初始化拓扑
        Topo.__init__( self )

        # 加入主机和交换机
        FirstHost = self.addHost( 'h1' )
        SecondHost = self.addHost( 'h2' )
        ThirdHost = self.addHost( 'h3' )
        FourthHost = self.addHost( 'h4' )
        FifthHost = self.addHost( 'h5' )
        SixthHost = self.addHost( 'h6' )
        firstSwitch = self.addSwitch( 's1' )
        secondSwitch = self.addSwitch( 's2' )
        thirdSwitch = self.addSwitch( 's3' )
        fourthSwitch = self.addSwitch( 's4' )
        fifthSwitch = self.addSwitch( 's5' )
        sixthSwitch = self.addSwitch( 's6' )

        # 添加连接
        self.addLink( firstSwitch, FirstHost )
        self.addLink( secondSwitch, SecondHost )
        self.addLink( thirdSwitch, ThirdHost )
        self.addLink( fourthSwitch, FourthHost )
        self.addLink( fifthSwitch, FifthHost )
        self.addLink( sixthSwitch, SixthHost )
        self.addLink( firstSwitch, secondSwitch  )
        self.addLink( secondSwitch, thirdSwitch )
        self.addLink( thirdSwitch, sixthSwitch )
        self.addLink( fourthSwitch, sixthSwitch )
        self.addLink( fourthSwitch, thirdSwitch )
        self.addLink( firstSwitch, fourthSwitch )
        self.addLink( firstSwitch, fifthSwitch )
        self.addLink( secondSwitch, fifthSwitch )
        self.addLink( secondSwitch, sixthSwitch )
        self.addLink( fifthSwitch, thirdSwitch )

topos = { 'mytopo': ( lambda: MyTopo() ) }
