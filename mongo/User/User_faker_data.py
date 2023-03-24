

import random
from pymongo import MongoClient
from bson.objectid import ObjectId
import string
import pandas as pd

        #importation du ficher csv des adresses
df =  pd.read_csv('data/adresse.csv',on_bad_lines='skip', sep=";")
#df.dropna(inplace=True)



        #récupération au hasar d'une adresse
def random_adress():
    data = df.iloc[random.randint(3, len(df))]
    string ="".join([str(data["numero"])," ",data["nom_voie"]," , ",str(data["code_postal"])," ",data["nom_commune"]])
    return string



def genrate_user_data(id):
        #generate random data for user table
    data = {"_id": id , "sexe":('H' if random.getrandbits(1) == 1 else 'F'), "age":(random.randint(15, 31)), "addresse":(random_adress()),"appareil":('IOS' if random.getrandbits(1) == 1 else 'Android')}
    return data