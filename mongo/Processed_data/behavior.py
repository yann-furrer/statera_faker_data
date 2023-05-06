from statistics import mean
import numpy as np
import matplotlib.pyplot as plt


def normalized_means(array_of_value):
    #array_of_value = [0.5, 0.4, 0.2, 0.7, 0.8, 0.34, 0.75,0.5, 0.4, 0.2, 0.7, 0.8, 0.34, 0.75]
    
    #calcule de la moyenne
    #mean_ = mean(array_of_value)
    # c'est la moyenne repésentant une choix neutre
    # une fonction de normalisation produit un résultat entre 0 t 1
    # https://www.datanovia.com/en/fr/blog/comment-normaliser-et-standardiser-les-donnees-dans-r-pour-une-visualisation-en-heatmap-magnifique/#:~:text=La%20normalisation%20standard%2C%20%C3%A9galement%20appel%C3%A9e,unit%C3%A9s%20d'%C3%A9cart%2Dtype.
    mean_mbti = 0.5
    #std_ = np.std(array_of_value)
    #calcul du max et min pour normaliser les données
    #print(array_of_value)
    max_ = max(array_of_value)
    min_ =min(array_of_value)

    #creation d'un tableau vide pour les données normalisées
    normalised_array = []
    for value in array_of_value:
        d = (value - min_)/(max_-min_)
        #print(value,"d:", d)
        normalised_array.insert(0,d )

    return mean(normalised_array)
   

def behavior_ascending_function(mean_):

   
    if mean_ < 0.25:
        return "Pessimiste"
    elif 0.25 <= mean_ <= 0.5:
        return " Optimiste"
    elif 0.5 <= mean_ <= 0.75:
        return "Rationnel"
    elif 0.75 <= mean_ <=1:
        return "Egoiste"




def behavior_type_function(mean_):
   
    if mean_ <= 0.45:
        return "climatoseptique"
    elif 0.45 <= mean_ <= 0.55:
        return "beta"
    elif mean_ > 0.55 : 
        return "ecologiste" 



def find_indices(list_to_check, item_to_find):
   
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    #print(indices)
    #print("list_to_check:", list_to_check)
    return indices


def polution_type_function( array_of_ascandant, array_of_type , array_polution_type, item_to_find, data_array):
    #print("item_to_find:", item_to_find)

    if item_to_find == "EMPTY ":
        return 0
    
    result = find_indices(array_polution_type, item_to_find)
   
    array_type = []
    array_ascandant = []
    
    for range in result:
        
        array_type.append(array_of_ascandant[range])
        array_ascandant.append(array_of_type[range])
    if len(array_of_type) ==0 or len(array_ascandant) ==0:
        array_type.append(0)
        array_ascandant.append(0)
   
    mean_type = mean(array_type)
    mean_ascandant = mean(array_ascandant)

   
    if data_array == "type":
        return mean_type
    else :
        return mean_ascandant

def set_polution_type(data):
    list_label_polution = ["EMPTY", "polution co2", "surpêche", "surproduction", "production de viande", "déchet plastique", "déforestation", "surexploitation des ressources", "co2", "déchet fossile", "dechet toxique", "déchet plastique", "déforestation", "surexploitation des ressources"]
    object = {}
    for label in list_label_polution:
        key_name = label
     
        object[key_name] = {"type_name":  key_name, "type_label" : behavior_type_function(polution_type_function(data["Behavior"]["behavior_ascending"],data["Behavior"]["behavior_type"] ,data["Behavior"]["polution_type"], key_name, "type" )), "type_value": polution_type_function(data["Behavior"]["behavior_ascending"],data["Behavior"]["behavior_type"] ,data["Behavior"]["polution_type"], key_name, "type" ),
        "ascandant_label": behavior_ascending_function(polution_type_function(data["Behavior"]["behavior_ascending"] ,data["Behavior"]["behavior_type"], data["Behavior"]["polution_type"], key_name, "ascending" )), "ascandant_value": polution_type_function(data["Behavior"]["behavior_ascending"] ,data["Behavior"]["behavior_type"], data["Behavior"]["polution_type"], key_name, "ascending" ) }
   
    return object


