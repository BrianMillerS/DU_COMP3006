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
    
    def test_c(self):
        sys.argv = ['count.py', '-c', 'test1.txt', 'output.csv']  # simulate the command line argument
        d = count.generate_count_csv()  # generate the count dictionary
        self.assertEqual(len(d), 28)  # check that the dict is the correct length
        self.assertDictContainsSubset(d, {"F":1,"I":1,"T":2,"W":1,"a":18,"c":13,"b":1,"e":28,"d":9,"g":2,"f":6,"i":18,"h":9,"k":1,"m":5,"l":15,"o":21,"n":15,"p":10,"s":14,"r":12,"u":10,"t":35,"w":4,"v":6,"y":8,"x":4,"z":1})  # check key:value pairs

    def test_z(self):
        sys.argv = ['count.py', '-z', 'test1.txt', 'output.csv']  # simulate the command line argument
        d = count.generate_count_csv()  # generate the count dictionary
        self.assertEqual(len(d), 26)  # check that the dict is the correct length
        self.assertDictContainsSubset(d, {"a":18,"c":13,"b":1,"e":28,"d":9,"g":2,"f":7,"i":19,"h":9,"k":1,"j":0,"m":5,"l":15,"o":21,"n":15,"q":0,"p":10,"s":14,"r":12,"u":10,"t":37,"w":5,"v":6,"y":8,"x":4,"z":1})  # check key:value pairs
    
    def test_cl(self):
        sys.argv = ['count.py', '-c', '-l', 'abcdABCD', 'test1.txt', 'test2.txt', 'output.csv']  # simulate the command line argument
        d = count.generate_count_csv()  # generate the count dictionary
        self.assertEqual(len(d), 5)  # check that the dict is the correct length
        self.assertDictContainsSubset(d, {'a':37, 'b':3,'c':29,'d':18,'C':1})  # check key:value pairs

if __name__ == '__main__':
    unittest.main()
