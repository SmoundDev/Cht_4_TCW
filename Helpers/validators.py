import os
from routes_files import file_route 

def validar_existencia_archivos():

    # Valida la existencia del archivo "Preguntas" sí este no existe, se crea
    if not os.path.isfile(file_route.f_preguntas):
        # Crear el archivo
        with open(file_route.f_preguntas, 'w') as file:
            file.write("- Preguntas -")
        print("El archivo Preguntas se ha creado con éxito.")

    # Valida la existencia del archivo "Respuestas" sí este no existe, se crea
    if not os.path.isfile(file_route.f_respuestas):
        # Crear el archivo
        with open(file_route.f_preguntas, 'w') as file:
            file.write("- Respuestas -")
        print("El archivo Respuestas se ha creado con éxito.")

    # Valida la existencia del archivo "Malas Palabras" sí este no existe, se crea
    if not os.path.isfile(file_route.f_malas_palabras):
        # Crear el archivo
        with open(file_route.f_malas_palabras, 'w') as file:
            file.write("- Malas Palabras -")
        print("El archivo Malas Palabras se ha creado con éxito.")

    # Valida la existencia del archivo "palabras_no_relacionadas" sí este no existe, se crea
    if not os.path.isfile(file_route.f_palabras_no_relacionadas):
        # Crear el archivo
        with open(file_route.f_palabras_no_relacionadas, 'w') as file:
            file.write("- palabras_no_relacionadas -")
        print("El archivo palabras_no_relacionadas se ha creado con éxito.")

    # Valida la existencia del archivo "Preguntas" sí este no existe, se crea
    if not os.path.isfile(file_route.f_palabras_relacionadas):
        # Crear el archivo
        with open(file_route.f_palabras_relacionadas, 'w') as file:
            file.write("- palabras_relacionadas -")
        print("El archivo palabras_relacionadas se ha creado con éxito.")

    # Valida la existencia del archivo "Respuestas" sí este no existe, se crea
    if not os.path.isfile(file_route.f_respuestas_ai):
        # Crear el archivo
        with open(file_route.f_respuestas_ai, 'w') as file:
            file.write("- f_respuestas_ai -")
        print("El archivo f_respuestas_ai se ha creado con éxito.")

    # Valida la existencia del archivo "Respuestas" sí este no existe, se crea
    if not os.path.isfile(file_route.f_preguntas_ai):
        # Crear el archivo
        with open(file_route.f_preguntas_ai, 'w') as file:
            file.write("- f_preguntas_ai -")
        print("El archivo f_preguntas_ai se ha creado con éxito.")
