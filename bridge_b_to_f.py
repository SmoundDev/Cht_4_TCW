from http.server import HTTPServer, BaseHTTPRequestHandler
import random as _r

import ConnectionToChat as _c
import ContextOfTraining as __ct

class MyServer(BaseHTTPRequestHandler):
        
    def do_POST(self):
        
        print(f"peticion recibida:\n{self}");
        
        data = self.rfile.read();
        
        print(f"peticion recibida:\n{data}");
        
        print(data)
        
        data = data.decode()
        
        print(data)
        
        _prompt = data.decode().replace("prompt=",'')
        tipo_entrenamiento_elegido = data.decode().replace("tipoent=",'')
        
        
        # tipo_entrenamiento_elegido, _prompt
        random_number = _r.randint(0, 2)
        
        _context = __ct.get_context_by_train(tipo_entrenamiento_elegido)
        
        messages = [_context]
        
        assistant_response = _c.send_to_ai(messages,_prompt,random_number)
        
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin","*")
        self.end_headers();
        self.wfile.write(assistant_response)

def main():
    PORT = 3002
    server_address = ('localhost', PORT)
    server = HTTPServer(server_address, MyServer)
    print('Iniciando servidor en el puerto {0}\n'.format(PORT))
    server.serve_forever()

if __name__ == '__main__':
    main()        