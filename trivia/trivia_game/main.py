from typing import List, Dict
from .questions import load_questions, get_random_questions_gen, shuffle_options, get_random_options
from .utils import calculate_score
from .decorators import timeit
from functools import partial

# Predefinir la función de cálculo de puntuación con puntos por pregunta a 10
calculate_default_score = partial(calculate_score, points_per_question=10)

def ask_question_recursively(question: Dict[str, str], shuffled_options: List[str]) -> int:
    """
    Función para hacer una pregunta y manejar la entrada del usuario con recursión.

    Args:
        question (Dict[str, str]): Diccionario que contiene la categoría, la pregunta y la respuesta correcta.
        shuffled_options (List[str]): Lista de opciones de respuesta ya mezcladas.

    Returns:
        int: 1 si la respuesta del usuario es correcta, 0 si es incorrecta.
    """
    
    print(f"Categoría: {question['Category']}")
    print(f"Pregunta: {question['Question']}")
    
    for i, option in enumerate(shuffled_options):
        print(f"{i + 1}. {option}")
    
    user_answer = input("Tu respuesta (1/2/3): ")
    
    if user_answer not in {'1', '2', '3'}:
        print("Opción inválida. Por favor, elige 1, 2 o 3.")
        return ask_question_recursively(question, shuffled_options)  # Recursión
    
    # Función lambda para verificar si la respuesta del usuario es correcta
    correct = lambda answer: answer.lower() == question['Answer'].lower()

    if correct(shuffled_options[int(user_answer) - 1]):
        print("¡Correcto!\n")
        return 1
    else:
        print(f"Incorrecto. La respuesta correcta era: {question['Answer']}\n")
        return 0


@timeit
def play_game(questions: List[Dict[str, str]], num_questions: int) -> int:
    """
    Función para jugar el juego haciendo una serie de preguntas aleatorias.

    Args:
        questions (List[Dict[str, str]]): Lista de diccionarios que contiene todas las preguntas disponibles.
        num_questions (int): Número de preguntas a seleccionar para el juego.

    Returns:
        int: La puntuación total obtenida después de responder las preguntas.
    """
    selected_questions = get_random_questions_gen(questions, num_questions)
    correct_answers = sum([ask_question_recursively(q, shuffle_options(get_random_options(questions, q['Answer']))) for q in selected_questions])
    return calculate_default_score(correct_answers)


if __name__ == "__main__":
    maybe_questions = load_questions(r'trivia\data\JEOPARDY_CSV.csv')

    # Verificamos si hay preguntas cargadas
    questions = maybe_questions.get_or_else([])

    if not questions:
        print("No se pudieron cargar las preguntas. Por favor, verifica el archivo.")
    else:
        score = play_game(questions, 5)
        print(f"Tu puntuación final es: {score}")
