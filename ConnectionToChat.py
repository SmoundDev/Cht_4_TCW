
from nltk.corpus import wordnet
import numpy as np
import math
import matplotlib.pyplot as plt

import openai
import os

import config
import random
import asyncio

import typer
from rich import print
from rich.table import Table
import time
import pyttsx3

from Helpers.routes_files import file_route

# imports para el aprendizaje básico natural de texto
# import nltk
# nltk.download('wordnet')

voice_engine = pyttsx3.init(driverName='sapi5') # Utilizamos el motor de síntesis de voz SAPI5
# Obtenemos las voces disponibles en el sistema
voices = voice_engine.getProperty('voices')
for voice in voices:
    if voice.name == 'Microsoft Zira Desktop':
        voice_engine.setProperty('voice', voice.id)
        break

_global_file = ""
_response_contains = []

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


def main():

    print("[bold green] ----- -------TCW Asistencia Online------- ----- [/bold green]")

    print("[bold green] ----- ----------------------------------- ----- [/bold green]")
    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Iniciar nueva conversación")
    table.add_row("voice_off", "Detiene la lectura de las respuestas")
    table.add_row("voice_on", "Inicia la lectura de las respuestas")
    
    print(table)
    print("[bold green] ----- ----------------------------------- ----- [/bold green]")

    # #comentar en produccion
    # textFisrtPromt = "💬 Bienvenido al Asistente virtual TCW, ¿en que puedo ayudarte?"
    # _textFisrtPromt = "💬 Bienvenido al Asistente virtual TCW, ¿en que puedo ayudarte?"

    # Aquí vamoa elegír el tipo de entrenamiento que el usuario realizará
    print("[bold yellow] Tipos de Entrenamiento: [/bold yellow]")

    table = Table("Comando", "Descripción")
    table.add_row("p", "Preguntas técnicas")
    table.add_row("r", "Respuesta técnicas")
    table.add_row("rw", "Palabras relacionadas")
    table.add_row("nw", "Palabras no relacionadas")
    print(table)

    tipo_entrenamiento_elegido = input(
        "Por favor, Elija un tipo de entrenamiento utilizando el comando deseado: ")

    # Definir tu clave de API como una variable de entorno
    openai.api_key = config.api_key

    _context, textFisrtPromt = get_context_by_train(tipo_entrenamiento_elegido)
    _textFisrtPromt = textFisrtPromt
    # # Contexto del asistente
    # _context = {"role": "system",
    #             "content": "Eres un tecnico reparador de celulares, no puedes dar respuestas a contextos "
    #             + "fuera de la reparación de smartphones, te llamas 'Spartan'"}

    # #comentar en produccion
    # _context = {"role": "system",
    #             "content": "Eres un programador especializado en python, node.js, mongoDB,sql,react, angular y c#"}

    # _context = {"role":"system",
    #             "content":"Puedes brindar información sobre accesorios celulares"}

    # _context = {"role":"system",
    #             "content":"Puedes asistir a personas en tareas básicas como por ejemplo: enviar un email, apagar el wifi, quitar el modo silencio, entre otras tareas de indole soporte a nivel software"}

    # _context = {"role":"system",
    #             "content":"Eres un asistente muy util para personas poco familiarizadas con el uso de smartphones"}

    # # añadimos el Contexto del asistente que se recibe acorde al tipo de entrenamiento
    messages = [_context]

    while True:

        _content = __prompt(textFisrtPromt)

        if _content == "new":
            print("🆕 Nueva conversación creada")
            messages = [_context]
            _content = __prompt(_textFisrtPromt)

        messages.append({"role": "user", "content": _content})

        # Validador de texto antes de enviar el prompt

        # Enviar una solicitud a la API para generar texto
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages,
            n=3
        )

        random_number = random.randint(0, 2)

        response_assistant = response.choices[random_number].message.content

        # Pasamos el contexto de las respuestas de la conversación
        messages.append({"role": "assistant", "content": response_assistant})

        if not tipo_entrenamiento_elegido == "r":
           
            # Imprimir la respuesta generada por la API
            type_printer(random_number, response_assistant)

        textFisrtPromt = "💬 ¿Algo más en lo que pueda ayudarte?"


def type_printer(random_number, response_assistant):
    print(f"[bold red]** [/bold red] se dió la respuesta #{random_number}:\n")
    print("[bold green]-> [/bold green]", end=' ')

    # loop = asyncio.get_event_loop()
            
    for char in response_assistant:
        print(f"[cyan]{char}[/cyan]", end='', flush=True)
        time.sleep(0.07)
        
    # loop.run_until_complete(leer_respuesta(response_assistant))
    # leer_respuesta(response_assistant)

# Función para leer una respuesta
# async def leer_respuesta(respuesta):
#     # Convertimos la respuesta a voz
#     voice_engine.say(respuesta)
#     # Reproducimos la voz
#     voice_engine.runAndWait()

def __prompt(textFisrtPromt) -> str:
    _textFisrtPromt = "💬 Bienvenido al Asistente virtual TCW, ¿en que puedo ayudarte?"

    prompt = typer.prompt(f"\n {textFisrtPromt}")

    if prompt == "exit":
        exit = typer.confirm(
            "✋ [red]¿Estás seguro de terminar esta conversación?[/red]")
        if exit:
            print("👋 Fue un placer atenderte, ¡vuelve pronto!")
            raise typer.Abort()

        return __prompt(_textFisrtPromt)
    elif prompt == 'voice_off':
        voice_engine.stop()
    elif prompt == 'voice_on':
        voice_engine.stop()
        
    return prompt


if __name__ == "__main__":
    typer.run(main)
