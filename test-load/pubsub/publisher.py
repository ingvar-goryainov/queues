import redis
import names
import json
import time

def publish( r, n ) :
    data = {}
    data['name'] = names.get_full_name()
    data['number'] = n

    print("%s : %s" % (n, data['name']))
    r.publish('projector', json.dumps(data))

r = redis.Redis(port=6382, db=0)

start_time = time.time()
n = 0
while n < 10000:
    n += 1
    publish( r, n )

r.close()

print("--- %s seconds ---" % (time.time() - start_time))