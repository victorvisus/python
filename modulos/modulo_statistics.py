"""
Módulo statistics
El módulo statistics proporciona funciones de estadísticas para datos numéricos. Algunas funciones comunes definidas en este módulo: mean, median, mode, stdev, etc.
"""

from statistics import *  # importar todo del módulo statistics

ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))  # ~22.9
print(median(ages))  # 23
print(mode(ages))  # 20
print(stdev(ages))  # ~2.3
