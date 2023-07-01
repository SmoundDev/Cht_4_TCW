import openai
import configurations.config as config
from rich import print

class SendToAi:
    def send_to_ai(_messages, _prompt, _random_number):
        # Definir tu clave de API como una variable de entorno
        openai.api_key = config.aky.replace("_", "")

        _messages.append({"role": "user", "content": _prompt})

        response = openai.ChatCompletion.create(
            # model="gpt-3.5-turbo-0613", messages=_messages, n=1
            model="gpt-3.5-turbo-16k-0613", messages=_messages, n=1
            # model="gpt-3.5-turbo", messages=_messages, n=3
        )
        response_assistant = response.choices[0].message.content
        # response_assistant = response.choices[_random_number].message.content
        
        num_tokens = len(response_assistant.split())
        print(f'[bold gold1]La respuesta contiene {num_tokens} tokens [/bold gold1]')


        return response_assistant
