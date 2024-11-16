from typing import List

def calculate_score(correct_answers: int, points_per_question: int) -> int:
    """
    Calcula el puntaje basado en las respuestas correctas.

    Args:
        correct_answers (int): Número de respuestas correctas.
        points_per_question (int, opcional): Puntaje que se otorga por cada respuesta correcta. Por defecto es 10.

    Returns:
        int: El puntaje total calculado.
    """
    return correct_answers * points_per_question
