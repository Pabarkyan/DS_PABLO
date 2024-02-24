# Mi juego: crea una clase armas y una clase monstruo, crea funciones que interaccionen entre ellos, crea personajes que solo puedan usar unas determinadas armas

# asignacion de clases

lista_personajes = [] # lista vacia donde guardaremos todos los personajes que vayamos creando

class Personaje:
    estado = True # Es tru si el personaje esta vivo, False si murio
    def __init__(self, nombre, vida, daño_base, velocidad_de_ataque, armadura, nivel=1):
        self.nombre = nombre
        self.vida = vida
        self.nivel = nivel
        self.daño = daño_base
        self.velocidadAtaque = velocidad_de_ataque
        self.armadura = armadura

    def __repr__(self): # Con esto definimos como queremos que nos devuelva un objeto
        return f'{self.nombre} |   clase: {self.clase} |   vida: {self.vida} |  nivel: {self.nivel} |  daño: {self.daño} |  velocidad de ataque: {self.velocidadAtaque} |  armadura: {self.armadura}'

    def subir_de_nivel(self, aumento):
        self.nivel = self.nivel + aumento

    def perder_vida(self, daño_recibido): # Todos los aumentos pueden ser decrementos siempre que usemos numeros negativos
        self.vida = self.vida - daño_recibido
        if self.vida <= 0:
            self.estado = False
            print("Su personaje murio, creese otro o resucitelo")
    
    def aumentar_daño(self, aumento):
        self.vida = self.vida + aumento

    def aumentar_velocidad_de_ataque(self, aumento):
        self.vida = self.vida + aumento

    def aumentar_armadura(self, aumento):
        self.vida = self.vida + aumento

    def restar_puntos_en_la_creacion(puntos, resta):
        puntos = puntos - resta
        if puntos <= 0:
            print("Se paso de sus puntos, repita la creacion de personaje")
            
        return puntos

    def mostrar_personajes(lista_personajes): # Muestra todos los personajes creados de la forma que asignamos en __repr__
        for i in lista_personajes:
            print(i)

#--------------Creacion de clases para los personajes------------------------

class Mago(Personaje):
    def __init__(self, nombre, vida, daño_base, velocidad_de_ataque, armadura, arma = None, clase = "Guerrero" , nivel=1, mana = 500):
        super().__init__(vida, daño_base, velocidad_de_ataque, armadura, nivel)
        self.nombre = nombre
        self.vida = vida
        self.nivel = nivel
        self.daño = daño_base
        self.velocidadAtaque = velocidad_de_ataque
        self.armadura = armadura
        self.clase = clase
        self.arma = arma
        self.mana = mana + self.nivel*2 + 200 # Cada habilidad tiene un costo en mana para evitar que se use la habilidad mas poderosa, y tengas que usar estrategia
        self.habilidades = {
            "bola de fuego": {
                "daño": 25 + self.nivel*0.1 + daño_base,
                "mana": -15, 
                "vida": 0,
                "armadura": 0,
                "velocidad": self.velocidadAtaque
            },
            "barrera": {
                "daño": 0,
                "mana": -15, 
                "vida": 20,
                "armadura": 50,
                "velocidad": self.velocidadAtaque
            },
            "bola de hielo": {
                "daño": 25 + self.nivel*0.1 + daño_base,
                "mana": -30, 
                "vida": 0,
                "armadura": 0,
                "velocidad": self.velocidadAtaque
            }
        }
        self.armas = ["bastones"] # Armas que puede utilizar el personaje

class Guerrero(Personaje):
    def __init__(self, nombre, vida, daño_base, velocidad_de_ataque, armadura, arma = None, clase = "Guerrero" , nivel=1, mana = 100):
        super().__init__(vida, daño_base, velocidad_de_ataque, armadura, nivel)
        self.nombre = nombre
        self.vida = vida
        self.nivel = nivel
        self.daño = daño_base
        self.velocidadAtaque = velocidad_de_ataque
        self.armadura = armadura
        self.clase = clase
        self.mana = mana + self.nivel*1.5
        self.armadura = self.armadura + 500
        self.vida = self.vida + 100
        self.daño = self.daño - 30
        self.arma = arma
        self.habilidades = {
            "embate": {
                "daño": 35 + self.nivel*0.1 + daño_base,
                "mana": -15, 
                "vida": 0,
                "armadura": 0,
                "velocidad": self.velocidadAtaque + 20
            },
            "defensa": {
                "daño": 0,
                "mana": -15, 
                "vida": 20,
                "armadura": 50,
                "velocidad": self.velocidadAtaque
            },
            "golpe mortal": {
                "daño": 80 + self.nivel*0.1  + daño_base,
                "mana": -60, 
                "vida": 0,
                "armadura": 0,
                "velocidad": self.velocidadAtaque - 10
            }
        }
        self.armas = ["espadas", "mazas", "hachas"]


