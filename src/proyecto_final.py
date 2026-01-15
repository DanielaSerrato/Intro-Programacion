"""Proyecto Final del curso: Sistema de Gestión de Usuarios.

Este módulo contiene funciones básicas para registrar, listar, buscar y eliminar usuarios.
"""

usuarios = []


def registrar_usuario(nombre, edad, ciudad):
    """Registra un usuario en la lista global y devuelve el diccionario creado."""
    usuario = {"nombre": nombre, "edad": edad, "ciudad": ciudad}
    usuarios.append(usuario)
    return usuario


def listar_usuarios():
    """Devuelve una lista con los nombres de todos los usuarios."""
    nombres = []
    for usuario in usuarios:
        nombres.append(usuario["nombre"])
    return nombres


def buscar_usuario(nombre):
    """Busca un usuario por nombre (sin distinguir mayúsculas)."""
    for usuario in usuarios:
        if usuario["nombre"].lower() == nombre.lower():
            return usuario
    return None


def eliminar_usuario(nombre):
    """Elimina un usuario por nombre y devuelve True si se eliminó."""
    indice = 0
    while indice < len(usuarios):
        if usuarios[indice]["nombre"].lower() == nombre.lower():
            usuarios.pop(indice)
            return True
        indice += 1
    return False


def menu():
    """Menú opcional en consola para interactuar con el sistema."""
    while True:
        print("\n— Menú —")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Buscar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            ciudad = input("Ciudad: ")
            registrar_usuario(nombre, edad, ciudad)

        elif opcion == "2":
            print(listar_usuarios())

        elif opcion == "3":
            nombre = input("Nombre: ")
            print(buscar_usuario(nombre))

        elif opcion == "4":
            nombre = input("Nombre: ")
            eliminar_usuario(nombre)

        elif opcion == "5":
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    menu()
