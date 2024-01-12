from scapy.all import * # The One and Only Scapy
import sys

dport = int(sys.argv[1])

conf.L3socket=L3RawSocket
ip = IP(dst='localhost')

syn = ip / TCP(sport=1500, dport=dport, flags="S", seq=1000)

syn_ack = sr1(syn)
