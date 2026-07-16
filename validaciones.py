def diccionarios(productos,stock):
    productos = {
        'M001': ['Alimento Premium','comida', 'DogPlus', 10, True,False],
        'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False,False],
        'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
        'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False,True],
        'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True,False],
        'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False,False]
    }
    stock = {
        'M001': [32990, 12],
        'M002': [9990, 0],
        'M003': [5490, 25],
        'M004': [7990, 5],
        'M005': [11990, 7],
        'M006': [24990, 3]
    }

def menu():
    print("=============== MENÚ PRINCIPAL ===============")
    print("1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("==============================================")

def leer_opcion():
    try:
        opcion = int(input("Ingrese opción (1-6): "))
    except ValueError:
        print("Debe seleccionar una opción válida")
        return -1

def buscar_categoria(productos,buscar):
    cantidad_productos = 0
    for i in range(len(productos)):
        if productos[i]['comida','higiene','snack','accesorio'].lower().strip() == buscar.lower().strip():
            cantidad_productos += 1

        else:
            print("No hay productos asociados a esa categoría")

def unidades_categoria(categoria):
    categoria = input("Ingrese categoría a buscar: ")

def busqueda_precio(p_min,p_max):

def validar_nombre(nombre):
    print("Ingresa un nombre sin espacios en blanco")
    try:
        if len(codigo.strip()) > 0:
            return True
        else:
            return False
    except ValueError:
        print("Ingresa un nombre válido")

def validar_pesokg(pesokg):
    try:
        pesokg = float(pesokg)
        if pesokg >= 0:
            return True
        else:
            return False
    except ValueError:
        print("Ingresa un peso válido")
        return False

def validar_importado(respuesta):
    respuesta = respuesta.lower().strip()
    es_importado = "s"
    es_importado2 = "n"
    si_es_importado = False
    if es_importado == respuesta:
        si_es_importado = True
    elif es_importado2 == respuesta:
        si_es_importado = False
    else:
        print("Ingresa una respuesta válida (s/n)")

def validar_precio(precio):
    try:
        if precio >= 1:
            return True
        else:
            return False
    except ValueError:
        print("Ingresa un precio válido")
        return False

def validar_unidades(unidades):
    try:
        if unidades >= 0:
            return True
        else:
            return False
    except ValueError:
        print("Ingresa unidades válidas")
        return False

def agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades):
    producto_agregado = {
        codigo : [nombre,categoria,marca,peso_kg,es_importado,es_para_cachorro]
    }
    producto_agregado2 = {
        codigo : [precio,unidades]
    }
    diccionarios(productos.append(producto_agregado))
    diccionarios(stock.append(producto_agregado2))
    print(f"El producto {nombre} a sido registrado satisfactoriamente")
def buscar_codigo(codigo):
    for i in range(len(diccionarios(stock))):
        if diccionarios(stock)[i]['M001','M002','M003','M004','M005','M006'].lower().strip() == codigo.lower().strip()
        return True
    return False

def actualizar_precio(codigo,nuevo_precio):
    if buscar_codigo(codigo) = True:
        nuevo_precio = input("Ingresa el nuevo precio: ")
    else:
        return False