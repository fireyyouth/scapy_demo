# syn flood test

## before running
```
# run a server
python3 -m http.server 8081
# prevent kernel RST
iptables -A OUTPUT -s 127.0.0.1 -p tcp -m tcp --tcp-flags RST RST -j DROP
```

## running
```
python3 syn_flood_test.py 8081
```

## show socket stat
```
ss -4 state syn-recv
```

## expected tcpdump output
```
$ sudo tcpdump -i lo port 8081 -nn
04:36:46.892390 IP 127.0.0.1.1500 > 127.0.0.1.8081: Flags [S], seq 1000, win 8192, length 0
04:36:46.892492 IP 127.0.0.1.8081 > 127.0.0.1.1500: Flags [S.], seq 3966369511, ack 1001, win 65495, options [mss 65495], length 0
04:36:47.941655 IP 127.0.0.1.8081 > 127.0.0.1.1500: Flags [S.], seq 3966369511, ack 1001, win 65495, options [mss 65495], length 0
04:36:50.003382 IP 127.0.0.1.8081 > 127.0.0.1.1500: Flags [S.], seq 3966369511, ack 1001, win 65495, options [mss 65495], length 0
04:36:54.019619 IP 127.0.0.1.8081 > 127.0.0.1.1500: Flags [S.], seq 3966369511, ack 1001, win 65495, options [mss 65495], length 0
04:37:02.218773 IP 127.0.0.1.8081 > 127.0.0.1.1500: Flags [S.], seq 3966369511, ack 1001, win 65495, options [mss 65495], length 0
04:37:18.338805 IP 127.0.0.1.8081 > 127.0.0.1.1500: Flags [S.], seq 3966369511, ack 1001, win 65495, options [mss 65495], length 0
```
