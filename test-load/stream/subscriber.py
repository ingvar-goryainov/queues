import os
import redis
import json

r = redis.Redis(port=6381, db=0)

last_id = '0-0'
while True:
    events = r.xread({"stream": last_id}, block=0, count=100)
    for _, e in events:
        last_id, data = e[0]
        print(last_id)
        print(data)

r.close()