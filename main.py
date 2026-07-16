import validaciones.py as vld
def main():
    coleccion = vld.diccionarios(productos,stock)
    while True:
        vld.menu()
        opcion = vld.leer_opcion()
        if opcion == 1:
            vld.unidades_categoria(coleccion)
        elif opcion == 2:
            vld.busqueda_precio(coleccion)
        elif opcion == 3:
            vld.actualizar_precio(coleccion)
        elif opcion == 4:
            codigo = input("Ingresa código del producto: ")
            if not vld.validar_nombre(codigo):
                print("Ingresa un código sin espacios en blanco ni vacío")
                return
            nombre = input("Ingresa un nombre del código: ")
            if not vld.validar_nombre(nombre):
                print("Ingresa un nombre sin espacios en blanco ni vacío")
                return
            categoria = input("Ingresa una categoría del producto: ")
            if not vld.validar_nombre(categoria):
                print("Ingresa una categoría sin espacios en blanco ni vacío")
                return
            marca = input("Ingresa una marca del producto: ")
            if not vld.validar_nombre(marca):
                print("Ingresa una marca sin espacios en blanco ni vacío")
                return
            peso_kg = input("Ingresa un peso del producto: ")
            if not vld.validar_pesokg(peso):
                print("Ingresa un peso mayor que cero")
                return
            es_importado = input("Ingresa si el producto es importado (s/n): ")
            if not vld.validar_importado(importado):
                print("Ingresa un importe correcto")
                return
            es_para_cachorro = input("¿Es para cachorro? (s/n): ")
            if not vld.validar_importado(cachorro):
                print("Ingresa cachorro correcto")
            precio = input("Ingresa el precio: ")
            if not vld.validar_precio(precio):
                print("Ingresa un precio mayor que cero")
                return
            unidades = input("Ingresa las unidades: ")
            if not vld.validar_unidades(unidades):
                print("Ingresa unidades igual o mayor que cero")
                return
            vld.agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades)
        elif opcion == 5:
            vld.eliminar_producto(coleccion)
        elif opcion == 6:
            print("Programa finalizado.")
            break
if __name__ == "__main__":
    main()