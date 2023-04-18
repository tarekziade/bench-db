# 1 Million ids
import os
import tkrzw
import hashlib
import time
from datetime import datetime, timezone
import timeit


DB_NAME = "casket.tkh"

if os.path.exists(DB_NAME):
    print(f"DB exists, delete {DB_NAME} to recreate")
else:
    dbm = tkrzw.DBM()
    dbm.Open(
        DB_NAME, True, truncate=True, num_buckets=100000, update_mode="UPDATE_APPENDING"
    )

    s = time.time()
    print("Adding 1 million ids and timestamps")
    max_len = 0

    for i in range(1000):
        when = str(datetime.now(timezone.utc).timestamp())
        for y in range(1000):
            id = f"{i}000a{y}"
            if len(id) > max_len:
                max_len = len(id)
            dbm[id] = str(when)

    print(f"took {time.time() - s} seconds")
    print(f"Final count {dbm.Count()}")
    print(f"max id len is {max_len}")
    dbm.Close()


dbm = tkrzw.DBM()
dbm.Open(DB_NAME, True, truncate=False, num_buckets=100)
print("Looking for one id")


def _lookup():
    assert dbm["23000a34"] is not None


print(f"{timeit.timeit(_lookup, number=1000)} seconds")
dbm.Close()

print(f"Size of DB on disk is {os.stat(DB_NAME).st_size / 1024. / 1024.} MiB")
