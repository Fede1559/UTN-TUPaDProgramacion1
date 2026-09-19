
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
bloqueado = False
racha_forzar = 0 


agente = input("Nombre del agente: ")
while not agente.isalpha():
    agente = input("Error: solo letras. Nombre del agente: ")

print(f"\nBienvenido, agente {agente}. La misión comienza.")


while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado:

    print(f"\n--- Estado ---")
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas}/3 | Alarma: {alarma}")
    print("1) Forzar cerradura  2) Hackear panel  3) Descansar")

    opcion = input("Elegí una opción: ")
    while not opcion.isdigit() or not (1 <= int(opcion) <= 3):
        print("Error: opción inválida.")
        opcion = input("Elegí una opción: ")
    opcion = int(opcion)


    if opcion == 1:
        racha_forzar += 1
        energia -= 20
        tiempo -= 2

        if racha_forzar == 3:
            print("¡La cerradura se trabó! Se activa la alarma.")
            alarma = True
        else:
            if energia < 40:
                print("Riesgo de alarma. Elegí un número:")
                numero = input("1-3: ")
                while not numero.isdigit() or not (1 <= int(numero) <= 3):
                    print("Error: debe ser un número entre 1 y 3.")
                    numero = input("1-3: ")
                numero = int(numero)
                if numero == 3:
                    print("¡Activaste la alarma!")
                    alarma = True

            if not alarma:
                cerraduras_abiertas += 1
                print("Cerradura forzada con éxito.")

    elif opcion == 2:
        racha_forzar = 0
        energia -= 10
        tiempo -= 3

        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"Paso {paso}/4 - código parcial: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Código completo! Se abrió una cerradura automáticamente.")


    elif opcion == 3:
        racha_forzar = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        if alarma:
            energia -= 10
            print("La alarma sigue activa: pierdes energía extra al descansar.")
        print("Descansaste.")

    if alarma and tiempo <= 3 and cerraduras_abiertas != 3:
        bloqueado = True


print("\n=== FIN DEL JUEGO ===")
if cerraduras_abiertas == 3:
    print("🏆 VICTORIA: abriste las 3 cerraduras.")
elif bloqueado:
    print(" DERROTA: el sistema se bloqueó por la alarma.")
elif energia <= 0:
    print(" DERROTA: te quedaste sin energía.")
elif tiempo <= 0:
    print(" DERROTA: se acabó el tiempo.")