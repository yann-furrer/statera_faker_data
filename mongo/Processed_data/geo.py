import requests
from requests.structures import CaseInsensitiveDict
import urllib.parse
import tqdm
#df ne sert qu'a faire beuge les focntion 
# il faut l'importer
df = []

def geocoding(address= str):
  
    #address = "7 Rue Henri Amédée Bellivier, Saint-André-de-Cubzac, France"
    
    url = "https://api.geoapify.com/v1/geocode/search?text="+urllib.parse.quote(address)+"&apiKey=0a16e6c5e3154a89b584d624b1f4acfd"
    #AIzaSyBamWuqidmGQgy6XPKUEaMOC8INvLcP_qs
    #url ="https://maps.googleapis.com/maps/api/geocode/json?address="+urllib.parse.quote(address)+"&key=AIzaSyBamWuqidmGQgy6XPKUEaMOC8INvLcP_qs&channel=1"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    resp = requests.get(url, headers=headers).json()

    #print("géo",resp["features"][0]["properties"])
    return resp["features"][0]["geometry"]["coordinates"][0], resp["features"][0]["geometry"]["coordinates"][1] ,resp["features"][0]["properties"]["city"], resp["features"][0]["properties"]["postcode"]

  #exemple result (-0.459123, 44.991016) long / lat
#geocoding("kj")
def get_coordinate(data, i): 
   


    lat = []
    long = []
   
   
    for elem in data:
           
            for k in data[0]:
              
                lat.append(k[0])
                long.append(k[1])
   
    return min(lat),max(lat), min(long), max(long)






def get_CSP_data(long , lat, df):
    
    # df est le nom du fichier à importer 
    for i in tqdm(range(len(df["features"]))):
    #print(i)
     
        minlat, maxlat, minlong, maxlong = get_coordinate(df["features"][i]["geometry"]["coordinates"][0],i)
       
        if minlat <= long <= maxlat and minlong <= lat <= maxlong:
      
          #print("true") 

          return df["features"][i]
    print("aune data trouvé")
    
#get_CSP_data(2.32100, 43.10300)     