import configurations.config as config
from  configurations.config import ai_variables as aiv 
from rich import print
from rich.table import Table

import random

def get_context_by_train(__entrenamiento_elegido,tryning_mode):
    
    lst_names = aiv.ai_surname
    
    random_number = random.randint(0,len(lst_names)-1)

    _log_from = ""
    _entrenamiento = ""

    if tryning_mode:
        textFisrtPromt = ""

        if __entrenamiento_elegido == "p":
            _context = {"role": "system",
                        "content": "Eres un tecnico reparador de celulares, no puedes dar respuestas a contextos "
                        + f"fuera de la reparación de smartphones, te llamas {aiv.ai_name}"}
            textFisrtPromt = f"💬 Bienvenido, soy {aiv.ai_name} {lst_names[random_number]} el Asistente virtual TCW, ¿en que puedo ayudarte?"
            _entrenamiento = 'Preguntas técnicas'
            _log_from = 'User'

        elif __entrenamiento_elegido == "r":
            _context = {"role": "system",
                        "content": "Eres un investigador que realiza una encuesta de preguntas como si fuera un usuario de "
                        + f"smartphones que presenta distintas fallas o descomposturas. realiza la pregunta sí el mensaje dice"
                        + " `next_question`"}
            textFisrtPromt = ""
            _entrenamiento = "Respuestas técnicas"
            _log_from = 'GPT'

        elif __entrenamiento_elegido == "rw":
            # _context = {
            #     "role":"system",
            #     "content":""
            # }
            _entrenamiento = "Palabras relacionadas"
            _log_from = 'User'
        elif __entrenamiento_elegido == "rw":
            # _context = {
            #     "role":"system",
            #     "content":""
            # }
            _entrenamiento = "Palabras relacionadas"
            _log_from = 'User'
            
        print("[bold green] ----- --------Tryining NO-------- ----- [/bold green]")
        
    else:
        textFisrtPromt = f"💬 Bienvenido, soy {aiv.ai_name} {lst_names[random_number]} el Asistente virtual TCW, ¿en que puedo ayudarte?"

        # comentar en produccion
        _context = {"role": "system",
                    "content": "Eres un programador especializado en python, node.js, mongoDB,sql,react, angular y c#"}
        
        
        # # comentar en produccion
        # _context = {"role": "system",
        #             "content": "Eres un Diseñador especializado en hacer animaciones svg y convirtiendolas en GIF"}
        
        
        print("[bold Yellow] ----- --------Tryining OFF-------- ----- [/bold Yellow]")
        _log_from = "try_off"

    return [_context, textFisrtPromt, _log_from, _entrenamiento]

