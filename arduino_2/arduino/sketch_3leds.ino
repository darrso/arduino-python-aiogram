/*
 * RED - 2dig
 * YELLOW - 3dig
 * GREEN - 4dig
 * 
 * 3 resistors
 * 1 ground
 * 
 * author - Darrso
 * telegram - @darrso
*/
int RED = 2;
int YEL = 3;
int GRE = 4;
String incoming;
void setup(){
  pinMode(RED, OUTPUT);
  pinMode(YEL, OUTPUT);
  pinMode(GRE, OUTPUT);
  digitalWrite(RED, HIGH);
  delay(2000);
  digitalWrite(RED, LOW);
  digitalWrite(YEL, HIGH);
  delay(2000);
  digitalWrite(YEL, LOW);
  digitalWrite(GRE, HIGH);
  delay(2000);
  digitalWrite(GRE, LOW);
  Serial.begin(9600);
   Serial.setTimeout(1);
  }
void loop(){
    while (Serial.available()){
  incoming =  Serial.readStringUntil('\n');}
    if (incoming == "off_red") {
      digitalWrite(RED, LOW);
    }
    if (incoming == "on_red") {
      digitalWrite(RED, HIGH);
    }
    if (incoming == "off_yel") {
      digitalWrite(YEL, LOW);
    }
    if (incoming == "on_yel") {
      digitalWrite(YEL, HIGH);
    }
    if (incoming == "off_gre") {
      digitalWrite(GRE, LOW);
    }
    if (incoming == "on_gre") {
      digitalWrite(GRE, HIGH);
    }
    delay(2000);
  }
