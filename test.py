#coding:utf-8
import unittest
from modules.functions import crypt_string

class TestCryptage(unittest.TestCase):
    
    def setUp(self):
        self.res1_1 = crypt_string('Bonjour ENEAM', 'cle')
        self.res1_2 = crypt_string('', 'cle')
        self.res2 = crypt_string('écolier', 'cle')
        self.res3 = crypt_string('élève', 'feu')
        self.res4 = crypt_string('bonjour', 'feu')
    
    def test_res1_1(self):
        self.assertGreater(len(self.res1_1), 0)
    
    def test_res1_2(self):
        self.assertTrue(len(self.res1_2) == 0)

    def test_res2(self):
        self.assertEqual(self.res2, False)

    def test_res3(self):
        self.assertEqual(self.res3, False)

    def test_res4(self):
        self.assertGreater(len(self.res4), 0)

if __name__ == '__main__':
    unittest.main()