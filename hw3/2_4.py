import time
import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)

json_file = '20mb.json'

with open(json_file, 'r') as f:
    data = json.load(f)

start_time = time.time()

for record in data:
    r.rpush('emails_list', json.dumps(record))

end_time = time.time()
save_time_list = end_time - start_time
print(f"Время сохранения данных с использованием списка: {save_time_list} сек")

start_time = time.time()

r.lrange('emails_list', 0, -1)

end_time = time.time()
read_time_list = end_time - start_time
print(f"Время чтения данных с использованием списка: {read_time_list} сек")
