from http.server import HTTPServer, BaseHTTPRequestHandler
import random as _r

from ConnectionToChat import send_to_ai
import ContextOfTraining as __ct


def Generate_Ai_Response(tipo_entrenamiento_elegido, _prompt):
    
    random_number = _r.randint(0, 2)
    
    _context = __ct.get_context_by_train(tipo_entrenamiento_elegido)
    
    messages = [_context]