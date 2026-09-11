def ordenar():
    chilaquiles = 90
    pozole = 150
    enchiladas = 120
    tacos = 100
    quesadillas = 80

    tiempoC = 10
    tiempoP = 20
    tiempoE = 15
    tiempoT = 12
    tiempoQ = 8

    while True:
        opcion1 = input("¿Quiere pedir los chilaquiles?: ")
        if opcion1.lower() == "si":
            cantidad1 = int(input("¿Cuantos platos quiere?: "))
            break
        elif opcion1.lower() == "no":
            cantidad1 = 0
            tiempoC = 0
            break
        else:
            print("opcion no valida")
    while True: 
        opcion2 = input("¿Quiere pedir el pozole?: ")
        if opcion2.lower() == "si":
            cantidad2 = int(input("¿Cuantos platos quiere?: "))
            break
        elif opcion2.lower() == "no":
            cantidad2 = 0
            tiempoP = 0
            break
        else: 
            print("opcion no valida")
    while True:
        opcion3 = input("¿Quiere pedir las enchiladas?: ")
        if opcion3.lower() == "si":
            cantidad3 = int(input("¿Cuantos platos quiere?: "))
            break
        elif opcion3.lower() == "no":
            cantidad3 = 0
            tiempoE = 0
            break
        else:
            print("opcion no valida")
    while True: 
        opcion4 = input("¿Quiere pedir unos tacos al pastor?: ")
        if opcion4.lower() == "si":
            cantidad4 = int(input("¿Cuantos platos quiere?: "))
            break
        elif opcion4.lower() == "no":
            cantidad4 = 0
            tiempoT = 0
            break
        else: 
            print("opcion no valida")
    while True: 
        opcion5 = input("¿Quiere pedir unas quesadillas?: ")
        if opcion5.lower() == "si":
            cantidad5 = int(input("¿Cuantos platos quiere?: "))
            break
        elif opcion5.lower() == "no":
            cantidad5 = 0
            tiempoQ = 0
            break
        else: 
            print("opcion no valida")
    while True:
        opcion_propina = input("¿Desea agregar propina?: ")
        if opcion_propina.lower() == "si":
            propina = float(input("¿Que porcenjate de propina?: "))
            propina = propina/100
            propina = 1 + propina
            break
        elif opcion_propina.lower() == "no":
            propina = 1
            break
        else: 
            print("opcion no valida")
    total = float(((chilaquiles * cantidad1) + (pozole * cantidad2) + (enchiladas * cantidad3) + (tacos * cantidad4) + (quesadillas * cantidad5)) * propina)
    tiempo = max(tiempoC, tiempoP, tiempoE, tiempoT, tiempoQ)
    print("Su total al pagar serian", f"{total:g}", "mxn")
    print("El tiempo de espera sera de", tiempo, "minutos")
while True:
    print("""
    --------------------
    ¿Que desea hacer?
    --------------------
    - Ver menu
    - Ordenar
    - Salir
    --------------------
    """)
    opcion = input("seleciona una opcion: ")
    if opcion.lower() == "ver menu" or opcion.lower() == "menu":
        print("""
        ------
        Chilaquiles
        Costo: $90
        Totopos cubiertos de salsa roja o verde con pollo, crema y queso
        Tiempo de espera: 10 minutos
        ------
        Pozole
        Costo: $150
        Pozole grande surtido
        Tiempo de espera: 20 minutos
        ------
        Enchiladas
        Costo: $120
        Tortillas rellenas de pollo bañadas en salsa roja, acompañadas de crema y queso
        Tiempo de espera: 15 minutos
        ------
        Tacos al Pastor
        Costo: $100
        Tacos de carne al pastor acompañados de cebolla, cilantro y piña
        Tiempo de espera: 12 minutos
        ------
        Quesadillas
        Costo: $80
        Tortillas de harina rellenas de queso y acompañadas de guacamole y salsa
        Tiempo de espera: 8 minutos

        """)
        while True:
            opcionz = input("¿Desea ordenar?: ")
            if opcionz.lower() == "si":
                ordenar()
                break
                
            elif opcionz.lower() == "no":
                opcionh = input("¿Desea salir al menu?: ")
                if opcionh.lower() == "si":
                    break
                elif opcionh.lower() == "no":
                    print("regresando al menu...")
                    print("""
        ------
        Chilaquiles
        Costo: $90
        Totopos cubiertos de salsa roja o verde con pollo, crema y queso
        Tiempo de espera: 10 minutos
        ------
        Pozole
        Costo: $150
        Pozole grande surtido
        Tiempo de espera: 20 minutos
        ------
        Enchiladas
        Costo: $120
        Tortillas rellenas de pollo bañadas en salsa roja, acompañadas de crema y queso
        Tiempo de espera: 15 minutos
        ------
        Tacos al Pastor
        Costo: $100
        Tacos de carne al pastor acompañados de cebolla, cilantro y piña
        Tiempo de espera: 12 minutos
        ------
        Quesadillas
        Costo: $80
        Tortillas de harina rellenas de queso y acompañadas de guacamole y salsa
        Tiempo de espera: 8 minutos  

        """)
            else:
                print("opcion no valida")

    elif  opcion.lower() == "ordenar":
        ordenar()
        exit()

    elif opcion.lower() == "salir":
        print("Saliendo del programa...")
        break

    else:
        print ("opcion no valida")