class Acechador(Personaje):
    def __init__(self, nombre, vida, daño_base, velocidad_de_ataque, armadura, arma = None, clase = "Acechador" ,nivel=1, mana = 300):
        super().__init__(vida, daño_base, velocidad_de_ataque, armadura, nivel)
        self.nombre = nombre
        self.vida = vida
        self.nivel = nivel
        self.daño = daño_base
        self.velocidadAtaque = velocidad_de_ataque
        self.armadura = armadura
        self.clase = clase
        self.arma = arma
        self.mana = mana + self.nivel*1.5
        self.velocidadAtaque = self.velocidadAtaque + 200
        self.habilidades = {
            "puñalada": {
                "daño": 20 + self.nivel*0.1  + daño_base,
                "mana": -15, 
                "vida": 0,
                "armadura": 0,
                "velocidad": self.velocidadAtaque + 20
            },
            "esfumar": {
                "daño": 0,
                "mana": -100, 
                "vida": 200,
                "armadura": 0,
                "velocidad": self.velocidadAtaque
            },
            "afilar": {
                "daño": 0 + self.nivel*0.1 + daño_base,
                "mana": -40, 
                "vida": 0,
                "armadura": 0,
                "velocidad": self.velocidadAtaque + 100
            }
        }
        self.armas = ["dagas"] 

#--------------- Creacion de armas para los personajes ------------------------

class Armas:
    def __init__(self, nombre, tipo, daño, velocidad):
        self.nombre = nombre
        self.tipo = tipo
        self.daño = daño
        self.velocidad = velocidad

    def __repr__(self):
        return f'{self.nombre} |   tipo: {self.tipo} |  daño: {self.daño} |  daño: {self.daño} |  velocidad de ataque: {self.velocidad}'

class Bastones(Armas):
    def __init__(self, nombre, tipo = "Baston", daño = 10, velocidad = 10):
        super().__init__(nombre, tipo, daño, velocidad)
        self.nombre = nombre

class Espadas(Armas):
    def __init__(self, nombre, tipo = "Espada", daño = 70, velocidad = 40):
        super().__init__(nombre, tipo, daño, velocidad)
        self.nombre = nombre

class Dagas(Armas):
    def __init__(self, nombre, tipo = "Dagas", daño = 60, velocidad = 100):
        super().__init__(nombre, tipo, daño, velocidad)
        self.nombre = nombre

class Hachas(Armas):
    def __init__(self, nombre, tipo = "Hacha", daño = 80, velocidad = 10):
        super().__init__(nombre, tipo, daño, velocidad)
        self.nombre = nombre

class Maza(Armas):
    def __init__(self, nombre, tipo = "Maza", daño = 100, velocidad = 90):
        super().__init__(nombre, tipo, daño, velocidad)
        self.nombre = nombre

# -------------- Definimos los monstruos con los que lucharemos -----------------

class Monstruos:
    def __init__(self, nombre, dificultad, vida, experiencia, velocidad, daño):
        self.nombre = nombre
        self.dificultad = dificultad
        self.vida = vida
        self.experiencia = experiencia # Cantidad de nivel que subes al derrotarlo
        self.velocidad = velocidad
        self.daño = daño

    def __repr__(self):
        return f'{self.nombre} |   vida: {self.vida} |  dificultado: {self.dificultad} |  daño: {self.daño} |  velocidad de ataque: {self.velocidad} |  recompensa de experiencia: {self.experiencia}'


# -------------------Elementos creados para el juego, monstruos y armas--------------------

cthulhu = Monstruos(nombre="cthulhu", dificultad="dificil", vida= 1000, experiencia= 10, velocidad= 30, daño=30)
Leon_de_Amenea = Monstruos(nombre="Leon de Amenea", dificultad="media", vida= 30, experiencia= 7, velocidad= 20, daño=10)
Minotauro = Monstruos(nombre="Minotauro", dificultad="dificil", vida= 2000, experiencia= 50, velocidad= 30, daño=30)

lista_de_monstruos = [cthulhu, Leon_de_Amenea, Minotauro]

Baston_de_Gandalf = Bastones("Baston de Gandalf", "Baston", 200, 10)
Excalibur = Bastones("Escalibur", "Espada", 100, 70)
Mjölnir = Bastones("Mjölnir", "Maza", 90, 40)
Tizona = Bastones("Tizona", "Dagas", 40, 300)
Fragarach = Bastones("Fragarach", "Hacha", 90, 40)

lista_de_armas = [Baston_de_Gandalf, Excalibur, Mjölnir, Tizona, Fragarach]

# ----------------------funciones del juego-----------------

# ----------------------Creacion de Personajes-------------------, he intentado separar la funcion crear_personake() en 3 funciones pero da muchos errores con la herencia (complica las cosas innecesariamente a pesar de ser una buena practica)

