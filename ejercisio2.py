usuario_correcto = "alumno"
clavecorrecta = "python123"
acceso = False

for intento in range(1, 4):
    usuario = input(f"intento {intento}/3 - usuario:")
    clave = input("clave:")
    if usuario == usuario_correcto and clave == clavecorrecta:
        print("acceso concedido.")
        acceso = True
        break
    else:
        print(" error: credencial invalida")

if not acceso:
    print("cuenta bloqueada")

if acceso:
    while True:
        print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("opcion:")
        while not opcion.isdigit() or not (1 <= int(opcion) <= 4):
            if not opcion.isdigit():
                print(" error: ingrese un numero valido")
            else:
                print(" error: opcion afuera de rango.")
            opcion = input("opcion:")

        opcion = int(opcion)

        if opcion == 1:
            print("inscripto")

        elif opcion == 2:
            clave_nueva = input("ingrese la nueva clave:")
            clave_confir = input("confirme la nueva clave:")

            while clave_nueva != clave_confir or len(clave_nueva) < 6:
                if clave_nueva != clave_confir:
                    print(" error: las claves no coinciden.")
                else:
                    print(" error: la clave debe tener minimo 6 caracteres.")
                clave_nueva = input("ingrese la nueva clave:")
                clave_confir = input("confirme la nueva clave:")

            clavecorrecta = clave_nueva
            print("clave actualizada con exito.")

        elif opcion == 3:
            print("¡vas muy bien, segui asi con Python!")

        elif opcion == 4:
            print("saliendo del sistema...")
            break