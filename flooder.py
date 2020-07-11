#! /usr/bin/env python
# Base for the tool borowed from: https://github.com/celefthe/udp-flooder
import argparse
import packetdispatch
import time
import datetime

# Set default values
DEFAULT_SRC_ADDR = "127.0.0.1"
DEFAULT_PACKET_SIZE = 1500
DEFAULT_CHKSUM = 0
DEFAULT_PORT = 53
DEFAULT_REQUEST_NUM = -1
DEFAULT_TCP_FLAG = "S"
# Not implemented but would be cool if it gets implemented
# The idea: Give option for user to specify ICMP type and
# code and allso add a flag for random ICMP generation Right now, there are .csv file in a folder icmp_resources not
# shared on git which contain all available options Read from them and generate user specific types or generate
# random packets by reading from them DEFAULT_ICMP_TYPE=8 #echo request DEFAULT_ICMP_CODE=0
DEFAULT_ICMP_TYPE_FLAG = 0
DEFAULT_PACKET_COUNT = 500
DEFAULT_OUTPUTPATH = "."


def main():
    # First parse the command line arguments
    input_parser = argparse.ArgumentParser()

    input_parser.add_argument("proto", nargs=1, help="Protocol(UDP or TCP or ICMP)")

    input_parser.add_argument("dst", nargs=1, help="Target IP Address")

    input_parser.add_argument("-src", "--source", type=str, nargs=1, default=DEFAULT_SRC_ADDR,
                              help="Source IP Address(-src rand || -src random for randomly generated IP Addr)")

    input_parser.add_argument("-p", "--port", type=int, nargs=1, default=DEFAULT_PORT,
                              help="Target port (999999 for randomly generated port)")

    input_parser.add_argument("-s", "--size", type=int, nargs=1, default=DEFAULT_PACKET_SIZE,
                              help="Packet size (999999 for randomly generated payload")

    input_parser.add_argument("--packetcount", type=int, nargs=1, default=DEFAULT_PACKET_COUNT,
                              help="Number of packets after which a timestamp is printed")

    # TCP FLAG
    input_parser.add_argument("-f", "--flag", type=str, nargs=1, default=DEFAULT_TCP_FLAG,
                              help="Set a TCP flag. Options: S(YN), A(CK), F(IN), U(RG),"
                                   "P(SH), R(ST),E(CE),C(WR),N(S)[NS is an experimental flag,see RFC 3540]")
    # ICMP TYPE -not implemented-
    # input_parser.add_argument("-t", "--type", type=int, nargs=1,default=DEFAULT_ICMP_CODE, help="Specify ICMP
    # packet type. ICMP TYPES and CODES: https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml")

    # ICMP CODE -not implemented-
    # input_parser.add_argument("-c", "--code", type=int, nargs=1,default=DEFAULT_ICMP_CODE, help="Specify ICMP
    # packet type. ICMP TYPES and CODES: https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml")

    # ICMP RAND TYPE & CODE
    input_parser.add_argument("-rtc", "--randomtypecode", type=int, nargs=1, default=DEFAULT_ICMP_TYPE_FLAG,
                              help="Randomly generates ICMP packets of different type."
                                   "1 for ON, 0 for OFF. ICMP TYPES and CODES: "
                                   "https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml")
    input_parser.add_argument("-req", "--requests", type=int, nargs=1, default=DEFAULT_REQUEST_NUM,
                              help="Number of requests")
    input_parser.add_argument("-r", "--rate", type=float, nargs=1, default=DEFAULT_REQUEST_NUM,
                              help="packet sending rate(Can only slow down the rate [e.g 0.5 halfs sending rate])")

    input_parser.add_argument("-o", "--output", type=str, nargs=1, default=DEFAULT_OUTPUTPATH,
                              help="Specifies the path where log file will be generated."
                                   "Default value uses the current directory")
    # pak = IP(dst=target, src = "100.99.98.97", ttl=ttl, flags="DF", id=id, len=1200, chksum = 0)/
    # TCP(flags="S", sport=sport, dport=int(dport), options=[('Timestamp',(0,0))], chksum = 0)

    args = input_parser.parse_args()
    # protocol
    protocol = str(args.proto).strip("[']")
    # IP
    dstAddr = str(args.dst).strip("[']")
    srcAddr = str(args.source).strip("[']")
    port = str(args.port).strip("[']")
    # UDP
    size = str(args.size).strip("[']")
    # TCP
    flags = str(args.flag).strip("[']")
    # ICMP
    icmp_rand = str(args.randomtypecode).strip("[']")
    # number of requests
    requests = str(args.requests).strip("[']")
    rate = float(args.rate)
    # not implemented yet...---^

    # packet count timestamp
    packetcount = str(args.packetcount).strip("[']")

    # logoutput location
    logpath = str(args.output).strip("[']")
    logpath = logpath+"/flooder"+'{:%Y-%m-%d_%H:%M:%S}'.format(datetime.datetime.now())+".log"
    # Display parameters to user
    print("Protocol: " + protocol)
    print("Target IP: " + dstAddr)
    print("Target Port: " + port)
    print("Packet Size: " + size)
    if requests != '-1':
        print("Number of Requests: " + requests)

    print("\nSending packets...")

    try:
        if (protocol == "UDP"):
            packetdispatch.sendUDPpackets(srcAddr, dstAddr, port, requests, size, packetcount, logpath)
        elif (protocol == "TCP"):
            packetdispatch.sendTCPpackets(srcAddr, dstAddr, port, requests, size, flags, packetcount, logpath)
        elif (protocol == "ICMP"):
            packetdispatch.sendICMPpackets(srcAddr, dstAddr, requests, size, icmp_rand, packetcount, logpath)
        else:
            print("Wrong/Unknown Protocol.")
    except KeyboardInterrupt:
        print('\nProcess cancelled by user')
    # except:
    #    print('\nError! Check parameters')
    # time_elapsed = time.clock() - start_time

    print("\nDone!")
    # print("Time elapsed: " + str(time_elapsed) + " seconds")


main()
