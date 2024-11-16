import trivia
import usql
import pedidos
import subprocess

def main():
    print("Seleccione una opción:")
    print("1. Jugar Trivia")
    print("2. Procesar Pedidos")
    print("3. Realizar Consulta USQL")
    
    choice = input("Opción: ")
    
    if choice == "1":
        # Ejecutar Trivia utilizando el comando adecuado
        subprocess.run(["py", "-m", "trivia.trivia_game.main"]) 
    elif choice == "2":
        # Ejecutar módulo de Pedidos (Java)
        subprocess.run(["java", "-cp", "pedidos", "Main"])
    elif choice == "3":
        # Ejecutar módulo USQL (Python)
        subprocess.run(["py", "-m", "usql.tests.test_usql_lexer"]) 
        subprocess.run(["py", "-m", "usql.tests.test_parser"]) 
        subprocess.run(["py", "-m", "usql.tests.test_sql_to_usql"]) 
        subprocess.run(["py", "-m", "usql.tests.test_usql_to_sql"])  
    else:
        print("Opción inválida")

if __name__ == "__main__":
    main()