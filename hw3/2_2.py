import time
import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)

json_file = '20mb.json'

with open(json_file, 'r') as f:
    data = json.load(f)

start_time = time.time()

for record in data:
    r.hset(record['email'] + '_hash', mapping=record)

end_time = time.time()
save_time_hset = end_time - start_time
print(f"Время сохранения данных с использованием hset: {save_time_hset} сек")

start_time = time.time()

for record in data:
    r.hgetall(record['email'] + '_hash')

end_time = time.time()
read_time_hset = end_time - start_time
print(f"Время чтения данных с использованием hgetall: {read_time_hset} сек")
