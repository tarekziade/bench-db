# 1 Million ids
import os
import dbm
import hashlib
import time
from datetime import datetime, timezone
import timeit


DB_NAME = "dbm_store.db"

if os.path.exists(DB_NAME):
    print(f"DB exists, delete {DB_NAME} to recreate")
else:
    with dbm.open("dbm_store", "c") as db:
        s = time.time()
        print("Adding 1 million ids and timestamps")
        max_len = 0

        for i in range(1000):
            when = str(datetime.now(timezone.utc).timestamp())
            for y in range(1000):
                id = f"{i}0000{y}"
                if len(id) > max_len:
                    max_len = len(id)
                db[id] = str(when)
        print(f"took {time.time() - s} seconds")
        print(f"Final count {len(db)}")
        print(f"max id len is {max_len}")


with dbm.open("dbm_store", "c") as db:
    print("Looking for one id")

    def _lookup():
        assert db["23000034"] is not None

    print(f"{timeit.timeit(_lookup, number=1000)} seconds")


print(f"Size of DB on disk is {os.stat(DB_NAME).st_size / 1024. / 1024.} MiB")
