import sys  
sys.path.insert(1, './mongo/db')
sys.path.insert(1, './mongo/User')
sys.path.insert(1, './mongo/Raw_data')
sys.path.insert(1, './mongo/Processed_data')
from getVariables import User, RawData, ProcessedData
from mbti_ import normalized_means, MBTI_letter


def proccesing():

    all_id_request= RawData.distinct('_raw_id')

    for id in  all_id_request:

        data = RawData.find_one({"_raw_id": id})

        energy_stat = normalized_means(data["mbti"]["energy"])
        information_stat = normalized_means(data["mbti"]["information"])
        decision_stat = normalized_means(data["mbti"]["decision"])
        action_mode = normalized_means(data["mbti"]["action_mode"])

        behavior_stat = normalized_means(data["Behavior"])
                                         

        post_data = {
        "process_id" : id, "MBTI":{
            "energy":{"energy_letter": MBTI_letter(energy_stat, "energy"), "energy_stat":energy_stat },
            "information":{"information_letter": MBTI_letter(energy_stat, "information"), "informatiob_stat": information_stat},
            "decision":{"decision_letter": MBTI_letter(energy_stat, "decision"), "decision_stat": decision_stat},
            "action_mode":{"action_mode_letter": MBTI_letter(energy_stat, "action_mode"), "action_mode_stat": action_mode}
        },
        "Politics":{
            "imigration_stat": normalized_means(data["politics_opinion"]["imigration_stat"]) ,
            "chomage_stat":normalized_means(data["politics_opinion"]["chomage_stat"]),
            "politics_label": "gauche"
        },
        "Social_data":{"latitude":123, "longitude":124, "age":17, 
            "CSP":{
                "estimed_household_income":1200, "parent_label": "pauvre", "city_type": "urbain" 
                }
        },

        "Behavoir": {"behavior_stat" : behavior_stat, "behavior_type": "pollueur"}
        
        

    }
        ProcessedData.insert_one(post_data)
    

proccesing()


#all_id_request= RawData.distinct('_raw_id')
#print(RawData.find_one({"_raw_id": "ccb05cfc-ca42-11ed-a924-de5d40a64ae1"}))
#for i in all_id_request:
 #   print(i)
        

