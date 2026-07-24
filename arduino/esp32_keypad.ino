#include <Keypad.h>

const byte ROWS = 4;
const byte COLS = 3;

char keys[ROWS][COLS] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};

byte rowPins[ROWS] = {23, 22, 21, 19};
byte colPins[COLS] = {18, 5, 4};

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

String input = "";

void setup() {
  Serial.begin(115200);
  delay(2000);
  Serial.println("Keypad Ready");
}

void loop() {
  char key = keypad.getKey();

  if (key) {

    if (key == '#') {
      Serial.println();  
      Serial.print("Entered PIN: ");
      Serial.println(input);
      input = "";  
    }

    else if (key == '*') {
      input = "";
      Serial.println();
      Serial.println("Cleared");
    }

    else {
      input += key;
      Serial.print("*");
    }
  }
}
