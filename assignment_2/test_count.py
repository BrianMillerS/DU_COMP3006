import unittest
import count
import sys

class TestCount(unittest.TestCase):

    def test_noArgs(self):
        sys.argv = ['count.py', 'test1.txt', 'test2.txt', 'output.csv']  # simulate the command line argument
        d = count.generate_count_csv()  # generate the count dictionary
        self.assertEqual(len(d), 24)  # check that the dict is the correct length
        self.assertDictContainsSubset(d, {"a":37, "b":3, "c":30, "d":18, "e":69, "f":14, "g":7, "h":20, "i":47, "k":4, "l":32, "m":12, "n":40, "o":43, "p":16, "r":24, "s":43, "t":78, "u":25, "v":10, "w":9, "x":5, "y":17, "z":1})  # check key:value pairs

    def test_l(self):
        sys.argv = ['count.py', '-l', 'abcd', 'test1.txt', 'test2.txt', 'output.csv']  # simulate the command line argument
        d = count.generate_count_csv()  # generate the count dictionary
        self.assertEqual(len(d), 4)  # check that the dict is the correct length
        self.assertDictContainsSubset(d, {'a':37, 'b':3,'c':30,'d':18})  # check key:value pairs

    def test_cl(self):
        sys.argv = ['count.py', '-c', '-l', 'abcdABCD', 'test1.txt', 'test2.txt', 'output.csv']  # simulate the command line argument
        d = count.generate_count_csv()  # generate the count dictionary
        self.assertEqual(len(d), 5)  # check that the dict is the correct length
        self.assertDictContainsSubset(d, {'a':37, 'b':3,'c':29,'d':18,'C':1})  # check key:value pairs

if __name__ == '__main__':
    unittest.main()