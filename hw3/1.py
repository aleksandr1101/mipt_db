import json
import redis


r = redis.Redis(host='localhost', port=6379, db=0)

json_file = '20mb.json'

with open(json_file, 'r') as f:
    data = json.load(f)

for i, record in enumerate(data):
    r.set(record['email'], json.dumps(record))
    r.hset(record['email'] + '_hash', mapping=record)
    r.zadd('emails_zset', {record['email']: i})
    r.rpush('emails_list', json.dumps(record))

print("Данные успешно сохранены в Redis")
