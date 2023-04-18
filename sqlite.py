# 1 Million ids
import os
import sqlite3
import hashlib
import time
from datetime import datetime, timezone
import timeit


class ElasticIndexIds:
    def __init__(self, path):
        self.path = path
        self._con = sqlite3.connect(path)
        self.cur = self._con.cursor()
        self.cur.execute(
            """\
                CREATE TABLE IF NOT EXISTS elastic_id(
                    doc_id text primary key,
                    ts TEXT
                ) WITHOUT ROWID;
        """
        )

    def count(self):
        res = self.cur.execute("SELECT COUNT(*) FROM elastic_id")
        return res.fetchone()[0]

    def add_docs(self, docs):
        self.cur.executemany(f"INSERT OR REPLACE INTO elastic_id values (?, ?)", docs)
        self._con.commit()

    def find(self, doc_id):
        res = self.cur.execute(f"SELECT ts FROM elastic_id where doc_id='{doc_id}'")
        return res.fetchone()


DB_NAME = "sqlite_store.db"

if os.path.exists(DB_NAME):
    print(f"DB exists, delete {DB_NAME} to recreate")
else:
    d = ElasticIndexIds(DB_NAME)

    max_len = 0
    s = time.time()
    print("Adding 1 million ids and timestamps")

    for i in range(1000):
        when = str(datetime.now(timezone.utc).timestamp())
        docs = []
        for y in range(1000):
            id = f"{i}000a{y}"
            if len(id) > max_len:
                max_len = len(id)
            docs.append((id, when))

        d.add_docs(docs)

    print(f"took {time.time() - s} seconds")
    print(f"Final count {d.count()}")
    print(f"max id len is {max_len}")


print("Looking for one id")

d = ElasticIndexIds(DB_NAME)


def _lookup():
    assert d.find("23000a34") is not None


print(f"{timeit.timeit(_lookup, number=1000)} seconds")

print(f"Size of DB on disk is {os.stat(DB_NAME).st_size / 1024. / 1024.} MiB")
