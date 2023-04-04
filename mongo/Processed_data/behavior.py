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
   

def Behavior_type(mean_):

    #print("mean " ,mean_)
    if mean_ < 0.25:
        return "Optimiste"
    elif 0.25 >= mean_ < 0.5:
        return " Pessimiste"
    elif 0.5 >= mean_ < 0.75:
        return "Egoîste"
    elif 0.75 >= mean_ < 1:
        return " Rationnel"
    # elif mean_ == 1:
    #     return "Climato séptique Bêta"
    


def behavior_type_function(array_of_value):
    type = normalized_means(array_of_value)
    if type <= 0.45:
        return "Climatoséptique"
    elif 0.45 >= type <= 1:
        return "Ecologiste"
    else : 
        return "Bêta" 
    

def behavior_ascending_function(mean):
  
    if mean <= 0.25:
        return "Optimiste"
    elif 0.25 >= mean <= 0.5:
        return "Pessimite"
    elif 0.5 >= mean <= 0.75:
        return "Egoîste"
    else : 
        return "Rationnel" 