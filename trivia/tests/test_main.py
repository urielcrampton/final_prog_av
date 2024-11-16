import unittest
from unittest.mock import patch
from trivia_game.main import play_game

class TestMain(unittest.TestCase):
    @patch('trivia_game.main.get_random_questions_gen')
    @patch('trivia_game.main.shuffle_options')
    @patch('trivia_game.main.get_random_options')
    @patch('trivia_game.main.ask_question_recursively')
    @patch('trivia_game.main.calculate_default_score')
    def test_play_game(self, mock_calculate_score, mock_ask_question_recursively, mock_get_random_options, mock_shuffle_options, mock_get_random_questions_gen):
        # Setup mock behavior
        mock_get_random_questions_gen.return_value = [{'Question': 'Q1', 'Answer': 'A1'}]
        mock_get_random_options.return_value = ['A1', 'B1', 'C1']
        mock_shuffle_options.return_value = ['A1', 'B1', 'C1']
        mock_ask_question_recursively.return_value = 1
        mock_calculate_score.return_value = 10

        questions = [{'Question': 'Q1', 'Answer': 'A1'}]
        score = play_game(questions, 1)

        self.assertEqual(score, 10)
        # Verifica que calculate_default_score se llamó con el valor esperado
        mock_calculate_score.assert_called_once_with(1)

if __name__ == '__main__':
    unittest.main()
