import unittest
import config
import redis

#test_ ile method adı baslamalıdır.
class MyUnitTests(unittest.TestCase):

    host = "test.redis.cache.windows.net"
    accessKey = "BP2QcJ8XSs="

    # def setUp(self):
        # self.redisClient = redis.StrictRedis(host=self.host, port=6380, password=self.accessKey, ssl=True)

    def test_first(self):
        self.assertNotEqual('hakan', 'HAKAN')

    def test_config(self):
        self.assertEqual(config.Config.SqlAlchemyTrackModifications, False)

    def test_redis_access(self):
        assert self.accessKey is not None

    # def test_redis(self):
        # self.assertEqual(self.redisClient.ping(), True)

    # def tearDown(self):
        # self.redisClient.flushall()

