import sys  
sys.path.insert(1, './mongo/db')
sys.path.insert(1, './mongo/User')
sys.path.insert(1, './mongo/Raw_data')
sys.path.insert(1, './mongo/Processed_data')
from getVariables import User, RawData, ProcessedData
from mbti_ import normalized_means, MBTI_letter
from geo import geocoding
from behavior import behavior_ascending_function, behavior_type_function,set_polution_type, polution_type_function, find_indices
from Social import menage_data_transform, get_CSP_data, get_coordinate, est_income, CSP_city_type
from politics import politics_label
from datetime import datetime
from tqdm import tqdm
import json
import pandas as pd





print("Load a data_test.geojson ")
def proccesing():
        error = 0
    
        all_id_request= RawData.distinct('_raw_id')
        #print(len(all_id_request))
        for id in  tqdm(all_id_request):
          
            if ProcessedData.find_one({"process_id": id, },{"lastupdate"} )== None:
                data = RawData.find_one({"_raw_id": id})
                user_data = User.find_one({"_id": id},{})
              
                try:
                #Social data
                    long, lat,city, postocde = geocoding(user_data["addresse"])
                    CSP_data =  get_CSP_data(long, lat)
                    nb_ind,ratio_log_soc, ratio_men_pauv, estimed_income, Ind_label = menage_data_transform(CSP_data, user_data["age"])
                    label_income = est_income(estimed_income)
                    city_type = CSP_city_type(nb_ind)
                except:
                     nb_ind,ratio_log_soc, ratio_men_pauv, estimed_income, Ind_label , label_income, city_type = 0,0,0,0,0,0,0
                    
                    

                     print(user_data["addresse"])
                     error = error + 1
                #mbti
                energy_stat = normalized_means(data["mbti"]["energy"])
                information_stat = normalized_means(data["mbti"]["information"])
                decision_stat = normalized_means(data["mbti"]["decision"])
                action_mode = normalized_means(data["mbti"]["action_mode"])
                #print("mbti", energy_stat, information_stat, decision_stat, action_mode)

                #Behavior
                behavior_type_stat = normalized_means(data["Behavior"]["behavior_type"])
                behavior_ascending_stat = normalized_means(data["Behavior"]["behavior_ascending"])
                #behavior_type = behavior_type_function(behavior_type_stat)

                #Politics
                tolerance_stat = normalized_means(data["politics_opinion"]["tolerance_stat"]) ,
                sharing_stat = normalized_means(data["politics_opinion"]["sharing_stat"]),
                individualist_stat = normalized_means(data["politics_opinion"]["individualist_stat"]),
                compliance_stat =normalized_means(data["politics_opinion"]["compliance_stat"]),


                    
               




                post_data = {
                "process_id" : id, "MBTI":{
                    "energy":{"energy_letter": str(MBTI_letter(energy_stat, "energy")[0]), "energy_stat":energy_stat , "MBTI_type": str(MBTI_letter(energy_stat, "energy",)[1])},
                    "information":{"information_letter": str(MBTI_letter(information_stat, "information")[0]), "information_stat": information_stat, "MBTI_type": str(MBTI_letter(information_stat, "information")[1])},
                    "decision":{"decision_letter": str(MBTI_letter(decision_stat, "decision")[0]), "decision_stat": decision_stat, "MBTI_type": str(MBTI_letter(decision_stat, "decision")[1])},
                    "action_mode":{"action_mode_letter": str(MBTI_letter(action_mode, "action_mode")[0]), "action_mode_stat": action_mode, "MBTI_type": str(MBTI_letter(action_mode, "action_mode")[1]) },
                    "result": str(MBTI_letter(energy_stat, "energy")[0]) + str(MBTI_letter(information_stat, "information")[0]) + str(MBTI_letter(decision_stat, "decision")[0]) + str(MBTI_letter(action_mode, "action_mode")[0])
                },
                "Politics":{
                    "tolerance_stat": normalized_means(data["politics_opinion"]["tolerance_stat"]) ,
                    "sharing_stat":normalized_means(data["politics_opinion"]["sharing_stat"]),
                    "individualist_stat":normalized_means(data["politics_opinion"]["individualist_stat"]),
                    "compliance_stat":normalized_means(data["politics_opinion"]["compliance_stat"]),
                    "politics_label": politics_label(tolerance_stat, sharing_stat, individualist_stat, compliance_stat)
                    
                },
                "Social_data":{ "longitude":long,"latitude":lat, "age":user_data["age"], "city":city, "postcode":postocde,
                    "CSP":{
                        "estimed_income":estimed_income,"Ind": Ind_label,  "income_label": label_income, "city_type": city_type, "poor_rate_area_200m":ratio_men_pauv , 'social_housing_rate_area_200m':ratio_log_soc
                        }
                },

                "Behavior": {"behavior_assandant_stat" : behavior_ascending_stat,  "behavior_type_stat" :behavior_type_stat ,"behavior_type":behavior_type_function(behavior_type_stat)  ,"behavior_ascandant" :behavior_ascending_function(behavior_ascending_stat)}, 
                "polution" : set_polution_type(data),
                "lastupdate": datetime.now()
                

            }
                #ajout de l'objet pollution dans le json
                ProcessedData.insert_one(post_data)
    
        
          
        print("ratio error :", error /len(all_id_request)*100, "%")
    

proccesing()
