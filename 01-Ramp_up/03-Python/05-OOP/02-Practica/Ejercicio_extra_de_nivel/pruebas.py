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