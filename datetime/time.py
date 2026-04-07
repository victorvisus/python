from datetime import time

# Representar tiempo con objetos time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute y second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute y second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)
