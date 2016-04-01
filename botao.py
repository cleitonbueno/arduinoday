import pingo
from time import sleep

print "Detectando placa, aguarde..."
board = pingo.detect.get_board()
print "Placa -> %s" % (board)

print "Configurando pino 12 [Botao Onboard]"
botao_pin = board.pins[12]
botao_pin.mode = pingo.IN

print "Loop..."

while True:
  status_botao = botao_pin.state
  if status_botao == "HIGH":
    print "Botao pressionado!"
  sleep(1)


