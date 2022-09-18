#include <LiquidCrystal.h>


///////////////////////////////////////////////////
//                         //
//         *** HOMEWORK PROJECTS ***       //
//      ----------------------------------   //
//            HI MAKERS, HELLO         //
//         IF YOU LIKE THIS PROGRAM      //
//           PLEASE GIVE A LIKE          //
//               IF YOU WANT...        //
//           THIS WILL HELP ME A LOT       //
//       TO SEE MORE OF MY PROJECTS,     //
//       PLEASE USE   =>    #GINDRO      //
//     ------------------------------------  //
//        THANKS.... GOOD WORK FOR YOU.    //
//                         //
///////////////////////////////////////////////////

//            DRONE = LCD DISPLAY
//-----------------------------------------------------

#include <Adafruit_LiquidCrystal.h>
Adafruit_LiquidCrystal lcd_1(0);

#include <IRremote.h>
int voltage[12];
IRrecv irrecv(12);
decode_results results;
unsigned long key_value = 0;

//-----------------------------------------------------
void setup()
{
  irrecv.enableIRIn();
  irrecv.blink13(true);  

  lcd_1.begin(16, 2);
  lcd_1.setCursor(0, 0);
  lcd_1.print("*  HI MAKERS  *");
  lcd_1.setCursor(0, 1);
  lcd_1.print(" DRONE PROJECT ");
  delay(500);
  lcd_1.clear();  
  lcd_1.setCursor(0, 0);
  lcd_1.print("* DRONE  READ *");
  lcd_1.setCursor(0, 1);
  lcd_1.print("*    TO FLY   *");
}

//-----------------------------------------------------
void loop()
{
  TranslateIR();
}


