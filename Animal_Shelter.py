import os  # Import the OS module to interact with the operating system
import random  # Import the random module for generating random numbers
from pymongo import MongoClient  # Import MongoClient to handle MongoDB connections
from bson.objectid import ObjectId  # Import ObjectId to create unique IDs for MongoDB documents
import urllib.parse  # Import urllib.parse for parsing user credentials

class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, user, password, host, port, database, collection):
        # Fetching environment variables or using provided parameters for MongoDB connection
        USER = urllib.parse.quote_plus(user) if user else os.getenv('MONGO_USER', 'aacuser')  # Encode username
        PASS = urllib.parse.quote_plus(password) if password else os.getenv('MONGO_PASS', 'SNHU1234')  # Encode password
        HOST = os.getenv('MONGO_HOST', 'nv-desktop-services.apporto.com')  # Set MongoDB host
        PORT = int(os.getenv('MONGO_PORT', 33321))  # Set MongoDB port number

        # Initialize connection to MongoDB server
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}/AAC')  # Create a MongoDB client
        self.database = self.client['AAC']  # Select the 'AAC' database
        self.collection = self.database['animals']  # Select the 'animals' collection within the database

    def create(self, data):
        """Insert a new document into the animals collection."""
        if data is not None:  # Check if data is provided
            insert_success = self.collection.insert_one(data)  # Use the collection's insert_one method to add a new document
            return True if insert_success.acknowledged else False  # Return True if the insert was acknowledged by MongoDB
        else:
            raise Exception("Nothing to save, because data parameter is empty")  # Raise an exception if no data is provided

    def read(self, search_data):
        """Retrieve documents based on search criteria."""
        if search_data:  # Check if search data is provided
            data = self.collection.find(search_data, {"_id": False})  # Use the collection's find method to query documents
        else:
            data = self.collection.find({}, {"_id": False})  # Query all documents if no search data is provided
        return list(data)  # Convert the cursor returned by find to a list for easier handling

    def update(self, search_data, update_data):
        """Update documents based on search criteria."""
        if search_data is not None:  # Check if search data is provided
            result = self.collection.update_many(search_data, {"$set": update_data})  # Update matching documents with new data
            return result.raw_result  # Return the raw result of the update operation
        else:
            return "{}"  # Return an empty result if no search data is provided

    def delete(self, delete_data):
        """Delete documents based on criteria."""
        if delete_data is not None:  # Check if delete criteria is provided
            result = self.collection.delete_many(delete_data)  # Use the collection's delete_many method to remove documents
            return result.raw_result  # Return the raw result of the delete operation
        else:
            return "{}"  # Return an empty result if no delete criteria is provided

    def get_random_animal(self):
        """Retrieve a random animal from the collection."""
        random_animal = self.collection.aggregate([{"$sample": {"size": 1}}])  # Use the aggregate method to get a random animal
        return list(random_animal)  # Convert cursor to list to return the randomly selected animal
