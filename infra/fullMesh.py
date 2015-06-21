# -*- coding: utf-8 -*-
from mininet.net import Mininet
from mininet.node import RemoteController, CPULimitedHost
from mininet.log import info
from mininet.link import TCLink
#from FloodLightClient import StaticFlowPusher


def multiPath():
    net = Mininet(controller=RemoteController, host=CPULimitedHost, link=TCLink)

    info('*** Adding controller\n')
    net.addController('c0',
        controller=RemoteController,
        ip='127.0.0.1',
        port=6653
    )

    info('*** Adding hosts\n')
    leftHost1 = net.addHost('h1')
    leftHost2 = net.addHost('h2')
    rightHost1 = net.addHost('h3')
    rightHost2 = net.addHost('h4')

    info('*** Adding switch\n')
    intSwitch1 = net.addSwitch('s1')
    intSwitch2 = net.addSwitch('s2')
    intSwitch3 = net.addSwitch('s3')
    intSwitch4 = net.addSwitch('s4')
    intSwitch5 = net.addSwitch('s5')
    intSwitch6 = net.addSwitch('s6')

    info('*** Creating border links\n')
    net.addLink(leftHost1, intSwitch1)
    net.addLink(leftHost2, intSwitch1)
    net.addLink(rightHost1, intSwitch6)
    net.addLink(rightHost2, intSwitch6)

    info('*** Creating Full Mesh\n')
    switchList = (intSwitch1, intSwitch2, intSwitch3, intSwitch4,
                  intSwitch5, intSwitch6)
    for index in range(0, len(switchList)):
        for index2 in range(index + 1, len(switchList)):
            net.addLink(
                switchList[index],
                switchList[index2],
                bw=1
            )