//-----------------------------------------------------
void TranslateIR() //-----TranslateIR-----
{
  if (irrecv.decode(&results))
  {
        if (results.value == 0XFFFFFFFF)
          results.value = key_value;

        switch(results.value)
        {
          case 0xFD00FF://power
        lcd_1.clear();            
          lcd_1.setCursor(0, 0);
          lcd_1.print("BUTTON POWER= 1");
          lcd_1.setCursor(0, 1);
          lcd_1.print("DRONE POWER ON ");
          break;
          
          case 0xFD40BF://func/stop 
          lcd_1.clear();           
          lcd_1.setCursor(0, 0);
          lcd_1.print("BUTTON STOP = 3");
          lcd_1.setCursor(0, 1);
          lcd_1.print("DRONE POWER OFF");         
          break;
       
          case 0xFD30CF://0
        lcd_1.clear();           
          lcd_1.setCursor(0, 0);
          lcd_1.print("BUTTON = 0     ");
          lcd_1.setCursor(0, 1);
          lcd_1.print("NO FUNCTION    ");
          break ; 
          
          case 0xFD08F7://1 
          lcd_1.clear();           
          lcd_1.setCursor(0, 0);
          lcd_1.print("BUTTON 1= POWER");
          lcd_1.setCursor(0, 1);
          lcd_1.print("DRONE POWER ON ");
          break ;
          
          case 0xFD8877://2  
        lcd_1.clear();           
          lcd_1.setCursor(0, 0);
          lcd_1.print("BUTTON 2 = VOL+");
          lcd_1.setCursor(0, 1);
          lcd_1.print("DRONE FLY LEFT ");
          break ;
          
          case 0xFD48B7://3 
          lcd_1.clear();           
          lcd_1.setCursor(0, 0);
          lcd_1.print("BUTTON 3 = STOP");
          lcd_1.setCursor(0, 1);
          lcd_1.print("DRONE POWER OFF");
          break ;
         
          case 0xFD28D7://4 
        lcd_1.clear();                
          lcd_1.setCursor(0, 0);
          lcd_1.print("BUTTON 4 = |<< ");
          lcd_1.setCursor(0, 1);
          lcd_1.print("DRONE FLY BACK ");
          break ;
          
          case 0xFDA857://5  
        lcd_1.clear();           
          lcd_1.setCursor(0, 0);
          lcd_1.print("BUTTON 5 = >|| ");
          lcd_1.setCursor(0, 1);
          lcd_1.print("DRONE FLY UP   ");
          break ;
          
          case 0xFD6897://6 
        lcd_1.clear();           
          lcd_1.setCursor(0, 0);
          lcd_1.print("BUTTON 6 = >>| ");
          lcd_1.setCursor(0, 1);
          lcd_1.print("DRONE  FORWARD ");
          break ;
          
          case 0xFD18E7://7 
      digitalWrite(2, HIGH);
      digitalWrite(3, HIGH);
          lcd_1.clear();           
          lcd_1.setCursor(0, 0);
          lcd_1.print("BUTTON 7 = DOWN");
          lcd_1.setCursor(0, 1);
          lcd_1.print("LED LCD ON     ");
          break ;
          
          case 0xFD9867://8  
        lcd_1.clear();           
          lcd_1.setCursor(0, 0);
          lcd_1.print("BUTTON 8 = VOL-");
          lcd_1.setCursor(0, 1);
          lcd_1.print("DRONE FLY RIGHT");
          break ;
          
          case 0xFD58A7://9 
          lcd_1.clear();           
          lcd_1.setCursor(0, 0);
          lcd_1.print("BUTTON 9 = UP  ");
          lcd_1.setCursor(0, 1);
          lcd_1.print("LED DRONE ON   ");
          break ; 
          
          case 0xFD807F://vol+
        lcd_1.clear();           
          lcd_1.setCursor(0, 0);
          lcd_1.print("BUTTON VOL+ = 2");
          lcd_1.setCursor(0, 1);
          lcd_1.print("DRONE FLY LEFT ");          
          break ;  
          
        case 0xFD906F://vol-
        lcd_1.clear();           
          lcd_1.setCursor(0, 0);
          lcd_1.print("BUTTON VOL- = 8");
          lcd_1.setCursor(0, 1);
          lcd_1.print("DRONE FLY RIGHT"); 
          break ;  
          
          case 0xFDA05F://>|| 
        lcd_1.clear();           
          lcd_1.setCursor(0, 0);
          lcd_1.print("BUTTON >|| = 5 ");
          lcd_1.setCursor(0, 1);
          lcd_1.print("DRONE FLY UP   "); 
          break ;
          
          case 0xFD20DF://|<<
        lcd_1.clear();           
          lcd_1.setCursor(0, 0);
          lcd_1.print("BUTTON |<< = 4 ");
          lcd_1.setCursor(0, 1);
          lcd_1.print("DRONE FLY BACK ");          
          break ; 
          
          case 0xFD609F://>>| 
        lcd_1.clear();           
          lcd_1.setCursor(0, 0);
          lcd_1.print("BUTTON >>|= 6  ");
          lcd_1.setCursor(0, 1);
          lcd_1.print("DRONE  FORWARD ");           
          break ;
          
          case 0xFD10EF://down arrow 
          lcd_1.clear();           
          lcd_1.setCursor(0, 0);
          lcd_1.print("BUTTON DOWN = 7");
          lcd_1.setCursor(0, 1);
          lcd_1.print("LED LCD ON     ");        
          break ; 
          
          case 0xFD50AF://up arrow
          lcd_1.clear();           
          lcd_1.setCursor(0, 0);
          lcd_1.print("BUTTON UP = 9  ");
          lcd_1.setCursor(0, 1);
          lcd_1.print("LED DRONE ON   ");           
          break ;
          
          case 0xFDB04F://eq
        lcd_1.clear();           
          lcd_1.setCursor(0, 0);
          lcd_1.print("BUTTON = EQ    ");
          lcd_1.setCursor(0, 1);
          lcd_1.print("NO FUNCTION    ");            
          break ;  
          
          case 0xFD708F://st/rept
        lcd_1.clear();           
          lcd_1.setCursor(0, 0);
          lcd_1.print("BUTTON =  REPT ");
          lcd_1.setCursor(0, 1);
          lcd_1.print("NO FUNCTION    ");         
          break ;          
          
        }
        key_value = results.value;
        irrecv.resume(); 
  }
}
//-----------------------------------------------------
