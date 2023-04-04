import sys  
sys.path.insert(1, './data')
import pandas as pd
import requests
from requests.structures import CaseInsensitiveDict
import urllib.parse
import geopandas as geo
from shapely.geometry import Polygon, LineString, Point

#df = pd.read_json("./data/France_data.json")
df = pd.read_json("./data/train.json")
for i in df["geometries"]:
    print( Polygon(i["coordinates"]))





def geocoding(address):
    #address = "7 Rue Henri Amédée Bellivier, Saint-André-de-Cubzac, France"
    url = "https://api.geoapify.com/v1/geocode/search?text="+urllib.parse.quote(address)+"&apiKey=0a16e6c5e3154a89b584d624b1f4acfd"
    #AIzaSyBamWuqidmGQgy6XPKUEaMOC8INvLcP_qs
    #url ="https://maps.googleapis.com/maps/api/geocode/json?address="+urllib.parse.quote(address)+"&key=AIzaSyBamWuqidmGQgy6XPKUEaMOC8INvLcP_qs&channel=1"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    resp = requests.get(url, headers=headers).json()

   # print(resp["features"][0]["geometry"]["coordinates"][0])
    return resp["features"][0]["geometry"]["coordinates"][0], resp["features"][0]["geometry"]["coordinates"][1]





