import unittest
from trivia_game.monads import Maybe

class TestMaybe(unittest.TestCase):
    def test_maybe_with_value(self):
        maybe = Maybe('value')
        self.assertFalse(maybe.is_nothing())
        self.assertEqual(maybe.get_or_else('default'), 'value')

    def test_maybe_without_value(self):
        maybe = Maybe()
        self.assertTrue(maybe.is_nothing())
        self.assertEqual(maybe.get_or_else('default'), 'default')

    def test_bind(self):
        def add_prefix(value: str) -> Maybe[str]:
            return Maybe('prefix_' + value)

        maybe = Maybe('value')
        result = maybe.bind(add_prefix)
        self.assertEqual(result.get_or_else('default'), 'prefix_value')

if __name__ == '__main__':
    unittest.main()
