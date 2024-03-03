import random

def seleccionar_turno(velocidad_personaje, velocidad_monstuo):
    diff = abs(velocidad_monstuo - velocidad_personaje)
    probabilidad_base = 1/(diff + 1)

    probabilidad_personaje = probabilidad_base *(1.0  +  velocidad_personaje*0.01)
    probabilidad_monstruo = probabilidad_base *(1.0  +  velocidad_monstuo*0.01)
    total_probabilidad = probabilidad_monstruo + probabilidad_personaje
    
    probabilidad_personaje /= total_probabilidad
    probabilidad_monstruo /= total_probabilidad
    
    # Usamos random.choices() para seleccionar aleatoriamente un número
    seleccion_de_turno = random.choices(["tu", "monstruo"], weights=[probabilidad_personaje, probabilidad_monstruo])[0]
    
    return seleccion_de_turno

contadormonstruo = 0
contadortu = 0
for i in range(100):
    numero_seleccionado = seleccionar_turno(300, 60)
    if numero_seleccionado == "tu":
        contadortu += 1
    else:    
        contadormonstruo += 1
dicc = {
    "tu": contadortu,
    "monstruo": contadormonstruo,
    "factor": contadortu/contadormonstruo
}
print(dicc)


diccc = {
    1: 0,
    2: 0,
    3: 0
}
for i in range(102):
    numero_aleatorio = random.choices([1, 2, 3])[0]
    if numero_aleatorio == 1:
        diccc[1] += 1
    elif numero_aleatorio == 2:
        diccc[2] += 1
    else:
        diccc[3] += 1
print(diccc)


def pruebas():
    fuerza = random.randint(1, 200)
    if fuerza == 200:
        velocidad = 0
        armadura = 0
    else:        
        velocidad = random.randint(0, 200 - fuerza)
        armadura = 200 - fuerza - velocidad
    caracteristicas = {
        "fuerza": fuerza,
        "velocidad": velocidad,
        "armadura": armadura,
        "total": fuerza + armadura+ velocidad
    }
    return caracteristicas

print(pruebas())

print(random.choices([1, 2, 3])[0])


# funcion de chat gpt

diccionario1 = {'clave1': 10, 'clave2': 22, 'clave3': 30}
diccionario2 = {'clave1': 10, 'clave2': 20, 'clave3': 35}
diccionario3 = {'clave1': 10, 'clave2': 20, 'clave3': 40}

# Lista de diccionarios para comparar
diccionarios = [diccionario1, diccionario2, diccionario3]

# Claves que quieres comparar
claves_a_comparar = ['clave1', 'clave2']

# Función para comparar valores de claves específicas en una lista de diccionarios
def comparar_claves(diccionarios, claves):
    # Iterar sobre cada clave que queremos comparar
    for clave in claves:
        # Obtener el valor de la primera entrada para la clave actual
        valor_inicial = diccionarios[0][clave]
        
        # Comparar el valor de la clave en todos los diccionarios
        for diccionario in diccionarios:
            if diccionario[clave] != valor_inicial:
                return False # Si algún valor no coincide, retorna False
    return True # Si todos los valores coinciden, retorna True

# Llamada a la función
resultado = comparar_claves(diccionarios, claves_a_comparar)

if resultado:
    print("Los valores son iguales para las claves especificadas en todos los diccionarios.")
else:
    print("Los valores no son iguales para las claves especificadas en todos los diccionarios.")


# Lista de diccionarios para analizar
diccionarios = [
    {'clave1': 'A', 'clave2': 'B', 'clave3': 'C'},
    {'clave1': 'A', 'clave2': 'B', 'clave3': 'D'},
    {'clave1': 'A', 'clave2': 'B', 'clave3': 'C'},
    {'clave1': 'B', 'clave2': 'B', 'clave3': 'C'},
    {'clave1': 'A', 'clave2': 'C', 'clave3': 'C'}
]

# Claves que quieres comparar
claves_a_comparar = ['clave1', 'clave2']

# Función para contar coincidencias de combinaciones de valores para claves específicas
def contar_coincidencias(diccionarios, claves):
    combinaciones = {}
    for diccionario in diccionarios:
        # Crear una tupla con los valores de las claves especificadas
        valores_claves = tuple(diccionario[clave] for clave in claves)
        # Contar cada combinación única
        if valores_claves in combinaciones:
            combinaciones[valores_claves] += 1
        else:
            combinaciones[valores_claves] = 1
    
    return combinaciones

# Llamada a la función y mostrar resultados
combinaciones = contar_coincidencias(diccionarios, claves_a_comparar)
for combinacion, cantidad in combinaciones.items():
    print(f"Combinación {combinacion}: {cantidad} veces")

# Para obtener solo las combinaciones con más de una coincidencia
print("\nCombinaciones con más de una coincidencia:")
for combinacion, cantidad in combinaciones.items():
    if cantidad > 1:
        print(f"Combinación {combinacion}: {cantidad} veces")
