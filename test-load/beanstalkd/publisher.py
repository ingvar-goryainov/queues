import greenstalk
import names
import json
import time

def publish( client, n ) :
    data = {}
    data['name'] = names.get_full_name()
    data['number'] = n

    print("%s : %s" % (n, data['name']))
    client.put(json.dumps(data))

client = greenstalk.Client(('127.0.0.1', 11300))

start_time = time.time()
n = 0
while n < 100000:
    n += 1
    publish( client, n )

print("--- %s seconds ---" % (time.time() - start_time))

client.close()