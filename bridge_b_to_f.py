from http.server import HTTPServer, BaseHTTPRequestHandler
import random as _r
import json

import ConnectionToChat as _c
import ContextOfTraining as _ct
from Helpers import routes_files
from Helpers.SendTo import SendToAi as sta


class MyServer(BaseHTTPRequestHandler):
    _lastPrompt = ""

    def do_POST(self):
        global _lastPrompt

        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)

        data = json.loads(body.decode("utf-8"))

        print(f"peticion recibida:\n{data}")

        _prompt = data["prompt"]
        tipo_entrenamiento_elegido = data["tipoent"]

        # tipo_entrenamiento_elegido, _prompt
        random_number = _r.randint(0, 2)

        _context = _ct.get_context_by_train(tipo_entrenamiento_elegido, False)

        user_from = _context[2]

        if user_from != "try_off":
            _lastPrompt = routes_files.write_files.writte_log(
                _prompt, _entrenamiento, user_from
            )

        _entrenamiento = _context[3]

        messages = [_context[0]]

        if tipo_entrenamiento_elegido == "r":
            messages.append({"role": "user", "content": _prompt})

        if "g''" in _prompt:
            archivo_guardado = routes_files.write_files.write_question(_lastPrompt)

        if "prueba" in _prompt:
            _prompt = "Describe una criatura mitologica no descrita hasta ahora"

        assistant_response = sta.send_to_ai(messages, _prompt, random_number)

        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(assistant_response.encode())


def main():
    PORT = 3002
    server_address = ("localhost", PORT)
    server = HTTPServer(server_address, MyServer)
    print(f"Iniciando servidor en el puerto {PORT}\n")
    server.serve_forever()


if __name__ == "__main__":
    main()
