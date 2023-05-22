from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://nelsonlainez91:eo71Nw0dkAnWAVxM@cluster0.bzqjn9m.mongodb.net/?retryWrites=true&w=majority"

# Crear un nuevo cliente y conectar al servidor
client = MongoClient(uri, server_api=ServerApi('1'))

# Enviar un ping para confirmar una conexión exitosa
try:
    client.admin.command('ping')
    print("¡Ping a tu implementación exitoso! Te has conectado correctamente a MongoDB.")
except Exception as e:
    print(e)

db = client["teststore"]
collection = db["products"]

while True:
    print("\n=== Operaciones CRUD ===")
    print("1. Crear un nuevo producto")
    print("2. Leer todos los productos")
    print("3. Actualizar un producto")
    print("4. Eliminar un producto")
    print("5. Salir")

    choice = input("Ingresa tu elección (1-5): ")

    if choice == "1":
        name = input("Ingresa el nombre del producto: ")
        price = float(input("Ingresa el precio del producto: "))
        collection.insert_one({"name": name, "price": price})
        print("¡Producto insertado exitosamente!")

    elif choice == "2":
        results = collection.find()
        print("Todos los productos:")
        for r in results:
            print(r["name"])

    elif choice == "3":
        name = input("Ingresa el nombre del producto a actualizar: ")
        new_price = float(input("Ingresa el nuevo precio: "))
        result = collection.update_one({"name": name}, {"$set": {"price": new_price}})
        if result.modified_count > 0:
            print("¡Producto actualizado exitosamente!")
        else:
            print("No se encontró ningún producto coincidente.")

    elif choice == "4":
        name = input("Ingresa el nombre del producto a eliminar: ")
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print("¡Producto eliminado exitosamente!")
        else:
            print("No se encontró ningún producto coincidente.")

    elif choice == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Por favor, ingresa un número del 1 al 5.")

print("Finalizó la operación seleccionada.")
