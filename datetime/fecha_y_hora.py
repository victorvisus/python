from datetime import datetime

"""
Python datetime
Python tiene un módulo datetime para trabajar con fechas y horas.

import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
Con los comandos incorporados dir o help puedes ver las funciones disponibles de un módulo. Como ves, el módulo datetime tiene muchas clases y funciones; nos centraremos en date, datetime, time y timedelta. Veámoslas una a una.
"""

# Obtener información de datetime
now = datetime.now()
print(now)  # 2021-07-08 07:34:46.549883
day = now.day  # 8
month = now.month  # 7
year = now.year  # 2021
hour = now.hour  # 7
minute = now.minute  # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print("timestamp", timestamp)
print(f"{day}/{month}/{year}, {hour}:{minute}")  # 8/7/2021, 7:38
""" El timestamp, o Unix timestamp, es el número de segundos transcurridos desde el 1 de enero de 1970 UTC."""

# Formatear fecha con strftime --- https://strftime.net/
print(now.strftime("%d/%m/%Y, %H:%M"))  # 08/07/2021, 07:38
new_year = datetime(2020, 1, 1, 11, 10, 9, 235678)
print(new_year)  # 2020-01-01 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute)  # 1 1 2020 0 0
print(f"{day}/{month}/{year}, {hour}:{minute}")  # 1/1/2020, 0:0

# Usa el método strftime para formatear fechas y horas; la documentación de formatos está https://strftime.net/.
# fecha y hora actual
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("Hora:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# formato mm/dd/YY H:M:S
print("Formato uno:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# formato dd/mm/YY H:M:S
print("Formato dos:", time_two)

tiempo_local = now.strftime("%c")
print(tiempo_local)
time_local_two = now.strftime("%d - %b'%y")
print(time_local_two)


# Convertir cadena a fecha con strptime
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
