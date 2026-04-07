from datetime import date

# Usar date desde datetime
d = date(2020, 1, 1)
print(d)
print("Fecha actual:", d.today())  # fecha actual
# objeto date de hoy
today = date.today()
print("Año actual:", today.year)  # 2019
print("Mes actual:", today.month)  # 12
print("Día actual:", today.day)  # 5
