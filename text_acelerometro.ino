#include <Arduino_LSM9DS1.h>

//Librería para poder utilizar el botón de la placa 
#include <TinyMLShield.h>  

// Variable auxiliar que informa si el botón fue presionado
bool record = false;

void setup() {
  Serial.begin(9600);
  while (!Serial);

  // Inicializa el uso del botón, se puede ver en su definición 
  initializeShield();
  
  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }

  Serial.print("Accelerometer sample rate = ");
  Serial.print(IMU.accelerationSampleRate());
  Serial.println(" Hz");
  Serial.println();
  Serial.println("Acceleration in g's");
  Serial.println("X\tY\tZ");
}

void loop() {
    float x, y, z;
    if (IMU.accelerationAvailable()) {
        
      IMU.readAcceleration(x, y, z);

      Serial.print(x);
      Serial.print('\t');
      Serial.print(y);
      Serial.print('\t');
      Serial.print(z);
      Serial.print('\n');
    }
}