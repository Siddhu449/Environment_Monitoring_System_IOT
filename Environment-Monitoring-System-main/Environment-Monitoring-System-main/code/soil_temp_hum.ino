/*************************************************************
   Project: Smart Environment Monitor (ESP32 + DHT11 + Soil)
   Platform: Blynk IoT
*************************************************************/

#define BLYNK_TEMPLATE_ID "#Blynk"
#define BLYNK_TEMPLATE_NAME "#Your"
#define BLYNK_AUTH_TOKEN "#Your "

#include <WiFi.h>
#include <WiFiClient.h>
#include <BlynkSimpleEsp32.h>
#include <DHT.h>

// --- WiFi credentials ---
char ssid[] = ""; #wifi name
char pass[] = ""; #wifi password 

// --- DHT11 setup ---
#define DHTPIN 14       // ESP32 GPIO14 connected to DHT11 DATA
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// --- Soil sensor setup ---
const int soilPin = 34;      // GPIO34 (ADC)
const int dryValue = 3500;   // ADC value in dry soil
const int wetValue = 1000;   // ADC value in water

// --- Blynk Virtual Pins ---
#define VPIN_TEMP V1
#define VPIN_HUM  V2
#define VPIN_SOIL V0

BlynkTimer timer;

void sendSensorData() {
  // --- Soil moisture ---
  int rawSoil = analogRead(soilPin);
  int soilPercent = map(rawSoil, dryValue, wetValue, 0, 100);
  soilPercent = constrain(soilPercent, 0, 100);

  // --- DHT11 readings ---
  float temp = dht.readTemperature();
  float hum = dht.readHumidity();

  // --- Debug print ---
  Serial.print("Soil: ");
  Serial.print(soilPercent);
  Serial.println("%");

  if (!isnan(temp)) {
    Serial.print("Temp: ");
    Serial.print(temp);
    Serial.println(" °C");
    Blynk.virtualWrite(VPIN_TEMP, temp);
  } else {
    Serial.println("Temp: NAN (check wiring/resistor)");
  }

  if (!isnan(hum)) {
    Serial.print("Hum : ");
    Serial.print(hum);
    Serial.println(" %");
    Blynk.virtualWrite(VPIN_HUM, hum);
  } else {
    Serial.println("Hum : NAN (check wiring/resistor)");
  }

  // --- Push Soil to Blynk ---
  Blynk.virtualWrite(VPIN_SOIL, soilPercent);
}

void setup() {
  Serial.begin(115200);
  dht.begin();

  // Start Blynk
  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass);

  // Run function every 5 seconds
  timer.setInterval(5000L, sendSensorData);
}

void loop() {
  Blynk.run();
  timer.run();
}
