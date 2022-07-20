import os
import redis
import json

def consume( pubsub ) :
    message = pubsub.get_message()['data']
    print(message)

r = redis.Redis(port=6382, db=0)

pubsub = r.pubsub()

pubsub.subscribe('projector')

for message in pubsub.listen():
    if message.get("type") == "message":
        data = json.loads(message.get("data"))
        name = data.get("name")
        number = data.get("number")
        print("%s : %s" % (number, name))

r.close()