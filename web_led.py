import SimpleHTTPServer
import SocketServer
import pingo
from time import sleep


PORT = 80

class my_arduino():
  def __init__(self):
    print "Iniciando comunicao serial com arduino"
    board = pingo.detect.get_board()
    
    global led_pin
    
    led_pin = board.pins[13]
    led_pin.mode = pingo.OUT
  

class my_handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
 

  def __init__(self, request, client_address, server, fake=False):
    if fake == False:
      SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self, request, client_address, server)
    pass
    

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()

    led_status = self.path

    if led_status == "/led_status=off" or led_status == "/" :
      self.wfile.write("<center><h1>Python com Arduino!</h1><br></center>")
      self.wfile.write("<center><a href=\"http://127.0.0.1/led_status=on\">\
          <button>Acender LED</button>\
          </a></center>")
      # Desliga LED
      led_pin.low()

    elif led_status == "/led_status=on":
      self.wfile.write("<center><h1>Python com Arduino!</h1><br></center>")
      self.wfile.write("<center><a href=\"http://127.0.0.1/led_status=off\">\
          <button>Apagar LED</button>\
          </a></center>")
      # Aciona LED
      led_pin.high()
    return
 
try:
  # Reutilizar endereco e nao acusar erro de socket em uso
  SocketServer.ThreadingTCPServer.allow_reuse_address = True

  # Objeto SocketServer
  httpd = SocketServer.ThreadingTCPServer(("", PORT), my_handler)

  # Objeto para iniciar comunicao Arduino
  my_arduino()

  print "servidor web rodando na porta ", PORT
  httpd.serve_forever()
 
except KeyboardInterrupt:
  print "Voce pressionou ^C, encerrando..."
  httpd.socket.close()
