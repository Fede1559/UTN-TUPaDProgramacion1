
operador = input("Nombre del operador: ")
while not operador.isalpha():
    operador = input("Inválido, solo letras. Nombre del operador: ")

lunes1 = lunes2 = lunes3 = lunes4 = ""
martes1 = martes2 = martes3 = ""


while True:
    print("\n1) Reservar turno  2) Cancelar turno  3) Ver agenda del día  4) Resumen general  5) Cerrar sistema")
    opcion = input("Opción: ")
    while not opcion.isdigit() or not (1 <= int(opcion) <= 5):
        print("Error: opción inválida.")
        opcion = input("Opción: ")
    opcion = int(opcion)

    if opcion == 1:
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or not (1 <= int(dia) <= 2):
            print("Error: día inválido.")
            dia = input("Elegir día (1=Lunes, 2=Martes): ")
        dia = int(dia)

        paciente = input("Nombre del paciente: ")
        while not paciente.isalpha():
            paciente = input("Inválido, solo letras. Nombre del paciente: ")

        if dia == 1:
            repetido = (paciente == lunes1 or paciente == lunes2 or
                        paciente == lunes3 or paciente == lunes4)
            if repetido:
                print("Error: el paciente ya tiene turno el lunes.")
            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado: lunes1")
            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado: lunes2")
            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado: lunes3")
            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado: lunes4")
            else:
                print("No hay turnos disponibles el lunes.")
        else:
            repetido = (paciente == martes1 or paciente == martes2 or paciente == martes3)
            if repetido:
                print("Error: el paciente ya tiene turno el martes.")
            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado: martes1")
            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado: martes2")
            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado: martes3")
            else:
                print("No hay turnos disponibles el martes.")

    elif opcion == 2:
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or not (1 <= int(dia) <= 2):
            print("Error: día inválido.")
            dia = input("Elegir día (1=Lunes, 2=Martes): ")
        dia = int(dia)

        paciente = input("Nombre del paciente a cancelar: ")
        while not paciente.isalpha():
            paciente = input("Inválido, solo letras. Nombre del paciente: ")

        if dia == 1:
            if lunes1 == paciente:
                lunes1 = ""
                print("Turno cancelado.")
            elif lunes2 == paciente:
                lunes2 = ""
                print("Turno cancelado.")
            elif lunes3 == paciente:
                lunes3 = ""
                print("Turno cancelado.")
            elif lunes4 == paciente:
                lunes4 = ""
                print("Turno cancelado.")
            else:
                print("Error: el paciente no tiene turno el lunes.")
        else:
            if martes1 == paciente:
                martes1 = ""
                print("Turno cancelado.")
            elif martes2 == paciente:
                martes2 = ""
                print("Turno cancelado.")
            elif martes3 == paciente:
                martes3 = ""
                print("Turno cancelado.")
            else:
                print("Error: el paciente no tiene turno el martes.")

    elif opcion == 3:
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or not (1 <= int(dia) <= 2):
            print("Error: día inválido.")
            dia = input("Elegir día (1=Lunes, 2=Martes): ")
        dia = int(dia)

        if dia == 1:
            print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
            print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
            print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
            print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")
        else:
            print("Turno 1:", martes1 if martes1 != "" else "(libre)")
            print("Turno 2:", martes2 if martes2 != "" else "(libre)")
            print("Turno 3:", martes3 if martes3 != "" else "(libre)")

    elif opcion == 4:
        ocupados_lunes = 0
        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1
        disponibles_lunes = 4 - ocupados_lunes

        ocupados_martes = 0
        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1
        disponibles_martes = 3 - ocupados_martes

        print(f"Lunes -> ocupados: {ocupados_lunes}, disponibles: {disponibles_lunes}")
        print(f"Martes -> ocupados: {ocupados_martes}, disponibles: {disponibles_martes}")

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos ocupados: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos ocupados: Martes")
        else:
            print("Empate entre Lunes y Martes")

    elif opcion == 5:
        print("Cerrando sistema...")
        break