from pymongo import MongoClient

# reemplace <username>, <password> y <clustername> con sus propias credenciales
username = "nelsonlainez91"
password = "eo71Nw0dkAnWAVxM"
clustername = "Cluster0"

# establecer la conexión
client = MongoClient(f"mongodb+srv://{username}:{password}@{clustername}.mongodb.net/test?retryWrites=true&w=majority")

# acceder a una base de datos
db = client.test
