# Disk-based id lookup

Store 1 Million string ids on disk and provide a fast id lookup, without loading
everything in memory.

Implementations:

- dbm - ndbm (stdlib)
- sqlite3 (stdlib)
- pysos -- https://github.com/dagnelies/pysos
- tkrzw -- https://dbmx.net/tkrzw/api-python
- ldbm -- https://github.com/Dobatymo/lmdb-python-dbm


TLDR;

- dbm has faster lookups!
- sqlite3 is smaller on disk
- tkrzw looks promising -- needs tweaking


## dbm (ndbm)

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

## sqlite3

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

## tkrzw

Maximum RSS: 19MiB

```
Adding 1 million ids and timestamps
took 10.578145027160645 seconds
Final count 1000000
max id len is 10
Looking for one id
0.00043975599692203104 seconds
Size of DB on disk is 55.308563232421875 MiB
```

## Pysos

Maximum RSS: 300MiB

```sh
Adding 1 million ids and timestamps
took 15.620530843734741 seconds
Final count 1000000
max id len is 10
Looking for one id
0.0018717409984674305 seconds
```

## LDBM

Maximum RSS: 19MiB

```sh
Adding 1 million ids and timestamps
took 1.4407689571380615 seconds
Final count 1000000
max id len is 10
Looking for one id
0.000999119016341865 seconds
Size of DB on disk is 81MiB
```

