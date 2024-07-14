import pymongo
from bson.objectid import ObjectId
import pprint

printer = pprint.PrettyPrinter()
client = pymongo.MongoClient("mongodb://localhost:27017/")

dbs = client.list_database_names()
# print(dbs)
weather_db = client.weather
collections = weather_db.list_collection_names()
# print(collections)


def insert_document():
    time = input("Enter the time")
    city = input("Enter the city name")
    temperature = int(input("Enter the temperature"))
    air_quality = int(input("Enter the air quality"))
    humidity = int(input("Enter the humidity"))
    pressure = int(input("Enter the pressure"))

    collection = weather_db.weather

    weather_data = {
        "Time": time,
        "City": city,
        "TemperatureC": temperature,
        "Air_Quality": air_quality,
        "Humidity": humidity,
        "Pressure": pressure
    }
    weather_insert = collection.insert_one(weather_data).inserted_id
    print("Recorded inserted")
    print(weather_insert)


def display_documents():
    collection = weather_db.weather
    data = collection.find()
    for dat in data:
        printer.pprint(dat)


def count_records():
    collection = weather_db.weather
    count = collection.count_documents(filter={})
    print("Total Records: ", count)


def delete_record():
    collection = weather_db.weather
    id = input("Enter the id to be deleted")
    _id = ObjectId(id)
    collection.delete_one(
        {'_id': _id}
    )


def update_record():
    collection = weather_db.weather
    id = input("Enter the id")
    _id = ObjectId(id)
    print("Updating information")
    time = input("Enter new time")
    city = input("Enter new city name")
    temperature = int(input("Enter new temperature"))
    air_quality = int(input("Enter new air quality"))
    humidity = int(input("Enter new humidity"))
    pressure = int(input("Enter new pressure"))

    all_updates = {
        "$set": {
            "Time": time,
            "City": city,
            "TemperatureC": temperature,
            "Air_Quality": air_quality,
            "Humidity": humidity,
            "Pressure": pressure
        }
    }
    collection.update_one({"_id": _id}, all_updates, upsert=True)


print("CRUD Operations demo in Mongodb")
while (True):
    print("Select one of the following options")
    print("1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Update")
    print("Select ur choice")
    ch = int(input())
    if ch == 1:
        insert_document()

    elif ch == 2:
        delete_record()

    elif ch == 3:
        display_documents()
        count_records()

    elif ch == 4:
        update_record()

    else:
        exit(0)
