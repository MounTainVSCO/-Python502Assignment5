import unittest
import WilliamZhaoLab5 as as5

class TestFrequencyDistribution(unittest.TestCase):
    
    def test_freq_table(self):
        data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        expected = {1: 1, 2: 2, 3: 3, 4: 4}
        test = as5.freq_table(data)
        self.assertEqual(test, expected)
        print(f"Expected {expected} got {test}")
        
        data = []
        expected = {}
        test = as5.freq_table(data)
        self.assertEqual(test, expected)
        print(f"Expected {expected} got {test}")
        
        data = [1, 1, 1, 1, 1]
        expected = {1: 5}
        test = as5.freq_table(data)
        self.assertEqual(test, expected)
        print(f"Expected {expected} got {test}")

        data = [1, 1, 1, 1, 900]
        expected = {}
        test = as5.freq_table(data)
        self.assertEqual(test, expected)
        print(f"Expected {expected} got {test}")
        
if __name__ == '__main__':
    unittest.main()

"""
Invalid Input, not integer in [0, 9]
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
"""