# De entero a float
num_int = 10
print("num_int", num_int)  # 10
num_float = float(num_int)
print("num_float:", num_float)  # 10.0

# De float a entero
gravity = 9.81
print(int(gravity))  # 9

# De entero a cadena
num_int = 10
print(num_int)  # 10
num_str = str(num_int)
print(num_str)  # '10'

# De cadena a entero o float
num_str = "1000.86"
print(
    "num_int", int(float(num_str))
)  # 10 -- para convertir un "string decimal" a int primero debe pasar por float
print("num_float", float(num_str))  # 10.6
print(complex(num_str))

# De cadena a lista
first_name = "Asabeneh"
print(first_name)  # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)  # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
