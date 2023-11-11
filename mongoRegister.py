from faker import Faker
import pymongo
import pyodbc

# Conexión a MongoDB
mongo_client = pymongo.MongoClient("mongodb://localhost:27017")
mongo_db = mongo_client["local"]
mongo_collection = mongo_db["ivan"]


# Generar datos ficticios utilizando Faker
fake = Faker()
data = []

for _ in range(100):
    document = {
        "name": fake.name(),
        "address": fake.address(),
        "email": fake.email(),
        "phone": fake.phone_number()
    }
    data.append(document)

# Insertar datos en MongoDB
mongo_collection.insert_many(data)



# Cerrar conexiones
mongo_client.close()

