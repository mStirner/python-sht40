import smbus2
import time

# I2C-Adresse des SHT40-Sensors
SHT40_I2C_ADDRESS = 0x44

# I2C-Bus-Nummer, abhängig vom Raspberry Pi Modell (normalerweise 1)
I2C_BUS = 1

# Befehl zur Messung bei hoher Präzision
MEASURE_HIGH_PRECISION = 0xFD

def read_temperature_and_humidity():
    # I2C-Bus initialisieren
    bus = smbus2.SMBus(I2C_BUS)
    
    # Senden des Befehls für die Messung
    bus.write_byte(SHT40_I2C_ADDRESS, MEASURE_HIGH_PRECISION)
    time.sleep(0.015)  # Wartezeit für die Messung (15 ms)

    # Lese die 6 Bytes der Antwort
    data = bus.read_i2c_block_data(SHT40_I2C_ADDRESS, 0, 6)

    # Berechne Temperatur und Luftfeuchtigkeit aus den erhaltenen Daten
    temperature_raw = (data[0] << 8) + data[1]
    humidity_raw = (data[3] << 8) + data[4]

    # Umrechnung in Celsius
    temperature = -45 + 175 * (temperature_raw / 65535.0)

    # Umrechnung in relative Luftfeuchtigkeit
    humidity = 100 * (humidity_raw / 65535.0)

    return temperature, humidity

try:
    temperature, humidity = read_temperature_and_humidity()
    print(f"Temperatur: {temperature:.2f} °C")
    print(f"Luftfeuchtigkeit: {humidity:.2f} %")
except Exception as e:
    print(f"Fehler beim Auslesen des Sensors: {e}")
