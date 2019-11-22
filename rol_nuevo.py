import random
from random import randint


class Personaje:
    def __init__(self):
        self.nombre = ""
        self.salud = 1
        self.salud_max = 1

    def hacer_danio(self, Enemigo):
        danio = min(max(randint(0, self.salud) - randint(0, Enemigo.salud), 0), Enemigo.salud)
        Enemigo.salud = Enemigo.salud - danio
        if danio == 0:
            print(f"{Enemigo.nombre} evade el ataque de {self.nombre}")
        else:
            print(f"{self.nombre} acierta un golpe {Enemigo.nombre}!")
        return Enemigo.salud <= 0


class Enemigo(Personaje):
    def __init__(self, Jugador):
        Personaje.__init__(self)
        bicho = ["Orco", "Araña gigante", "Oso"]
        self.nombre = random.choice(bicho)
        self.salud = randint(1, Jugador.salud)


class Jugador(Personaje):
    def __init__(self):
        Personaje.__init__(self)
        self.estado = 'normal'
        self.salud = 10
        self.salud_max = 10

    def salir(self):
        print(f"{self.nombre} no puede encontrar el camino de vuelta a casa y muere de inanicion.\nR.I.P.")
        self.salud = 0

    def ayuda(self):
        print(Commands.keys())

    def estado(self):
        print(f"{self.nombre} - salud: {self.salud}/{self.salud_max}")

    def cansancio(self):
        print(f"{self.nombre} siente cansancio.")
        self.salud = max(1, self.salud - 1)

    def descanso(self):
        if self.estado != 'normal':
            print(f"{self.nombre} no puede descansar ahora!")
        else:
            print(f"{self.nombre} descansa.")
            if randint(0, 1):
                self.Enemigo = Enemigo(self)
                print(f"{self.nombre} se desperto de golpe por {self.Enemigo.nombre}!")
                self.estado = 'lucha'
                self.Enemigo_ataques()
            else:
                if self.salud < self.salud_max:
                    self.salud = self.salud + 1
                else:
                    self.salud = self.salud - 1
                    print(f"{self.nombre} a dormido demasiado. {self.salud}")

    def explorar(self):
        if self.estado != 'normal':
            print(f"{self.nombre} esta demasiado ocupado en este momento!")
            self.Enemigo_ataques()
        else:
            print(f"{self.nombre} explora un pasaje sinuoso.")
            if randint(0, 1):
                self.Enemigo = Enemigo(self)
                print(f"{self.nombre} encuentra {self.Enemigo.nombre}!")
                self.estado = 'lucha'
            else:
                if randint(0, 1):
                    self.cansancio()

    def huir(self):
        if self.estado != 'lucha':
            print(f"{self.nombre} corre en circulos durante un tiempo.")
            self.cansancio()
        else:
            if randint(1, self.salud + 5) > randint(1, self.Enemigo.salud):
                print(f"{self.nombre} huye de {self.Enemigo.nombre}.")
                self.Enemigo = None
                self.estado = 'normal'
            else:
                print(f"{self.nombre} no puede escapar de {self.Enemigo.nombre}!")
                self.Enemigo_ataques()

    def atacar(self):
        if self.estado != 'lucha':
            print(f"{self.nombre} golpea con fuerza pero sin resultados.")
            self.cansancio()
        else:
            if self.hacer_danio(self.Enemigo):
                print(f"{self.nombre} aniquila {self.Enemigo.nombre}!")
                self.Enemigo = None
                self.estado = 'normal'
                if randint(0, self.salud) < 10:
                    self.salud = self.salud + 1
                    self.salud_max = self.salud_max + 1
                    print(f"{self.nombre} se siente mas fuerte!")
            else:
                self.Enemigo_ataques()

    def Enemigo_ataques(self):
        if self.Enemigo.hacer_danio(self):
            print(f"{self.nombre} fue sacrificado por {self.Enemigo.nombre}!!!\nR.I.P.")

Commands = {
    'salir': Jugador.salir,
    'ayuda': Jugador.ayuda,
    'estado': Jugador.estado,
    'descanso': Jugador.descanso,
    'explorar': Jugador.explorar,
    'huir': Jugador.huir,
    'atacar': Jugador.atacar,
    }

p = Jugador()
p.nombre = input("Cual es el nombre del personaje? ")
print("(Escribe ayuda para obtener una lista de acciones)\n")
print(f"{p.nombre} entra en una cueva oscura en busca de aventura.")

while(p.salud > 0):
    line = input("> ")
    args = line.split()
    if len(args) > 0:
        commandFound = False
        for c in Commands.keys():
            if args[0] == c[:len(args[0])]:
                Commands[c](p)
                commandFound = True
                break
        if not commandFound:
            print(f"{p.nombre} no se entiende la accion.")
