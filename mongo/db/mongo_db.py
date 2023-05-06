from pymongo import MongoClient
  
# creation of MongoClient
db=MongoClient()
  
# Connect with the portnumber and host
db = MongoClient("mongodb://localhost:27017")
  
# Access database
mydatabase = db['Statera']
  
# Access collection User of the database Statera

# Access collection User of the database Statera
#push json modele for table user


mydatabase.create_collection('user')
mydatabase.create_collection('raw_data')
mydatabase.create_collection('processed_data')
mydatabase.create_collection('MBTI_info')

#mydatabase.drop_collection('DB')
#print(mycollection.find_one())
