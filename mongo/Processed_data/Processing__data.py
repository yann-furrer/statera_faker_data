import sys  
sys.path.insert(1, './mongo/db')
sys.path.insert(1, './mongo/User')
sys.path.insert(1, './mongo/Raw_data')
sys.path.insert(1, './mongo/Processed_data')
from getVariables import User, RawData, ProcessedData
from mbti_ import normalized_means, MBTI_letter
from geo import geocoding
from behavior import Behavior_type, behavior_ascending_function, behavior_type_function
from Social import menage_data_transform, get_CSP_data, get_coordinate, est_income, CSP_city_type
from politics import politics_label
from datetime import datetime
from tqdm import tqdm
import json
import pandas as pd





def proccesing():
        error = 0
    
        print("Load a data_test.geojson ")
        all_id_request= RawData.distinct('_raw_id')
        print(len(all_id_request))
        for id in  tqdm(all_id_request):
          
            if ProcessedData.find_one({"process_id": id, },{"lastupdate"} )== None:
                data = RawData.find_one({"_raw_id": id})
                user_data = User.find_one({"_id": id},{})
                
                #print(data)
                try:
                #Social data
                    long, lat = geocoding(user_data["addresse"])
                    CSP_data =  get_CSP_data(long, lat)
                    nb_ind,ratio_log_soc, ratio_men_pauv, estimed_income, Ind_label = menage_data_transform(CSP_data, user_data["age"])
                    label_income = est_income(estimed_income)
                    city_type = CSP_city_type(nb_ind)
                except:
                     nb_ind,ratio_log_soc, ratio_men_pauv, estimed_income, Ind_label , label_income, city_type = 0,0,0,0,0,0,0
                    
                     print(error)
                     print("erreur dans l'adresse")
                     print(user_data["addresse"])
                     error = error + 1
                #mbti
                energy_stat = normalized_means(data["mbti"]["energy"])
                information_stat = normalized_means(data["mbti"]["information"])
                decision_stat = normalized_means(data["mbti"]["decision"])
                action_mode = normalized_means(data["mbti"]["action_mode"])


                #Behavior
                behavior_type_stat = normalized_means(data["Behavior"]["behavior_type"])
                behavior_ascending_stat = normalized_means(data["Behavior"]["behavior_ascending"])
                behavior_type =Behavior_type(behavior_type_stat)

                #Politics
                tolerance_stat = normalized_means(data["politics_opinion"]["tolerance_stat"]) ,
                sharing_stat = normalized_means(data["politics_opinion"]["sharing_stat"]),
                individualist_stat = normalized_means(data["politics_opinion"]["individualist_stat"]),
                compliance_stat =normalized_means(data["politics_opinion"]["compliance_stat"]),


                    
               




                post_data = {
                "process_id" : id, "MBTI":{
                    "energy":{"energy_letter": MBTI_letter(energy_stat, "energy"), "energy_stat":energy_stat },
                    "information":{"information_letter": MBTI_letter(energy_stat, "information"), "informatiob_stat": information_stat},
                    "decision":{"decision_letter": MBTI_letter(energy_stat, "decision"), "decision_stat": decision_stat},
                    "action_mode":{"action_mode_letter": MBTI_letter(energy_stat, "action_mode"), "action_mode_stat": action_mode},
                    "result": str(MBTI_letter(energy_stat, "energy") + MBTI_letter(energy_stat, "information") + MBTI_letter(energy_stat, "decision") + MBTI_letter(energy_stat, "action_mode"))
                },
                "Politics":{
                    "tolerance_stat": normalized_means(data["politics_opinion"]["tolerance_stat"]) ,
                    "sharing_stat":normalized_means(data["politics_opinion"]["sharing_stat"]),
                    "individualist_stat":normalized_means(data["politics_opinion"]["individualist_stat"]),
                    "compliance_stat":normalized_means(data["politics_opinion"]["compliance_stat"]),
                    "politics_label": politics_label(tolerance_stat, sharing_stat, individualist_stat, compliance_stat)
                    
                },
                "Social_data":{ "longitude":long,"latitude":lat, "age":user_data["age"], 
                    "CSP":{
                        "estimed_income":estimed_income,"Ind": Ind_label,  "income_label": label_income, "city_type": city_type, "poor_rate_area_200m":ratio_men_pauv , 'social_housing_rate_area_200m':ratio_log_soc
                        }
                },

                "Behavoir": {"behavior__assandant_stat" : behavior_ascending_stat,  "behavior_type_stat" :behavior_type_stat ,"behavior_type":behavior_type_function(behavior_type_stat)  ,"behavior_ascandant" :behavior_ascending_function(behavior_ascending_stat)}, 
                "lastupdate": datetime.now()
                

            }
                ProcessedData.insert_one(post_data)
    
        
           # print("erreur dans l'adresse")
        #print( post_data)
        print("ratio error :", error /len(all_id_request)*100, "%")
    

proccesing()
