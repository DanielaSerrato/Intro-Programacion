"""Proyecto Final del curso: Sistema de Gestión de Usuarios.
"""

usuarios = []


def registrar_usuario(nombre, edad, ciudad):
    usuario = {"nombre": nombre, "edad": edad, "ciudad": ciudad}
    usuarios.append(usuario)
    return usuario


def mostrar_usuarios():
    return usuarios


def buscar_usuario(nombre):
    for u in usuarios:
        if u["nombre"].lower() == nombre.lower():
            return u
    return None


def eliminar_usuario(nombre):
    global usuarios
    usuarios = [u for u in usuarios if u["nombre"].lower() != nombre.lower()]
    return usuarios


def menu():
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
            print(mostrar_usuarios())

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
"""Material de apoyo para Proyecto Final.

Completa este archivo con ejemplos o funciones según el avance del curso.
"""

