import logging

def flood_tcpflows(flows: [])
	
	# TODO: make up packets for each flow: some of fields can be generated here or under layer 
	# As there are many packets and many flows, so it makes sense to generate those 
	# meaningless payload in Scapy function right before sending and then discard 
	logging.info("Preparing flow data for flooding ...")
	for f in flows:
		payload = 'AAAAAA' 
		pckt = IP(dst=f[2]) / TCP(dport=f[4], flags=packet_flags) / payload 

	logging.info("Read to flood")
	# TODO: send flows/packets via Scapy 
	# send() or dispatch()


def main():

    input_parser = argparse.ArgumentParser()

    input_parser.add_argument("proto", nargs=1, help="Protocol(UDP or TCP or ICMP)")

    input_parser.add_argument("dst", nargs=1, help="Target IP Address")

    input_parser.add_argument("-src", "--source", type=str, nargs=1, default=DEFAULT_SRC_ADDR,
                              help="Source IP Address(-src rand || -src random for randomly generated IP Addr)")   

    input_parser.add_argument("-f", "--flow", type=int, nargs=1, default=DEFAULT_PACKET_SIZE,
                              help="Number of flows to flood")
    
    # TODO: add other parameters

    # TODO: load variable from arguments above
    num_flows = 5
    dst_addr = '10.0.0.2'
    dport = 1234
    packet_size = 5000
    packet_count = 10
    packet_interval = 0  # if 0 send packet in a non-stop fashion, other wait for 1 millisecond before send next 
    log_path = '/tmp/'

    logfile = log_path+"/flooder.tcp."+'{:%Y-%m-%d_%H:%M:%S}'.format(datetime.datetime.now())+".log"
    logging.basicConfig(filename=logfile, format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %I:%M:%S %p', level=logging.DEBUG)
   
	flows = []
    # TODO IF source address is random generate
    for _ in range(num_flows):
    	src_addr = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    	flows = [(src_addr, sport, dst_addr, dport, packet_size, packet_count, packet_interval)] 
	
	# TODO source address can be loaded from a external file

	# TODO
    flood_tcpflows(flows)

if __name__ == '__main__':
	main()