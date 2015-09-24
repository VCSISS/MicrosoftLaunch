/*
 * ISSPseudo.c
 * 
 * The pseudocode for the Microsoft experiment.
 */

// MACROS MACROS MACROS MACROS MACROS
#define SECOND 1000

#define MINUTE SECOND * 60

#define HOUR MINUTE * 60

#define DAY HOUR * 24

// VARIABLES VARIABLES VARIABLES VARIABLES VARIABLES
int experimentCount;

// FUNCTION DECLARATIONS FUNCTION DECLARATIONS FUNCTION DECLARATIONS FUNCTION DECLARATIONS
void waitFor(int milliseconds);

void takePicture();

void turnOnLight();
void turnOffLight();

void turnOnVideo();
void turnOffVideo();

void turnOnMagnet();
void turnOffMagnet();

void recordData();

bool hasEnoughMemory();

void finish();

// SETUP SETUP SETUP SETUP SETUP
void setup() {

  experimentCount = 0;

  waitFor(HOUR * 4);
}

// LOOP LOOP LOOP LOOP LOOP
void loop() {

  turnOnLight();

  takePicture();

  turnOnVideo();
  waitFor(MINUTE + (SECOND * 15));

  turnOnMagnet();
  waitFor(MINUTE + (SECOND * 15));

  turnOffVideo();
  turnOffLight();
  turnOffMagnet();

  experimentCount++;
  recordData();

  if (!hasEnoughMemory()) {
    finish();
  }
  else {
    // *subject to change!*
    waitFor(SECOND * 30);
  }
}

// FUNCTION DEFINITIONS FUNCTION DEFINITIONS FUNCTION DEFINITIONS FUNCTION DEFINITIONS
void waitFor(int milliseconds)
{
  unsigned long t = millis();
  while (millis() < t + milliseconds) { }
}

void takePicture()
{
  
}

void turnOnLight()
{
  
}

void turnOffLight()
{
  
}

void turnOnVideo()
{
  
}

void turnOffVideo()
{
  
}

void turnOnMagnet()
{
  
}

void turnOffMagnet()
{
  
}

void recordData()
{
  
}

bool hasEnoughMemory()
{
  
}

void finish()
{
  while (true) { }
}

