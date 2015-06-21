# -*- coding: utf-8 -*-
from mininet.net import Mininet
from mininet.node import RemoteController, CPULimitedHost
from mininet.log import info
from mininet.link import TCLink
#from FloodLightClient import StaticFlowPusher


def fatTree():
    net = Mininet(controller=RemoteController, host=CPULimitedHost, link=TCLink)

    info('*** Adding controller\n')
    net.addController('c0',
        controller=RemoteController,
        ip='127.0.0.1',
        port=6653
    )

    info('*** Adding switch\n')
    s01 = net.addSwitch('s01')
    s02 = net.addSwitch('s02')
    s03 = net.addSwitch('s03')
    s04 = net.addSwitch('s04')
    s11 = net.addSwitch('s11')
    s12 = net.addSwitch('s12')
    s13 = net.addSwitch('s13')
    s14 = net.addSwitch('s14')
    s21 = net.addSwitch('s21')
    s22 = net.addSwitch('s22')
    s23 = net.addSwitch('s23')
    s24 = net.addSwitch('s24')
    s31 = net.addSwitch('s31')
    s32 = net.addSwitch('s32')
    s33 = net.addSwitch('s33')
    s34 = net.addSwitch('s34')
    s41 = net.addSwitch('s41')
    s42 = net.addSwitch('s42')
    s43 = net.addSwitch('s43')
    s44 = net.addSwitch('s44')

    info('*** Setting up Fat Tree Area 1\n')
    net.addLink(s11, s13)
    net.addLink(s11, s14)
    net.addLink(s12, s13)
    net.addLink(s12, s14)
    net.addLink(s11, s01)
    net.addLink(s11, s03)
    net.addLink(s12, s02)
    net.addLink(s12, s04)

    info('*** Setting up Fat Tree Area 2\n')
    net.addLink(s21, s23)
    net.addLink(s21, s24)
    net.addLink(s22, s23)
    net.addLink(s22, s24)
    net.addLink(s21, s01)
    net.addLink(s21, s03)
    net.addLink(s22, s02)
    net.addLink(s22, s04)

    info('*** Setting up Fat Tree Area 3\n')
    net.addLink(s31, s33)
    net.addLink(s31, s34)
    net.addLink(s32, s33)
    net.addLink(s32, s34)
    net.addLink(s31, s01)
    net.addLink(s31, s03)
    net.addLink(s32, s02)
    net.addLink(s32, s04)

    info('*** Setting up Fat Tree Area 4\n')
    net.addLink(s41, s43)
    net.addLink(s41, s44)
    net.addLink(s42, s43)
    net.addLink(s42, s44)
    net.addLink(s41, s01)
    net.addLink(s41, s03)
    net.addLink(s42, s02)
    net.addLink(s42, s04)

    info('*** Adding hosts\n')
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')
    h5 = net.addHost('h5')
    h6 = net.addHost('h6')
    h7 = net.addHost('h7')
    h8 = net.addHost('h8')
    h9 = net.addHost('h9')
    h10 = net.addHost('h10')
    h11 = net.addHost('h11')
    h12 = net.addHost('h12')
    h13 = net.addHost('h13')
    h14 = net.addHost('h14')
    h15 = net.addHost('h15')
    h16 = net.addHost('h16')

    info('*** Setting Up Hosts connections')
    net.addLink(h1, s13)
    net.addLink(h2, s13)
    net.addLink(h3, s14)
    net.addLink(h4, s14)

    net.addLink(h5, s23)
    net.addLink(h6, s23)
    net.addLink(h7, s24)
    net.addLink(h8, s24)

    net.addLink(h9, s33)
    net.addLink(h10, s33)
    net.addLink(h11, s34)
    net.addLink(h12, s34)

    net.addLink(h13, s43)
    net.addLink(h14, s43)
    net.addLink(h15, s44)
    net.addLink(h16, s44)

    return net