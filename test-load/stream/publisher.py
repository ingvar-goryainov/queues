import redis
import names
import json
import time

def publish( r, n ) :
    event = {}
    event['number'] = n
    event['name'] = names.get_full_name()
    print("%s : %s" % (n, event['name']))
    r.xadd("stream", event)

r = redis.Redis(port=6381, db=0)

start_time = time.time()
n = 0
while n < 100000:
    n += 1
    publish( r, n )

r.close()

print("--- %s seconds ---" % (time.time() - start_time))