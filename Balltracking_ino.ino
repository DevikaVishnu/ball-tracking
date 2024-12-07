#define I1 9 // Control pin 1 for motor 1
#define I2 6 // Control pin 2 for motor 1
#define I3 11 // Control pin 1 for motor 2
#define I4 10 // Control pin 2 for motor 2

// Include the Servo library 
#include <Servo.h> 
//Defining vaiable
char a;
int angle = 15;
int speed = 3;
int originalleft = 80;
int originalright = 65;
int complete = 'i';

// Declare the Servo pin 
int ArmServoPin = 7 ;
int HookServoPin = 4 ;
// Create a servo object 
Servo ArmServo;  
Servo HookServo;
void setup() {
  // put your setup code here, to run once:
  HookServo.attach(HookServoPin);
  ArmServo.attach(ArmServoPin);
  complete = 'i';
  // put your setup code here, to run once:
  //DCMotor1
  pinMode(I1, OUTPUT);
  pinMode(I2, OUTPUT);

  //DCMotor2
  pinMode(I3, OUTPUT);
  pinMode(I4, OUTPUT);

  Serial.begin(9600);

}

void loop() {
      HookServo.write(0);
      ArmServo.write(13);
      if(Serial.available()>0)
        {
          a=Serial.read();
      
          //Forward
          if(a =='f') 
          {
            //DCMotor 1
            analogWrite(I2, 80);
            digitalWrite(I1, LOW);
            //DCMotor 2
            analogWrite(I3, 62);
            digitalWrite(I4, LOW);
          }
         /* if(a =='l')
          {
            originalright = originalright - speed;
            //DCMotor 1
            analogWrite(I2, originalleft);
            digitalWrite(I1, LOW);
            //DCMotor 2
            analogWrite(I3, originalright);
            digitalWrite(I4, LOW);
          }
          if(a =='r')
          {
            originalleft = originalleft - speed;
            //DCMotor 1
            analogWrite(I2, originalleft);
            digitalWrite(I1, LOW);
            //DCMotor 2
            analogWrite(I3, originalright);
            digitalWrite(I4, LOW);
          }*/
          if(a =='s')
          { if (complete == 'i')
             {
              //DCMotor 1
              analogWrite(I2, 0);
              digitalWrite(I1, LOW);

              //DCMotor 2
              analogWrite(I3, 0);
              digitalWrite(I4, LOW);
             
              ArmServo.write(45);
              delay(500);
              HookServo.write(90);
              ArmServo.write(15);
              complete = 'c';
              } 
            
          }
   
 
        //ServoMotor1
        //ArmServo.write(angle);
        }
  
  }

