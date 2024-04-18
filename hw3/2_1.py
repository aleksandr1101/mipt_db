import time
import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)

json_file = '20mb.json'

with open(json_file, 'r') as f:
    data = json.load(f)

start_time = time.time()

for record in data:
    r.set(record['email'], json.dumps(record))

end_time = time.time()
save_time = end_time - start_time
print(f"Время сохранения данных: {save_time} сек")

start_time = time.time()

for record in data:
    r.get(record['email'])

end_time = time.time()
read_time = end_time - start_time
print(f"Время чтения данных: {read_time} сек")
