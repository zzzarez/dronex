import time
from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil

# Подключение к транспортному средству через MAVLink
vehicle = connect("tcp:127.0.0.1:5760", wait_ready=True)

# Взлет
vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True
vehicle.simple_takeoff(10)

# Ожидание завершения взлета
while not vehicle.is_armable:
    time.sleep(1)

# Перемещение вперед на 10 м
vehicle.simple_goto(LocationGlobalRelative(vehicle.location.global_frame.lat, vehicle.location.global_frame.lon + 0.01, vehicle.location.global_frame.alt))

# Ожидание завершения перемещения
while vehicle.mode.name != "LAND":
    time.sleep(1)

# Посадка
vehicle.mode = VehicleMode("LAND")

# Ожидание завершения посадки
while vehicle.armed:
    time.sleep(1)

# Закрытие соединения
vehicle.close()