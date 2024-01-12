# syn flood test

## before running
```
iptables -A OUTPUT -s 127.0.0.1 -p tcp -m tcp --tcp-flags RST RST -j DROP
```

## running
```
python3 syn_flood_demo.py
```

## monitor socket stat
```
ss -4 state syn-recv
```
