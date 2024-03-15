import pymysql
import random
from time import sleep

config = {
    "user": "root",
    "password": "root123BahbibP@ssword",
    "host": "localhost",
    "database": "fleet",
}

def create_vehicle_table(vehicle_id):
    """
    Creates a table for a vehicle if it doesn't exist.
    """
    table_name = f"vehicle_{vehicle_id}"
    try:
        cnx = pymysql.connect(**config)
        cursor = cnx.cursor()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                temperature DECIMAL(5, 2),
                fuel_level DECIMAL(5, 2),
                pressure DECIMAL(5, 2),
                speed INT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        cnx.commit()
    except pymysql.Error as err:
        print(f"Failed to create table for vehicle {vehicle_id}: {err}")
    finally:
        cursor.close()
        cnx.close()

def insert_status(vehicle_id, temperature, fuel_level, pressure, speed):
    """
    Inserts the status into the vehicle's table.
    """
    table_name = f"vehicle_{vehicle_id}"
    try:
        cnx = pymysql.connect(**config)
        cursor = cnx.cursor()
        add_status = (f"INSERT INTO {table_name} "
                      "(temperature, fuel_level, pressure, speed) "
                      "VALUES (%s, %s, %s, %s)")
        data_status = (temperature, fuel_level, pressure, speed)
        cursor.execute(add_status, data_status)
        cnx.commit()
    except pymysql.Error as err:
        print(f"Failed to insert data into table for vehicle {vehicle_id}: {err}")
    finally:
        cursor.close()
        cnx.close()


def create_car(n):
    return n

def generate_values_status():
    """
    Generates random values for temperature, fuel level, pressure, and speed.
    """
    temperature = round(random.uniform(10, 80), 2)
    fuel_level = round(random.uniform(70, 100), 2)
    pressure = round(random.uniform(100, 120), 2)
    speed = random.randint(20, 130)
    return temperature, fuel_level, pressure, speed

def main():
    n=0

    vehicle_ids = ['1', '2', '3','4']  
    for vehicle_id in range(n):
        pass
    n=create_car(n)
        

    while n>0:
        for vehicle_id in range(n):
            create_vehicle_table((vehicle_id))
            temperature, fuel_level, pressure, speed = generate_values_status()
            print(f"Vehicle ID: {vehicle_id} | Motor Temperature: {temperature:.2f}°C | Fuel Level: {fuel_level:.2f}% | Pressure: {pressure:.2f} bar | Speed: {speed} km/h")
            insert_status(vehicle_id, temperature, fuel_level, pressure, speed)
        sleep(4)  

if __name__ == "__main__":
    main()
