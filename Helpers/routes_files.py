import datetime

class file_route:
    f_preguntas = "/data_collectors/questions.csv"
    f_respuestas_ai = "/data_collectors/answers_ai.csv"
    f_preguntas_ai = "/data_collectors/questions_ai.csv"
    f_respuestas = "/data_collectors/answers.csv"
    f_malas_palabras = "/data_collectors/bad_words.csv"
    f_palabras_relacionadas = "/data_collectors/related_words.csv"
    f_palabras_no_relacionadas = "/data_collectors/unrelated_words.csv"
    log = "/data_collectors/log.txt"

class write_files:
    def writte_log(_promp, _from):
        fecha_actual = datetime.datetime.now()

        if fecha_actual not in  file_route.log:
            with open(file_route.log, 'a') as f:
                f.write('*********\n')
                f.write('**********************\n')
                f.write(f'***************************** {fecha_actual} *****************************\n')
                f.write('*****Un nuevo día de entrenamiento*****\n')

        log = f"{fecha_actual}: {_promp}"

        with open(file_route.log, 'a') as archivo:
            archivo.write(log + "\n")
    
    def write_question(_prompt):
        try:
            # Código que puede provocar una excepción
            archivo = open("archivo.txt", "r")
            contenido = archivo.read()
        except FileNotFoundError:
            # Manejo de la excepción para el caso de que el archivo no se encuentre
            print("El archivo no se pudo encontrar.")
        except:
            # Manejo genérico de excepciones
            print("Ha ocurrido un error inesperado.")