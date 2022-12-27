import redis

r = redis.Redis(host="localhost", port=6379, db=0)
p = r.pubsub()
p.subscribe("my-first-channel")
r.publish("my-first-channel", "Hello World!")
print(p.get_message())
