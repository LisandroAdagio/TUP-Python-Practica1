"""Coerción a Booleanos"""


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_01
"""

A = 5

# COMPLETAR - INICIO
variable_01 = True if A == 5 else False
print(variable_01)
# COMPLETAR - FIN

assert variable_01 is True


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_02
"""

Domicilio = ""

# COMPLETAR - INICIO
variable_02 = True if  Domicilio == "Calle Falsa 123" else False
print(variable_02)
# COMPLETAR - FIN

assert variable_02 is False


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_03
"""

Domicilio = "Alsina 2446" or "Pueyrredón y la vía"

# COMPLETAR - INICIO
variable_03 = True if Domicilio == "Alsina 2446" or Domicilio == "Pueyrredón y la vía" else False
print(variable_03)
# COMPLETAR - FIN

assert variable_03 is True


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_04
"""

lista_de_compras = "No comprar nada" and ["Pan", "Aceite", "Sal"]

# COMPLETAR - INICIO
if lista_de_compras == "No comprar nada":
    variable_04 = True
elif lista_de_compras == ["Pan", "Aceite", "Sal"]:
    variable_04 = True
else:
    variable_04 = False
print(variable_04)
# COMPLETAR - FIN

assert variable_04 is True


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_05
"""

lista_de_ids = 0 and [1236, 5565, 8956, 2534]

# COMPLETAR - INICIO
variable_05 = bool(lista_de_ids)
print(variable_05)
# COMPLETAR - FIN

assert variable_05 is False


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_06
"""

diccionario = {} and {"Nombre": "Alberto Paz", "DNI": 12365855}

# COMPLETAR - INICIO
variable_06 = bool(diccionario)
print(variable_06)
# COMPLETAR - FIN

assert variable_06 is False