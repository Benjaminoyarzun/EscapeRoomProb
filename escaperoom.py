import random


def pedir_respuesta_numerica(mensaje):
    while True:
        try:
            return float(input(mensaje).replace(",", "."))
        except ValueError:
            print("Ingrese un valor numérico válido.")


def nivel1():
    print("\n" + "=" * 50)
    print("NIVEL 1 - ESPACIO MUESTRAL")
    print("=" * 50)

    print("Se lanza un dado y una moneda.")
    print("El dado tiene 6 resultados posibles y la moneda 2.")

    respuesta_correcta = 6 * 2

    while True:
        respuesta = pedir_respuesta_numerica(
            "¿Cuántos resultados posibles existen?: "
        )

        if respuesta == respuesta_correcta:
            print("\n✓ Correcto.")
            print("6 resultados del dado × 2 resultados de la moneda = 12.")
            print("Nivel 2 desbloqueado.")
            return

        print("✗ Respuesta incorrecta. Intente nuevamente.")


def nivel2():
    print("\n" + "=" * 50)
    print("NIVEL 2 - PROBABILIDAD CLÁSICA")
    print("=" * 50)

    print("Una bolsa contiene:")
    print("- 5 bolas rojas")
    print("- 3 bolas azules")
    print("- 2 bolas verdes")
    print()
    print("Se extrae una bola al azar.")

    favorables = 2
    posibles = 10
    probabilidad = favorables / posibles

    while True:
        respuesta = pedir_respuesta_numerica(
            "¿Cuál es la probabilidad de obtener una bola verde (%)?: "
        )

        if abs(respuesta - probabilidad * 100) < 0.001:
            print("\n✓ Correcto.")
            print(
                f"Hay {favorables} resultados favorables "
                f"de {posibles} resultados posibles."
            )
            print(f"Probabilidad = {favorables}/{posibles} = 20%.")
            print("Nivel 3 desbloqueado.")
            return

        print("✗ Respuesta incorrecta. Intente nuevamente.")


def nivel3():
    print("\n" + "=" * 50)
    print("NIVEL 3 - PROBABILIDAD FRECUENCIAL")
    print("=" * 50)

    while True:
        resultados = [
    random.choice(["cara", "cruz"])for _ in range(100)]

        caras = resultados.count("cara")
        cruces = resultados.count("cruz")
        print("\nSe realizó una simulación de 100 lanzamientos de una moneda.")
        print(f"Caras: {caras}")
        print(f"Cruces: {cruces}")

        respuesta = pedir_respuesta_numerica(
            "¿Cuál fue la frecuencia relativa de caras (%)?: "
        )

        frecuencia_relativa = caras / 100 * 100

        if abs(respuesta - frecuencia_relativa) < 0.001:
            print("\n✓ Correcto.")
            print(
                f"La frecuencia relativa se obtiene dividiendo "
                f"los {caras} casos de cara por los 100 lanzamientos."
            )
            print(f"Frecuencia relativa = {caras}/100 = {frecuencia_relativa}%.")
            print("Nivel 4 desbloqueado.")
            return

        print("✗ Respuesta incorrecta.")

        opcion = input(
            "Presione ENTER para intentar nuevamente "
            "o escriba S para generar otra simulación: "
        ).strip().lower()

        if opcion == "s":
            print("Generando una nueva simulación...")


def nivel4():
    print("\n" + "=" * 50)
    print("NIVEL 4 - PROBABILIDAD CONDICIONAL")
    print("=" * 50)

    print("Se registraron 30 estudiantes según su grupo y si aprobaron:")

    print()
    print("                 Aprobó    No aprobó")
    print("Grupo A             12          3")
    print("Grupo B              8          7")
    print()

    print(
        "Si sabemos que el estudiante pertenece al Grupo A,"
    )
    print(
        "¿cuál es la probabilidad de que haya aprobado?"
    )

    while True:
        respuesta = pedir_respuesta_numerica(
            "Ingrese la respuesta (%): "
        )

        probabilidad = 12 / 15 * 100

        if abs(respuesta - probabilidad) < 0.001:
            print("\n✓ Correcto.")
            print(
                "Como sabemos que pertenece al Grupo A, "
                "solo consideramos los 15 estudiantes de ese grupo."
            )
            print("P(Aprobó | Grupo A) = 12/15 = 80%.")
            print("Nivel 5 desbloqueado.")
            return

        print("✗ Respuesta incorrecta. Intente nuevamente.")


def nivel5():
    print("\n" + "=" * 50)
    print("NIVEL 5 - INDEPENDENCIA")
    print("=" * 50)

    print("Se lanzan un dado y una moneda.")
    print()
    print("Evento A: obtener un número par en el dado.")
    print("Evento B: obtener cara en la moneda.")
    print()

    print("¿Los eventos A y B son independientes?")
    print("1. Independientes")
    print("2. Dependientes")

    while True:
        respuesta = input("Seleccione una opción: ").strip()

        if respuesta == "1":
            print("\n✓ Correcto.")
            print()
            print("P(A) = 3/6 = 1/2")
            print("P(B) = 1/2")
            print("P(A ∩ B) = 3/12 = 1/4")
            print("P(A) × P(B) = 1/2 × 1/2 = 1/4")
            print()
            print(
                "Como P(A ∩ B) = P(A) × P(B), "
                "los eventos son independientes."
            )
            print("\n¡Felicitaciones! Completaste el escape room.")
            return

        if respuesta == "2":
            print("✗ Incorrecto. Los eventos son independientes.")
        else:
            print("Seleccione 1 o 2.")


def main():
    print("=" * 50)
    print("       ESCAPE ROOM DE PROBABILIDAD")
    print("=" * 50)
    print()
    print(
        "Superá los 5 niveles para completar el desafío."
    )
    print(
        "Cada nivel debe ser resuelto correctamente "
        "para poder avanzar."
    )

    input("\nPresione ENTER para comenzar...")

    nivel1()
    nivel2()
    nivel3()
    nivel4()
    nivel5()


if __name__ == "__main__":
    main()