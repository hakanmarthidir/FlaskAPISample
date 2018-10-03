import redis
import datetime
import config

host = config.Config.RedisHost
accessKey = config.Config.RedisAccessKey

redisClient = redis.StrictRedis(host=host, port=6380, password=accessKey, ssl=True)
cachedResult1 = redisClient.set("developer", "Hakan")
cachedResult2 = redisClient.set("mytime1", datetime.datetime.now())
cachedResult3 = redisClient.setex("mytime2", 30, datetime.datetime.now())

print(str(cachedResult1))
print(str(cachedResult2))
print(str(cachedResult3))

try:
    result = redisClient.get("developer")
    resultdate = redisClient.get("mytime")
    resultdate2 = redisClient.get("mytime2")

    print(result.decode("utf-8"))
    print(resultdate.decode("utf-8"))
    print(resultdate2.decode("utf-8"))

except Exception as e:
    print(e)


pingResult = redisClient.ping()
print(str(pingResult))


clientList = redisClient.client_list()
for c in clientList:
    print(c)


redisClient.flushdb()
redisClient.flushall()