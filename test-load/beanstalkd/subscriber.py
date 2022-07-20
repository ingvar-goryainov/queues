import os
import greenstalk
import json

def consume( pubsub ) :
    message = pubsub.get_message()['data']
    print(message)

client = greenstalk.Client(('127.0.0.1', 11300))

while True:
    job = client.reserve()
    print(job.body)
    client.delete(job)

client.close()