
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(1, './mongo/db')
from getVariables import User, RawData
import json


    


def avg_politics_opinion(tolerance_stat,sharing_stat, individualist_stat,compliance_stat):
    avg_po = sum(tolerance_stat+sharing_stat + individualist_stat)/ len(tolerance_stat +sharing_stat + individualist_stat)
    return avg_po




def politics_label(tolerance_stat,sharing_stat, individualist_stat,compliance_stat):
    politics_label =""
    if avg_politics_opinion(tolerance_stat,sharing_stat, individualist_stat,compliance_stat) <= 0.40:
        politics_label = "Gauche"
    elif 0.40 >= avg_politics_opinion(tolerance_stat,sharing_stat, individualist_stat,compliance_stat) <= 0.60:
        politics_label = "Centre"
    elif 0.6 >= avg_politics_opinion(tolerance_stat,sharing_stat, individualist_stat,compliance_stat) <= 1:
        politics_label = "Droite"
    else:
        politics_label =  "Erreur"

    if mean(compliance_stat) > 0.5 and 0.40 <= avg_politics_opinion(tolerance_stat,sharing_stat, individualist_stat,compliance_stat)<= 0.60: 
        politics_label = "Extreme "+ politics_label

    return politics_label