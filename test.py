import unittest
from main import *


class MyTestCase(unittest.TestCase):
    
    #def setUp(self):
    #    self.driver = webdriver.Edge()
        
    #def tearDown(self):
    #    self.driver.quit()
        
    def test_zero(self):
        self.assertEqual(Add(""), 0)  # add assertion here

    def test_figures(self):
        self.assertEqual(Add("3,4"), 7)

    def test_many_figures(self):
        self.assertEqual(Add("3,4,5"), 12)

    def test_wrong_char(self):
        with self.assertRaises(ValueError):
            Add("1,2,\n7")

    def test_good_char(self):
        self.assertEqual(Add("1,2\n7"), 10)

    def test_float(self):
        self.assertEqual(Add("1,2.3"), 3.3)


if __name__ == '__main__':
    unittest.main()
