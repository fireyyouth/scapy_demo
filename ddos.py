from scapy.all import * # The One and Only Scapy

conf.L3socket=L3RawSocket
ip = IP(dst='localhost')

syn = ip / TCP(sport=1500, dport=8888, flags="S", seq=1000)

syn_ack = sr1(syn, timeout=1)

input('press to ack')

ack = ip / TCP(sport=1500, dport=8888, flags="A", seq=syn_ack.ack, ack=syn_ack.seq + 1)

print(ack)

send(ack)

input('press to quit')
