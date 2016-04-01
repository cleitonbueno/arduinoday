import pingo
from time import sleep

print "Detectando placa, aguarde..."
board = pingo.detect.get_board()
print "Placa -> %s" % (board)

print "Configurando pino 13 [Led Onboard]"
led_pin = board.pins[13]
led_pin.mode = pingo.OUT

print "Loop..."
while True:
  led_pin.hi()
  print "Led ON"
  sleep(1)
  led_pin.lo()
  print "Led OFF\n"
  sleep(1)


