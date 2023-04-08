import pandas as pd
import json
import tqdm
from statistics import median, quantiles
dt= pd.read_csv("./data/income_by_city.csv", delimiter=";")
dt2 = dt["niveau de vie ménage"].convert_dtypes(convert_integer=True)
#dt = dt.fillna(0)
#dt.to_csv("./data/income_by_city.csv", sep=";")
with open("./data/data_test_copy.geojson") as data:
        dj = json.load(data)
#print(dj["features"][0]["properties"])


def get_coordinate(data, i): 
   


    lat = []
    long = []
   
   
    for elem in data:
           
            for k in data[0]:
              
                lat.append(k[0])
                long.append(k[1])
   
    return min(lat),max(lat), min(long), max(long)

#print(len(dj["features"]))



def get_CSP_data(long , lat):
    # df est le nom du fichier à importer 
    for i in range(len(dj["features"])):
        #print(i)
     
        minlat, maxlat, minlong, maxlong = get_coordinate(dj["features"][i]["geometry"]["coordinates"][0],i)
       
        if minlat <= long <= maxlat and minlong <= lat <= maxlong:
      
            #print("true") 
        
            return dj["features"][i]["properties"]
    print(long, lat)
    print("echec de la recherche")
#get_CSP_data(2.32100, 43.10300)  





def menage_data_transform(data, age ):
   
    ind_snv = data["Ind_snv"] / data["Ind"]
 
    men_pauv = data["Men_pauv"]
    men = data["Men"]
    ratio_log_soc = data["Log_soc"] /(data["Log_soc"] + data["Log_av45"] + data["Log_70_90"] + data["Log_ap90"])
    ratio_men_pauv = men_pauv / (men_pauv +men)
    Nb_ind = data["Ind"]
    men_prop = data["Men_prop"]
    if age > 18:
         ind_label = "adulte"
    else:
         ind_label = "enfant"
#seuil de pauvreté
    poverty_brink = 13224
    
    

   
    return Nb_ind, ratio_log_soc, ratio_men_pauv , ind_snv, ind_label



def CSP_city_type(Nb_ind):
    #convertion de 200m2 en km2  
    Nb_ind = Nb_ind * 5
    city_type = None

    if Nb_ind >= 400:
          city_type = "Métropole"
    elif 400 <= Nb_ind >= 150:
           city_type = "Moyenne Ville"
    elif 150 <= Nb_ind >= 50:
           city_type = "Petite Ville"
    else:
           city_type = "Campagne"
    

   
          


    
    return city_type
# min Ind_snv: 8381.262857142856
# max Ind_snv: 66061.48421052631
# median Ind_snv: 22296.449
# quartile Ind_snv: [20253.633333333335, 22296.449, 24740.878259005145]

def est_income(income):
    quantiles_25 = 20253.633333333335
    median = 22296.449
    quantiles_75 = 24740.878259005145
    better_off = 3800
    rich =  45600
    if income < quantiles_25:
        label_income = "Pauvre"
        return label_income
    elif quantiles_25 <= income <= median:
        label_income = "classe moyenne inférieure"
        return label_income
    elif median <= income <= quantiles_75:
        label_income = "classe moyenne supérieure"
        return label_income
    elif better_off <= income <= rich:
        label_income = "aisé"
        return label_income
    elif income > 3800:
        label_income = "riche" 
        return label_income
    return label_income
