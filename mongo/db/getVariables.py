from pymongo import MongoClient
# creation of MongoClient
db=MongoClient()
# Connect with the portnumber and host
db = MongoClient("mongodb://localhost:27017")
# Access database
mydatabase = db['Statera']






User = mydatabase['user']
RawData = mydatabase['raw_data']
ProcessedData = mydatabase['processed_data']