import os
import openai
import configurations.config as config
from rich import print

# Definir tu clave de API como una variable de entorno
openai.api_key = config.aky.replace("_", "")
response = openai.Image.create(
  prompt='''An hyper relistic album cover where Jupiter, Saturn, Uranus and Neptune appear 
  in the center fused into each other, fading a quarter of each planet to form a single planet 
  with a space full of stars and galaxies in the background. 
  surrounded by a nebula of tones   orange at the bottom. the album is called 'BIg Giants'
  ''',
  n=3,
  size="1024x1024"
)

print(f"[bold green] {response} [/bold green]")
