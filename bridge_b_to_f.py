from http.server import HTTPServer, BaseHTTPRequestHandler
import random as _r
import json

import ConnectionToChat as _c
import ContextOfTraining as _ct

class MyServer(BaseHTTPRequestHandler):
        
    def do_POST(self):
        
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        
        data = json.loads(body.decode('utf-8'))
        
        print(f"peticion recibida:\n{data}");
        
        _prompt = data['prompt']
        tipo_entrenamiento_elegido = data['tipoent']
        
        # tipo_entrenamiento_elegido, _prompt
        random_number = _r.randint(0, 2)
        
        _context = _ct.get_context_by_train(tipo_entrenamiento_elegido,False)
        
        messages = [_context[0]]
        
        if "prueba" in _prompt:
            _prompt = "Describe una criatura mitologica no descrita hasta ahora"
        
        assistant_response = _c.send_to_ai(messages,_prompt,random_number)
        
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin","*")
        self.end_headers();
        self.wfile.write(assistant_response.encode())

def main():
    PORT = 3002
    server_address = ('localhost', PORT)
    server = HTTPServer(server_address, MyServer)
    print('Iniciando servidor en el puerto {0}\n'.format(PORT))
    server.serve_forever()

if __name__ == '__main__':
    main()        