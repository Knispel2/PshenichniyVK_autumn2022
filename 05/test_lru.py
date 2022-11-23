import unittest
import lru


class TestLRU(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_proba1_1(self):
        self.cache = lru.MyLRU(2)
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.cache.set("k1", "val3")
        self.assertNotEqual(self.cache.get("k1"), None)
        self.assertNotEqual(self.cache.get("k2"), None)

    def test_proba1_3(self):
        self.cache = lru.MyLRU(1)
        self.cache.set("k1", "val1")
        self.assertEqual(self.cache.get("k1"), "val1")
        self.cache.set("k2", "val2")
        self.assertEqual(self.cache.get("k1"), None)
        self.assertEqual(self.cache.get("k2"), "val2")

    def test_proba1_4(self):
        self.cache = lru.MyLRU(2)
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.assertEqual(self.cache.get("k3"), None)
        self.assertEqual(self.cache.get("k2"), "val2")
        self.assertEqual(self.cache.get("k1"), "val1")
        self.cache.set("k3", "val3")
        self.assertEqual(self.cache.get("k3"), "val3")
        self.assertEqual(self.cache.get("k2"), None)
        self.assertEqual(self.cache.get("k1"), "val1")

    def test_proba1_5(self):
        self.cache = lru.MyLRU(2)
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.cache.set("k1", "val3")
        self.cache.set("k3", "val4")
        self.assertEqual(self.cache.get("k2"), None)
        self.assertEqual(self.cache.get("k1"), "val3")
        self.assertEqual(self.cache.get("k3"), "val4")