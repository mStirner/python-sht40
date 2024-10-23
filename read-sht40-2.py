import smbus2
import time

# I2C-Adresse des SHT40-Sensors
SHT40_I2C_ADDRESS = 0x44

# I2C-Bus-Nummer (meistens 1 auf Raspberry Pi)
I2C_BUS = 1

# Befehle für den SHT40-Sensor
SOFT_RESET = 0x94
MEASURE_LOWEST_PRECISION = 0xE0

def soft_reset():
    """Führt einen Soft-Reset des Sensors durch."""
    bus = smbus2.SMBus(I2C_BUS)
    bus.write_byte(SHT40_I2C_ADDRESS, SOFT_RESET)
    time.sleep(0.01)  # Wartezeit von 10 ms
    bus.close()

def read_temperature_and_humidity():
    """Liest Temperatur und Luftfeuchtigkeit vom Sensor."""
    # I2C-Bus initialisieren
    bus = smbus2.SMBus(I2C_BUS)
    
    # Senden des Befehls für eine Messung mit niedriger Präzision
    bus.write_byte(SHT40_I2C_ADDRESS, MEASURE_LOWEST_PRECISION)
    time.sleep(0.02)  # Wartezeit von 20 ms für die Messung

    # Lese die 6 Bytes der Antwort
    data = bus.read_i2c_block_data(SHT40_I2C_ADDRESS, 0, 6)

    # Berechne Temperatur und Luftfeuchtigkeit aus den erhaltenen Daten
    temperature_raw = (data[0] << 8) + data[1]
    humidity_raw = (data[3] << 8) + data[4]

    # Umrechnung in Celsius
    temperature = -45 + 175 * (temperature_raw / 65535.0)

    # Umrechnung in relative Luftfeuchtigkeit
    humidity = 100 * (humidity_raw / 65535.0)

    bus.close()
    return temperature, humidity

def main():
    """Hauptfunktion zum Auslesen und Anzeigen der Messwerte."""
    try:
        # Soft-Reset des Sensors durchführen
        soft_reset()
        
        # Mehrfach Messungen durchführen
        for _ in range(5):
            temperature, humidity = read_temperature_and_humidity()
            print(f"Temperatur: {temperature:.2f} °C")
            print(f"Luftfeuchtigkeit: {humidity:.2f} %")
            time.sleep(0.5)  # Wartezeit zwischen den Messungen
    except Exception as e:
        print(f"Fehler beim Auslesen des Sensors: {e}")

if __name__ == "__main__":
    main()
