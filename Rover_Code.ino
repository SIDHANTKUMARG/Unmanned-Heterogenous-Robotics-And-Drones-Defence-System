#include <Servo.h>
#include <LiquidCrystal.h>
#define Temp_Update 15
#define Init_Servo 90
#define Time_Init 333.333

const int pingPin = 9;
const int servoPin = 10;
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
Servo servoMotor;

void setup()
{
  pinMode(A2, OUTPUT);/*Input0*//*l293d*/
  pinMode(A3, OUTPUT);/*Input1*//*l293d*/
  pinMode(A4, OUTPUT);/*Input2*//*l293d*/
  pinMode(A5, OUTPUT);/*Input3*//*l293d*/
  
  lcd.begin(16, 2);
  Serial.begin(9600);
  servoMotor.attach(servoPin);
  servoMotor.write(Init_Servo);
  delay(Time_Init);
}

void loop()
{
  long duration;
  float cm;
  float droite_0,Gauche_0;
  int rand_direction;
  pinMode(pingPin, OUTPUT);         /* on prépare la pin pour envoyer le signal */
  digitalWrite(pingPin, LOW);       /* on commence a l'etat bas            */
  delayMicroseconds(2);             /* on attend pendant 2 µs                 */
  digitalWrite(pingPin, HIGH);      /* mise à l'état haut               */
  delayMicroseconds(10);            /* on attend pendant 10 µs                  */
  pinMode(pingPin, INPUT);          /* on prépare le pin pour recevoir un état  */
  duration = pulseIn(pingPin, HIGH);/*fonction pulseIn qui attend un état haut 
                    et renvoie le temps d'attente             */
  cm = microsecondsToCentimeters(duration);
  
  if(cm>332 ||cm<0)
  {   
     lcd.clear();
     Avancer();
     Servo_Moteur();
     lcd.print("pas d'obstacle  ");
    }
  else  
    {
    if(cm>31){
     Avancer();
     lcd.setCursor(0, 0);
   lcd.print("Distance en cm : ");
     lcd.setCursor(5, 1);
     lcd.print(cm);
     Servo_Moteur();
    }
    else
    {
     Stop();
     servoMotor.write(Init_Servo);
     delay(Time_Init);
     lcd.setCursor(0, 0);
   lcd.print("Test d'obstacle ");
     lcd.setCursor(5, 1);
     lcd.print(cm);
     delay(500);
     lcd.clear();
     lcd.setCursor(0, 0);
   lcd.print("Test adroite ");
     lcd.setCursor(5, 1);
     Servo_droite();
   lcd.print(Servo_droite());
     droite_0 = Servo_droite();
     delay(500);
     lcd.setCursor(0, 0);
   lcd.print("Test gauche ");
     lcd.setCursor(5, 1);
     Servo_Gauche();
     lcd.print(Servo_Gauche());
     Gauche_0 = Servo_Gauche();
     delay(500);
     if (droite_0 > Gauche_0)
     {
       droite();
     }
     else
     {
       if(droite_0 < Gauche_0)
       {
         Gauche();
       }
       else
       {
         if (droite_0 == Gauche_0 && droite_0 < 31)
         {
           Reculer();
         }
         else
         {
           rand_direction = random(200) ;
           if (rand_direction <= 100)
           {
             droite();
           }
           else
           {
             Gauche();
           }
         }
       }
     }  
    }
  }
  /*
  we have made calculations to make the project as realistic as possible
   we calculate the sum of the delays that of the servo motor
   we chose the Time_Init = 333.333 so that the sum of the lost temp
   is equal to 999.99 ms ~ 1s
   and we have V=d/s (d=distance s=temp)
   then from the angular velocity formula
   N(rpm) = (25/3piR) * V
   then assuming r=4cm and N=170rpm
   so the offset distance is 25 cm
   and the length of the car is estimated to be 18cm
   so Distance to stop is 18/3 + 25~31cm
   then 31 cm is the safest distance to escape from obstacles
   easier.
   */

}

/*Fonction permet de convertir microseconds ->centimetre
distance_mm = measure / 2.0 * SOUND_SPEED;
*/

float microsecondsToCentimeters(long microseconds) {
  return microseconds / 29 / 2;
}

void Avancer(){
 digitalWrite(A2,1);
 digitalWrite(A3,0);
 digitalWrite(A4,1);
 digitalWrite(A5,0);
}

void Reculer(){
 digitalWrite(A2,0);
 digitalWrite(A3,1);
 digitalWrite(A4,0);
 digitalWrite(A5,1);
 delay(500);
 if (random(100)>50)
 {
   digitalWrite(A2,1);
   digitalWrite(A3,0);
   digitalWrite(A4,0);
   digitalWrite(A5,1);
   delay(500);
 }
 else
 {
   digitalWrite(A2,0);
   digitalWrite(A3,1);
   digitalWrite(A4,1);
   digitalWrite(A5,0);
   delay(500);
 }
}

void Stop(){
 digitalWrite(A2,0);
 digitalWrite(A3,0);
 digitalWrite(A4,0);
 digitalWrite(A5,0); 
}

void droite(){
 digitalWrite(A2,1);
 digitalWrite(A3,0);
 digitalWrite(A4,0);
 digitalWrite(A5,1);
 delay(500);
}

void Gauche(){
 digitalWrite(A2,0);
 digitalWrite(A3,1);
 digitalWrite(A4,1);
 digitalWrite(A5,0);
 delay(500);
}
float Servo_Gauche(){
  servoMotor.write(0);
  delay(500);
  pinMode(pingPin, OUTPUT);         
  digitalWrite(pingPin, LOW);       
  delayMicroseconds(2);               
  digitalWrite(pingPin, HIGH);      
  delayMicroseconds(10);            
  pinMode(pingPin, INPUT);          
  servoMotor.write(Init_Servo);
  return microsecondsToCentimeters(pulseIn(pingPin, HIGH));
}
float Servo_droite(){
  servoMotor.write(180);
  delay(500);
  pinMode(pingPin, OUTPUT);         
  digitalWrite(pingPin, LOW);       
  delayMicroseconds(2);               
  digitalWrite(pingPin, HIGH);      
  delayMicroseconds(10);            
  pinMode(pingPin, INPUT);          
  servoMotor.write(Init_Servo);
  return microsecondsToCentimeters(pulseIn(pingPin, HIGH));
}

int Servo_Moteur(){
  servoMotor.write(70);
  delay(Time_Init);
  servoMotor.write(130);
  delay(Time_Init);
}
