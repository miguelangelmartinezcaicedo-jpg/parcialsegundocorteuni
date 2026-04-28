peliculas = [
    ("Los minions", 12000),
    ("Avengers", 14000),
    ("Batman", 11000),
    ("Mario Bros", 12000),
    ("Spiderman: No way home", 20000),
    ("Mario Bros 2", 20000),
    ("Pacman", 11000),
    ("El paseo 8", 19000),
    ("Jorge el curioso", 15000)
]

compras = {}


def comprar():
    try:
        nombre = input("Cual es su nombre: ")
        documento = input("Cual es su documento: ")

        for i in range(len(peliculas)):
            print(i + 1, peliculas[i][0], peliculas[i][1])

        op = int(input("Película: "))
        cant = int(input("Cantidad: "))

        peli = peliculas[op - 1]
        total = peli[1] * cant

        compras[nombre] = (peli[0] ,documento , cant, total)

        print("Total:", total)

    except:
        print("Error")


while True:
    op = input("1.Comprar otras boletas 2.Ver boletas compradas 3.Salir: ")

    if op == "1":
        comprar()

    elif op == "2":
        print(compras)

    elif op == "3":
        break