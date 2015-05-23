
#include <Wire.h>
#include "rgb_lcd.h"
#include <SPI.h>
#include <SD.h>
const int pinTemp = A0;     
const int chipSelect = 4;
float temperature;
int B=3975;                 
float resistance;
rgb_lcd lcd;



void setup()
{
    Serial.begin(115200); 
   
    lcd.begin(16, 2);
    
    lcd.print("Temperature");
    
    Serial.print("Start write to card.");
  
 
    
    



 
  if (!SD.begin(chipSelect)) {
    Serial.println("No card or failure");
   
    return;
  }
  Serial.println("Card found");

}
void breath(unsigned char color)
{

    for(int i=0; i<255; i++)
    {
        lcd.setPWM(color, i);
        delay(5);
    }

    delay(500);
    for(int i=254; i>=0; i--)
    {
        lcd.setPWM(color, i);
        delay(5);
    }

}
void loop()
{
  
     if (temperature >25){
      breath(REG_RED);
      
      }
     if (temperature <25){
        breath(REG_GREEN);
        
        }
        
      if (temperature <20)
        {
          breath(REG_BLUE);
          }
          lcd.setCursor(5,1);
          lcd.write(0b11011111);
          lcd.setCursor(6,1);
          lcd.print("C");
 
    
    int val = analogRead(pinTemp);                               
    resistance=(float)(1023-val)*10000/val;                      
    temperature=1/(log(resistance/10000)/B+1/298.15)-273.15;    
    Serial.println(temperature);
    lcd.setCursor(0,1);
    lcd.print(temperature);
    
    
    
 
     
  String dataString = "";

 
  File dataFile = SD.open("datalog.txt", FILE_WRITE);

  if (dataFile) {
    dataFile.println(temperature);
    dataFile.close();
    
}
 
  else {
    Serial.println("error opening datalog.txt");
 
  
       
  } 
      
    
}
    
   
      

