import config

def get_context_by_train(__entrenamiento_elegido):

    if config.trining_mode:
        textFisrtPromt = ""

        if __entrenamiento_elegido == "p":
            _context = {"role": "system",
                        "content": "Eres un tecnico reparador de celulares, no puedes dar respuestas a contextos "
                        + f"fuera de la reparación de smartphones, te llamas {config.ai_name}"}
            textFisrtPromt = f"💬 Bienvenido, mi nombre es {config.ai_name} el Asistente virtual TCW, ¿en que puedo ayudarte?"

        elif __entrenamiento_elegido == "r":
            _context = {"role": "system",
                        "content": "Eres un investigador que realiza una encuesta de preguntas como si fuera un usuario de "
                        + f"smartphones que presenta distintas fallas o descomposturas. realiza la pregunta sí el mensaje dice"
                        + " 'next_question'"}
            textFisrtPromt = ""
        
        print("[bold green] ----- --------Tryining NO-------- ----- [/bold green]")
        
    else:
        textFisrtPromt = f"💬 Bienvenido, mi nombre es {config.ai_name} el Asistente virtual TCW, ¿en que puedo ayudarte?"

        # comentar en produccion
        _context = {"role": "system",
                    "content": "Eres un programador especializado en python, node.js, mongoDB,sql,react, angular y c#, sí el usuario "+
                    "ecribe save_response guardas la respuesta en la siguiente ruta \"/data_collectors/save_answer.csv\""}
        
        print("[bold Yellow] ----- --------Tryining OFF-------- ----- [/bold Yellow]")
        

    return [_context, textFisrtPromt]

