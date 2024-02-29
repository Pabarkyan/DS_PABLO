# Modelo de machine learning

"""
    El modelo consistira en averiguar que combinacion de ataque, vida , velocidad de ataque, armadura y clase son las mas
    optimas para detorrar a cada  uno de los monstruos.
"""

#import clases
"""
def ML():
    clases.jugar()."""

import sys
from io import StringIO

# Guarda la entrada estándar original
entrada_original = sys.stdin

# Simula la entrada
sys.stdin = StringIO('respuesta simulada\n')

# Ahora, input() usará la entrada simulada
respuesta = input("Por favor, introduce algo: ")
print("Simulaste la entrada:", respuesta)

# Restaura la entrada estándar original
sys.stdin = entrada_original

    
