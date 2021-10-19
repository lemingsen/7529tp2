import unittest

from src.lector import Lector

class TestLector(unittest.TestCase):
    def test_inexistente(self):
        self.assertRaises(Exception,Lector,"nombre_de_archivo_inexistente.txt")


if __name__ == '__main__':
    unittest.main()