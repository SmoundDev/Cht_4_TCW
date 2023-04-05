
# TODO
# El sistema entra por primera vez y valida que los archivos de datos existan
# Basdo en el tipo de entrenamiento seleccionado el sistema seteará la variable "_global_file"
# que indicará la ruta del archivo donde se tomarán los datos para entrenamiento
# Basado en el entrenamiento, se pondrá un contexto referente a lo que se busca haga o responda
# el asistente
# Basado en el entrenamiento, debe setearse la variable "_response_contains" que nos indica que
# posible respuesta o que puede contener el texto de respuesta para que actualicemos los datos
# del entrenamiento
# Casos de USO:
# - Preguntas: El usuario realizará preguntas relacionadas con el tema en cuestion, calificando
# la respuesta para poder agregarlas a los datos de entrenamiento.
# - Respuestas: El asistente realizará preguntas sobre el tema en cuestion, calificando dichas
# preguntas para que se añadan a la lista de preguntas permitidas.Siempre que el usuario así
# lo determine
