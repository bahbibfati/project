import mysql.connector
import random
from time import *
config = {
    "user": "user_fati",
    "password": "root123BahbibP@ssword",
    "host": "localhost",
    "database": "fleet_management",
    "raise_on_warnings": True
}

def generate_values_status():
    temperature = round(random.uniform(10,80),2)  
    fuel_level = round(random.uniform(100,70),2) 
    pressure = round(random.uniform(100,120),2)  
    speed = round(random.randint(20,130),2)  
    return temperature, fuel_level, pressure, speed
def insert_status(temperature, fuel_level, pressure, speed):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        add_status = ("INSERT INTO vehicle "
                      "(temperature, fuel_level, pressure, speed) "
                      "VALUES (%s, %s, %s, %s)")
        data_status = (temperature, fuel_level, pressure, speed)
        cursor.execute(add_status, data_status)
        cnx.commit()
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(f"Failed to insert data: {err}")

def main():
    while True:
        temperature, fuel_level, pressure, speed = generate_values_status()
        print(f"Motor Temperature: {temperature:.2f}°C")
        print(f"Fuel Level: {fuel_level:.2f}%")
        print(f"Pressure: {pressure:.2f} bar")
        print(f"Speed: {speed} km/h")
        print("/ / / / / / / / / / / / / ")
        insert_status(temperature,fuel_level,pressure,speed)
        sleep(2)

if __name__ == "__main__":
    main()






