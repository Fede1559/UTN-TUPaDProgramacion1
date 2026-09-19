
nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    nombre = input("Error: Solo se permiten letras. Nombre del Gladiador: ")


vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
danio_enemigo = 12
turno_gladiador = True

print(f"\n¡Que comience la batalla, {nombre}!")


while vida_jugador > 0 and vida_enemigo > 0:


    print(f"\n--- Estado ---")
    print(f"Tu vida: {vida_jugador} | Vida del enemigo: {vida_enemigo} | Pociones: {pociones}")
    print("1) Ataque Pesado  2) Ráfaga Veloz  3) Curar")

    opcion = input("Elegí una opción: ")
    while not opcion.isdigit() or not (1 <= int(opcion) <= 3):
        print("Error: opción inválida.")
        opcion = input("Elegí una opción: ")
    opcion = int(opcion)


    if opcion == 1:
        if vida_enemigo < 20:
            danio_final = ataque_pesado * 1.5
            print("¡Golpe Crítico!")
        else:
            danio_final = float(ataque_pesado)
        vida_enemigo -= danio_final
        print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")

    elif opcion == 2:
        for golpe in range(3):
            vida_enemigo -= 5
            print(" > Golpe conectado por 5 de daño")

   
    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print("Usaste una poción. Recuperaste 30 puntos de vida.")
        else:
            print("¡No quedan pociones! Pierdes el turno.")

    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f"¡El enemigo te atacó por {danio_enemigo} puntos de daño!")


print("\n=== FIN DE LA BATALLA ===")
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")