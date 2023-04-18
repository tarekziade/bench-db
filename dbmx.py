# 1 Million ids
import os
import tkrzw
import hashlib
import time
from datetime import datetime, timezone
import timeit


DB_NAME = "casket.tkh"
NUM_BUCKETS = 1000000 * 2

if os.path.exists(DB_NAME):
    print(f"DB exists, delete {DB_NAME} to recreate")
else:
    s = time.time()
    print("Adding 1 million ids and timestamps")
    max_len = 0
    dbm = tkrzw.DBM()
    dbm.Open(
        DB_NAME,
        True,
        truncate=False,
        num_buckets=NUM_BUCKETS,
        update_mode="UPDATE_APPENDING",
        offset_width=5,
        align_pow=4,
    )


    x = 0
    for i in range(1000):
        when = str(datetime.now(timezone.utc).timestamp())
        for y in range(1000):
            id = f"{i}000a{y}"
            if len(id) > max_len:
                max_len = len(id)
            dbm[id] = str(when)
            x += 1
            if x > 2500:
                dbm.Synchronize(True)
                x = 0

    dbm.Close()
    dbm = tkrzw.DBM()
    dbm.Open(DB_NAME, False)
    print(f"took {time.time() - s} seconds")
    print(f"Final count {dbm.Count()}")
    print(f"max id len is {max_len}")
    dbm.Close()


dbm = tkrzw.DBM()
dbm.Open(DB_NAME, False)

print("Looking for one id")


def _lookup():
    assert dbm["23000a34"] is not None


print(f"{timeit.timeit(_lookup, number=1000)} seconds")
dbm.Close()

print(f"Size of DB on disk is {os.stat(DB_NAME).st_size / 1024. / 1024.} MiB")
