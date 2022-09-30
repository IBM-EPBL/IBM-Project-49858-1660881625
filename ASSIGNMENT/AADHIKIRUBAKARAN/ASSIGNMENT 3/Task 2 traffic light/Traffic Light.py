void setup() 
{ 
  Serial.begin(9600); 
  pinMode(21, OUTPUT); 
  pinMode(20, OUTPUT);
  pinMode(19, OUTPUT);
}
 
void loop() 
{
  digitalWrite (21,HIGH);
  delay(5000);
  digitalWrite (21,LOW);
  digitalWrite(20, HIGH);
  delay(5000);
  digitalWrite(20, LOW);
  digitalWrite(19, HIGH);
  delay(5000);
  digitalWrite(19, LOW);
}
