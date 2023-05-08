import openai
import configurations.config as config

class SendToAi:
    def send_to_ai(_messages, _prompt, _random_number):
        # Definir tu clave de API como una variable de entorno
        openai.api_key = config.aky.replace("_", "")

        _messages.append({"role": "user", "content": _prompt})
        openai.api_key = config.aky.replace("_", "")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=_messages, n=3
        )

        response_assistant = response.choices[_random_number].message.content

        return response_assistant
