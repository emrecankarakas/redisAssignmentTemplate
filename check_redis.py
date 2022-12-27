import redis

# Connect to Redis
r = redis.Redis(host="localhost", port=6379, db=0)

# Pub sub
p = r.pubsub()
p.subscribe("my-first-channel")
r.publish("my-first-channel", "Hello World!")

# SET GET
r.set("min-sum", 0)
min_sum = r.get("min-sum")
