# Disk-based id lookup

Store 1 Million string ids on disk and provide a fast id lookup, without loading
everything in memory.

Implementations:

- dbm
- sqlite3
- pysos (https://github.com/dagnelies/pysos)


dbm has faster lookups!

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
took 3.1656839847564697 seconds
Final count 1000000
max id len is 10
Looking for one id
0.012021810980513692 seconds
Size of DB on disk is 54.109375 MiB
```

## Pysis benchmark

Maximum RSS: 300MiB

```sh
Adding 1 million ids and timestamps
took 15.620530843734741 seconds
Final count 1000000
max id len is 10
Looking for one id
0.0018717409984674305 seconds
```

