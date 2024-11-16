# Juego de Trivia en Python
Este proyecto es un juego de trivia desarrollado en Python que utiliza varios conceptos avanzados de programación funcional. A continuación, se detallan los conceptos implementados y dónde se encuentran en el código.

## Como ejecutarlo:
En la raiz del proyecto, ejecutar: 
    Para el proyecto: python -m trivia_game.main
    Para los tests: python -m unittest discover -s tests

## Conceptos Implementados
1. Recursión
    * Ubicación: main.py en la función ask_question_recursively.
    * Descripción: La recursión se utiliza en la función ask_question_recursively para permitir que el juego vuelva a preguntar al usuario cuando se ingresa una respuesta inválida, hasta que se ingrese una respuesta válida.
2. Generadores
    * Ubicación: generators.py en la función question_generator.
    * Descripción: La función question_generator implementa un generador que produce preguntas una por una, lo que permite procesar grandes conjuntos de preguntas sin cargarlas todas en memoria al mismo tiempo.
3. Listas por comprensión
    * Ubicación: main.py en la función play_game.
    * Descripción: Se utiliza una lista por comprensión en la línea correct_answers = sum([ask_question_recursively(q, questions) for q in selected_questions]) para iterar sobre las preguntas seleccionadas y calcular el número de respuestas correctas de forma concisa y eficiente.
4. Decoradores
    * Ubicación: decorators.py en la función timeit.
    * Descripción: El decorador timeit mide y muestra el tiempo de ejecución de la función play_game. Se aplica sobre la función para envolverla y añadir funcionalidad sin modificar su código original.
5. itertools.chain
    * Ubicación: questions.py en la función get_random_options.
    * Descripción: itertools.chain se utiliza para concatenar las opciones de respuesta correctas e incorrectas en una sola lista antes de barajarlas y presentarlas al usuario.
6. Mónadas
    * Ubicación: monads.py en la clase Maybe.
    * Descripción: La clase Maybe se utiliza para encapsular operaciones que pueden resultar en un valor o en None, proporcionando una forma segura de manejar posibles valores faltantes o errores en el flujo del programa. En este código, se usa principalmente para cargar preguntas desde un archivo y garantizar que, en caso de que no se puedan cargar, el resto del sistema no falle inesperadamente. A través de métodos como bind y get_or_else, permite encadenar funciones sobre los datos cargados de manera segura, o proporcionar valores por defecto cuando los datos no están disponibles, evitando comprobaciones explícitas de None en otras partes del programa
7. Funciones lambda
    * Ubicación: main.py en la función evaluate_answer.
    * Descripción: Se utiliza una función lambda para comparar la respuesta del usuario con la respuesta correcta en la función evaluate_answer, permitiendo evaluar las respuestas de manera compacta y eficiente.
8. functools.partial (Extra)
    * Ubicación: main.py y utils.py en la función calculate_default_score.
    * Descripción: partial se utiliza para predefinir el argumento points_per_question en la función calculate_score, creando una versión de la función con un valor fijo de puntos por pregunta, simplificando así las llamadas a la función en el resto del código.
9. functools.lru_cache (Extra)
    * Ubicación: questions.py en la función load_questions.
    * Descripción: lru_cache se aplica a la función load_questions para almacenar en caché el resultado de la carga de preguntas desde el archivo CSV, mejorando el rendimiento si se llama a esta función varias veces con el mismo archivo (Cosa que no pasa).

## Extras no Implementados:
1. Se podria implementar una Tail recursion en main.py para calcular la suma de puntos, lo cual no seria compatible con el requisito de usar Listas por Comprension
    ```python
    def sum_points_recursively(questions: List[Dict[str, str]], all_questions: List[Dict[str, str]], accumulator: int = 0) -> int:
        """Tail-recursive function to calculate the total score based on correct answers."""
        if not questions:
            return accumulator

        question = questions[0]
        remaining_questions = questions[1:]

        points_for_this_question = ask_question_recursively(question, all_questions)
        return sum_points_recursively(remaining_questions, all_questions, accumulator + points_for_this_question)


## Estructura del Proyecto
    main.py: Contiene la lógica principal del juego, incluida la interacción con el usuario y la ejecución del flujo del juego.
    decorators.py: Define decoradores reutilizables, como timeit.
    questions.py: Maneja la carga y selección de preguntas, así como la generación de opciones de respuesta.
    utils.py: Contiene funciones de utilidad como calculate_score y evaluate_answer.
    monads.py: Implementa el concepto de mónadas a través de la clase Maybe.
    generators.py: Define generadores utilizados para la producción de preguntas