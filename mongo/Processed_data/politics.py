
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(1, './mongo/db')
from getVariables import User, RawData
import json
data =  RawData.find_one({"_raw_id" :"49f4a110-c83a-11ed-ac50-de5d40a64ae0"})

def normalized_means(array_of_value):
    #array_of_value = [0.5, 0.4, 0.2, 0.7, 0.8, 0.34, 0.75,0.5, 0.4, 0.2, 0.7, 0.8, 0.34, 0.75]
    
    #calcule de la moyenne
    mean_ = mean(array_of_value)
    # c'est la moyenne repésentant une choix neutre
    # une fonction de normalisation produit un résultat entre 0 t 1
    # https://www.datanovia.com/en/fr/blog/comment-normaliser-et-standardiser-les-donnees-dans-r-pour-une-visualisation-en-heatmap-magnifique/#:~:text=La%20normalisation%20standard%2C%20%C3%A9galement%20appel%C3%A9e,unit%C3%A9s%20d'%C3%A9cart%2Dtype.
    mean_mbti = 0.5
    #std_ = np.std(array_of_value)
    #calcul du max et min pour normaliser les données
    max =np.max(array_of_value)
    min = np.min(array_of_value)

    #creation d'un tableau vide pour les données normalisées
    normalised_array = []
    for value in array_of_value:
        d = (value - min)/(max-min)
        #print(value,"d:", d)
        normalised_array.insert(0,d )
    mean_normalised = mean(normalised_array)
    return mean_normalised


    


def MBTI_letter(mean, type):
    if type == "energy":
        return 'I' if mean > 0.5 else 'E'
    elif type == "information":
        return 'N' if mean > 0.5 else 'S'
    elif type == "decision":
        return 'F' if mean > 0.5 else 'T'
    elif type == "action_mode":
        return 'P' if mean > 0.5 else 'J'

    
    
