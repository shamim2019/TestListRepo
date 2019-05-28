import unittest
from list1 import addition
class Testaddition(unittest.TestCase):
    def test_list1_sum(self):
        self.assertEqual(addition(), 29)
    if __name__ == "__main__":
        test_list1_sum()
    print("Everything passed")