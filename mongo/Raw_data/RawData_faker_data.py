import random


def generate_raw_data(id):
        #generate random data for user table
    size = 15
    data = {
            "_raw_id":  id,
        "mbti":{
            "energy": [random.uniform(0,1) for _ in range(size)],
            "information": [random.uniform(0,1) for _ in range(size)],
            "decision": [random.uniform(0,1) for _ in range(size)],
            "action_mode": [random.uniform(0,1) for _ in range(size)]
            
            },
            "politics_opinion": {
        "tolerance_stat": [random.uniform(0,1) for _ in range(size)]  ,
        "sharing_stat":[random.uniform(0,1) for _ in range(size)],
        "individualist_stat":[random.uniform(0,1) for _ in range(size)],
        "compliance_stat":[random.uniform(0,1) for _ in range(size)],
            },
            "Behavior":{
                "behavior_type":[random.uniform(0,1) for _ in range(size)], "behavior_ascending": [random.uniform(0,1) for _ in range(size)]
            }
              }
    return data
