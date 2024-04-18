import time
import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)

json_file = '20mb.json'

with open(json_file, 'r') as f:
    data = json.load(f)

start_time = time.time()

for i, record in enumerate(data):
    r.zadd('emails_zset', {record['email']: i})

end_time = time.time()
save_time_zset = end_time - start_time
print(f"Время сохранения данных с использованием zset: {save_time_zset} сек")

start_time = time.time()

r.zrange('emails_zset', 0, -1)

end_time = time.time()
read_time_zset = end_time - start_time
print(f"Время чтения данных с использованием zrange: {read_time_zset} сек")
