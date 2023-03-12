import unittest
from translator import en_fr, fr_en

class Testfr_en(unittest.TestCase):
    def test1(self):
        self.assertEqual(en_fr('Hello'),'Bonjour')
        self.assertEqual(en_fr('Good'),'Bonne')

class Testfr_en(unittest.TestCase):
    def test1(self):
        self.assertEqual(fr_en('Bonne'),'Good')
        self.assertEqual(fr_en('Bonjour'),'Hello')
        

   

unittest.main()
