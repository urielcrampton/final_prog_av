import unittest
from trivia_game.utils import calculate_score  

class TestUtils(unittest.TestCase):
    def test_calculate_score(self):
        self.assertEqual(calculate_score(5, 10), 50)  # Pasa ambos argumentos
        self.assertEqual(calculate_score(5, 20), 100)  # Prueba con puntos diferentes
        self.assertEqual(calculate_score(0, 10), 0)    # Caso con 0 respuestas correctas
        self.assertEqual(calculate_score(3, 15), 45)   # Caso con puntos diferentes

if __name__ == '__main__':
    unittest.main()