def crear_personaje(lista_personajes): # Caracteristicas base del personaje
    try:
        print("Reparta sus puntos entre daño, velocidad, armadura o velocidad, tiene 200 puntos, repartalo sabiamente ")
        puntos_totales = 200
        nombre_personaje = input("Ingrese el nombre del personaje: ")
        daño_personaje = int(input(f"Ingrese la fuerza del personaje (puntos totales: {puntos_totales}): "))
        puntos_totales -= daño_personaje
        velocidad_personaje = int(input(f"Ingrese la velocidad del personaje(puntos totales: {puntos_totales}): "))
        puntos_totales -= velocidad_personaje
        armadura_personaje = int(input(f"Ingrese la armadura de su personaje(puntos totales: {puntos_totales}): "))
        puntos_totales -= armadura_personaje
        if puntos_totales < 0:
            print("Introdujo mas puntos de los que tiene, repita el proceso")
            crear_personaje(lista_personajes)
        else: # Para este else podria haber hecho otra funcion pero las he tenido que unir porque daba demasiados errores
            print("""\nClases disponibles:\n
                1. Guerrero: Menos velocidad de ataque, ataque medio y mas aguante, puede usar espadas, hachas o mazas
                2. Mago: poco aguante y poca velocidad de ataque, mucho daño, solo puede usar bastones
                3. Acechador: daño y aguante medios, velocidad de ataque muy alta, solo puede usar dagas      
            """)
            seleccion = input("\nSeleccione su clase: ") # Segundo paso para la creacion de personaje
            if seleccion == "1":
                personaje = Guerrero(vida=250, daño_base=100, velocidad_de_ataque=30, armadura=200, nombre=nombre_personaje)
            elif seleccion == "2":
                personaje = Mago(vida=100, daño_base=500, velocidad_de_ataque=10, armadura=20, nombre=nombre_personaje)
            elif seleccion == "3":
                personaje = Acechador(vida=200, daño_base=120, velocidad_de_ataque=100, armadura=80, nombre=nombre_personaje)
            else:
                print("\nIntrodujo algo mal, recuerda que debes seleccionar el indice que acompañe a la opcion que quiera seleccionar")
                crear_personaje(lista_personajes)
        
        lista_personajes.append(personaje) # Este es el final de la funcion, no es necesario un return
        print("\n\nSe creo su personaje correctamente")
    except:
        print("\nSolo puede introducir numeros enteros en las caracteristicas de su personaje\n")
        crear_personaje(lista_personajes)

# ----------------------Mostrar personajes-------------------

def mostrar_personajes(lista_personajes):
    for i, j in enumerate(lista_personajes):
        print(f"{i + 1}. {j}")

# ----------------------funciones de lucha-------------------

def seleccion_de_batalla(lista_personajes, lista_de_monstruos, lista_de_armas): # seleccionamos monstruo personaje y arma para luchar
    print("\n\nMonstruos disponibles: ")
    for i, j in enumerate(lista_de_monstruos): # Los bucles muestran la lista de todos los elementos y lgo seleccionamos su indice
        print(f"{i + 1}. {j}")
    try: # Usamos este try para usar bien los indices con los ints para posteriormente usarlos como int dentro de los indices de las listas
        decision_monstruo = int(input("\nSeleccione un monstruo para combatir: ")) - 1
        monstruo_seleccionado = lista_de_monstruos[decision_monstruo] # Al seleccionar el indice lgo con ese mismo indice podemos escoger el elemento que queramos dentro de la lista
        
        print("\n\nPersonajes disponibles:")
        for k, h in enumerate(lista_personajes):
            print(f"{k + 1}. {h}")
        decision_personaje = int(input(f"\nSeleccione el personaje con el que quiere combatir: ")) - 1
        personaje_seleccionado = lista_personajes[decision_personaje]

        print("\n\nArmas disponibles: ")
        for a, b in enumerate(lista_de_armas):
            print(f"{a + 1}. {b}")
        decision_arma = int(input(f"\nSeleccione el arma con el que quiere combatir: ")) - 1
        arma_seleccionada = lista_de_armas[decision_arma]

        lucha(personaje_seleccionado, monstruo_seleccionado, arma_seleccionada)
    except:
        print("\nIntrodujo algo incorrectamente")
        seleccion_de_batalla(lista_personajes, lista_de_monstruos)

def lucha(personaje, monstruo, arma): # Logica del combate
    print(f"Empezo la lucha, usted combatira con {personaje.nombre} a {monstruo.nombre} con {arma.nombre}")
    return
    

# ----------------------Funcion de juego-------------------

def jugar():
    print("Bienvenido al juego de los monstruos")

    juego = True
    while juego:
        if len(lista_personajes) == 0: # Si no tenemos Ningun personaje el juego nos obligara a crearnos uno para poder seguir jugando
            print("\nAntes de seguir jugando tienes que tener al menos un personaje creado")
            print("\n---1. Crear personaje---")
            crear_personaje(lista_personajes)
        else:
            print("""\n\n
                1. Crear personaje
                2. Mostrar personajes
                3. Luchar!!!!!
                4. Salir        
            """)
            decision = input("\n¿Que quiere hacer ahora (Introduzca el numero que acompaña a la opcion para seleccionarla)?\n\n")

            if decision == "1":
                crear_personaje(lista_personajes)
            elif decision == "2":
                mostrar_personajes(lista_personajes)
            elif decision == "3":
                seleccion_de_batalla(lista_personajes, lista_de_monstruos, lista_de_armas)
            elif decision == "4":
                juego = False
            else:
                print("\nIntrodujo una opcion que no es valida, recuerde que tiene que introducir, 1, 2, 3, o 4 si quiere abandonar")


# Jugar

jugar()