#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);
byte temp[8][8];

void setup()
{
  lcd.begin();
  lcd.backlight();
  lcd.print("Ogmgml602");
  lcd.clear();
  
  for(uint8_t j=0;j<8;j++){
        lcd.createChar(j,temp[j]);
      }
  lcd.home();
  // Initialize the serial port at a speed of 9600 baud
  Serial.begin(9600);
  lcd.print("On LCD1602");
  delay(20);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.write(byte(0));
  lcd.write(byte(1));
  lcd.write(byte(2));
  lcd.write(byte(3));
  lcd.setCursor(0, 1);
  lcd.write(byte(4));
  lcd.write(byte(5));
  lcd.write(byte(6));
  lcd.write(byte(7));
  Serial.flush();
}

void loop()
{
  
  if (Serial.available()>=64) {
    // Wait a bit for the entire message to arrive
    delay(5);
    for(uint8_t i=0;i<8;i++){
      Serial.readBytes(temp[i], 8);
      }
    for(uint8_t j=0;j<8;j++){
        lcd.createChar(j,temp[j]);
      }
  }
}
