# Disk-based id lookup

Store 1 Million string ids on disk and provide a fast id lookup, without loading
everything in memory.

Implementations:

- dbm (stdlib)
- sqlite3 (stdlib)
- pysos -- https://github.com/dagnelies/pysos
- tkrzw -- https://dbmx.net/tkrzw/api-python

TLDR;

- dbm has faster lookups! 
- sqlite3 is smaller on disk.
- tkrzw looks promising -- needs tweaking


## dbm bench

Maximum RSS: 11MiB


```sh
Adding 1 million ids and timestamps
took 3.8714396953582764 seconds
Final count 1000000
max id len is 10
Looking for one id
0.00015072201495058835 seconds
Size of DB on disk is 95.359375 MiB
```

## sqlite3 bench

Maximum RSS: 13MiB

```sh
Adding 1 million ids and timestamps
took 2.6603636741638184 seconds
Final count 1000000
max id len is 10
Looking for one id
0.012375471997074783 seconds
Size of DB on disk is 34.44921875 MiB
```

## tkrzw benchmark

Maximum RSS: 46MiB

```
Adding 1 million ids and timestamps
took 1.4278862476348877 seconds
Final count 1000000
max id len is 10
Looking for one id
0.0008815110195428133 seconds
Size of DB on disk is 38.49774169921875 MiB
```

## Pysos benchmark

Maximum RSS: 300MiB

```sh
Adding 1 million ids and timestamps
took 15.620530843734741 seconds
Final count 1000000
max id len is 10
Looking for one id
0.0018717409984674305 seconds
```

