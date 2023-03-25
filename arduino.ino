// carrega a biblioteca AFMotor
#include <AFMotor.h>

AF_DCMotor motor1(1); // Define o motor1 ligado a conexao 1
AF_DCMotor motor2(4);  // Define o motor2 ligado a conexao 4
 
void setup()
{
  motor1.setSpeed(255); // Define a velocidade máxima para os motores 1 e 2
  motor2.setSpeed(255); 
}

void loop()
{
  if (Serial.available() > 0) {
    char comando = Serial.read(); // lê o dado recebido
    delay(100); // aguarda a leitura completa do dado
    
    switch (comando) {
      case 'T': // caso receba a letra 'T', o carrinho se move para frente
        motor1.run(FORWARD); 
        motor2.run(FORWARD);
        break;
      case 'B': // caso receba a letra 'B', o carrinho se move para trás
        motor1.run(BACKWARD); 
        motor2.run(BACKWARD);
        break;
      case 'R': // caso receba a letra 'R', o carrinho vira para a direita
        motor1.run(FORWARD);
        motor2.run(RELEASE);
        break;
      case 'L': // caso receba a letra 'L', o carrinho vira para a esquerda
        motor1.run(RELEASE);
        motor2.run(FORWARD);
        break;
      default: // caso não receba nenhuma letra, os motores são desligados
        motor1.run(RELEASE);
        motor2.run(RELEASE);
        break;
    }
  }
}