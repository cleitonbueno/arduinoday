#define PINLED            13
#define BAUDRATE          115200
#define CMD_LIGA_LED      108
#define CMD_DESLIGA_LED   100



void setup(){
  Serial.begin(BAUDRATE);
  pinMode(PINLED, OUTPUT); 
}

void loop(){
  if (Serial.available() > 0) {
    unsigned char cmd_rx = Serial.read();
    if (cmd_rx == CMD_LIGA_LED) { // letra l -> LIGAR
      digitalWrite(PINLED, HIGH);
    }
    else if (cmd_rx == CMD_DESLIGA_LED) { // letra d -> DESLIGAR
      digitalWrite(PINLED, LOW);
    }
  }
}
