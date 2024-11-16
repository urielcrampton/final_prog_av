import unittest
from trivia_game.decorators import timeit
import time

class TestDecorators(unittest.TestCase):
    def test_timeit(self):
        @timeit
        def slow_function():
            time.sleep(1)
            return 'done'

        result = slow_function()
        self.assertEqual(result, 'done')

if __name__ == '__main__':
    unittest.main()
