import unittest
import client
import server
import threading


class TestServer(unittest.TestCase):
    def setUp(self) -> None:
        self.cache = lru.MyLRU(2)

    def test_one(self):
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.assertEqual(self.cache.get("k3"), None)
        self.assertEqual(self.cache.get("k2"), "val2")
        self.assertEqual(self.cache.get("k1"), "val1")

    def test_two(self):
        self.cache = lru.MyLRU(2)
        self.test_one()
        self.cache.set("k3", "val3")
        self.assertEqual(self.cache.get("k3"), "val3")
        self.assertEqual(self.cache.get("k2"), None)
        self.assertEqual(self.cache.get("k1"), "val1")

