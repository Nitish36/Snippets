import pymongo
import pprint
from bson.objectid import ObjectId
client = pymongo.MongoClient("mongodb://localhost:27017/")

dbs = client.list_database_names()
print(dbs)

weather_db = client.weather    # create a collection
collections = weather_db.list_collection_names()
print(collections)


def insert_weather_data():
    collection = weather_db.weather
    weather_data = {
        "city": "Bangalore",
        "temperature": 30
    }
    inserted_id = collection.insert_one(weather_data).inserted_id
    print(inserted_id)


insert_weather_data()

production = client.production
person_collection = production.person_collection


def create_documents():
    first_names = ["Tim", "Jane", "Brad"]
    last_names = ["Tom", "Doe", "Pit"]
    ages = [21, 30, 33]
    docs = []

    for first_name, last_name, age in zip(first_names, last_names, ages):
        doc = {"first_name": first_name, "last_name": last_name, "age": age}
        docs.append(doc)

    person_collection.insert_many(docs)


printer = pprint.PrettyPrinter()


def find_all_people():
    people = person_collection.find()
    for person in people:
        printer.pprint(person)


def count_all_people():
    count = person_collection.count_documents(filter={})
    print("The number of people are ", count)


find_all_people()
count_all_people()


def get_person_by_id(person_id):
    _id = ObjectId(person_id)
    person = person_collection.find_one({"_id": _id})
    printer.pprint(person)


def get_age_range(min_age, max_age):
    query = {"$and": [
            {"age": {"$gte": min_age}},
            {"age": {"$lte": max_age}}
        ]}

    people = person_collection.find(query).sort("age")
    for person in people:
        printer.pprint(person)


get_age_range(20, 35)


def update_person_by_id(person_id):
    _id = ObjectId(person_id)
    all_updates = {
        "$set": {"new_field": True},
        "$inc": {"age": 1},
        "$rename": {"first_name": "first", "last_name": "last"}
    }
    person_collection.update_one({"_id": _id}, all_updates)

    # How to remove certain values
    person_collection.update_one({"_id": _id}, {"$unset": {"new_field": ""}})


update_person_by_id("666e681b0ba6ae63c8512b88")
print("After Updation")
find_all_people()


def replace_one(person_id):
    _id = ObjectId(person_id)
    new_doc = {
        "first_name": "new first name",
        "last_name": "new last name",
        "age": 100
    }
    person_collection.replace_one({"_id": _id}, new_doc)


replace_one("666e681b0ba6ae63c8512b88")


def delete_doc_by_id(person_id):
    _id = ObjectId(person_id)
    person_collection.delete_one({"_id": _id})


delete_doc_by_id("666e681b0ba6ae63c8512b87")
