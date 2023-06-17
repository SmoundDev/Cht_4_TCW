
from nltk.corpus import wordnet
import numpy as np
import math
import matplotlib.pyplot as plt

import os

import random
import asyncio

import typer
from rich import print
from rich.table import Table
import time
import pyttsx3
import gc

import configurations.config as config
from Helpers.routes_files import file_route
from Helpers.SendTo import SendToAi as sta
import ContextOfTraining as __ct

# imports para el aprendizaje básico natural de texto
# import nltk
# nltk.download('wordnet')

# voice_engine = pyttsx3.init(driverName='sapi5') # Utilizamos el motor de síntesis de voz SAPI5
# # Obtenemos las voces disponibles en el sistema
# voices = voice_engine.getProperty('voices')
# for voice in voices:
#     if voice.name == 'Microsoft Zira Desktop':
#         voice_engine.setProperty('voice', voice.id)
#         break

_global_file = ""
respondeAI = False
_response_contains = []

def main():

    print("[bold green] ----- -------TCW Asistencia Online------- ----- [/bold green]")

    print("[bold green] ----- ----------------------------------- ----- [/bold green]")
    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Iniciar nueva conversación")
    table.add_row("voice_off", "Detiene la lectura de las respuestas(on dev)")
    table.add_row("voice_on", "Inicia la lectura de las respuestas(on dev)")
    
    print(table)
    print("[bold green] ----- ----------------------------------- ----- [/bold green]")

    # Aquí vamoa elegír el tipo de entrenamiento que el usuario realizará
    print("[bold yellow] Tipos de Entrenamiento: [/bold yellow]")

    table = Table("Comando", "Descripción")
    table.add_row("p", "Preguntas técnicas")
    table.add_row("r", "Respuesta técnicas(on dev)")
    table.add_row("rw", "Palabras relacionadas(on dev)")
    table.add_row("nw", "Palabras no relacionadas(on dev)")
    print(table)

    tipo_entrenamiento_elegido = input(
        "Por favor, Elija un tipo de entrenamiento utilizando el comando deseado: ")


    _context = __ct.get_context_by_train(tipo_entrenamiento_elegido,config.trining_mode)
    _textFisrtPromt = _context[1]
   
    # # añadimos el Contexto del asistente que se recibe acorde al tipo de entrenamiento
    messages = [_context[0]]

    while True:
        global respondeAI;
        
        _content = __prompt(_textFisrtPromt)

        if _content == "new":
            respondeAI = False;
            
            print("🆕 Nueva conversación creada")
            messages = [_context[0]]
            _content = __prompt(_textFisrtPromt)


        # Validador de texto antes de enviar el prompt
            #aqui se pondrá funcionalidad para que el texto sea validado respecto a los datos entrenados
            
        # Enviar una solicitud a la API para generar texto
        random_number = random.randint(0, 2)
        
        response_assistant = sta.send_to_ai(messages,_content,random_number)
        
        gc.collect()

        tam_respuesta =   len(response_assistant)
        # Pasamos el contexto de las respuestas de la conversación
        if tam_respuesta < 1000:
            messages.append({"role": "assistant", "content": response_assistant})

        if not tipo_entrenamiento_elegido == "r":
           
            textFisrtPromt = "💬 ¿Algo más en lo que pueda ayudarte?"
            # Imprimir la respuesta generada por la API
            type_printer(random_number, response_assistant, textFisrtPromt)



def type_printer(random_number, response_assistant, textFisrtPromt):
    #descomentar para pruebas
    global _textFirstPrompt, respondeAI 
    #  print(f"[bold red]** [/bold red] se dió la respuesta #{random_number}:\n")
    print("[bold green]-> [/bold green]", end='')
    
    for char in response_assistant:
        print(f"[cyan]{char}[/cyan]", end='', flush=True)
        time.sleep(0.07)
    
    respondeAI = True

def __prompt(textFisrtPromt) -> str:
    
    global respondeAI
    
    if respondeAI:
        
        _textFisrtPromt = "💬 ¿Algo más en lo que pueda ayudarte?"
        
    else:
        _textFisrtPromt = "💬 Bienvenido al Asistente virtual TCW, ¿en que puedo ayudarte?"

    prompt = typer.prompt(f"\n {textFisrtPromt}")

    if prompt == "exit":
        exit = typer.confirm(
            "✋ [red]¿Estás seguro de terminar esta conversación?[/red]")
        if exit:
            respondeAI = False;
            print("👋 Fue un placer atenderte, ¡vuelve pronto!")
            raise typer.Abort()

        return __prompt(_textFisrtPromt)
    
        
    return prompt


if __name__ == "__main__":
    typer.run(main)
