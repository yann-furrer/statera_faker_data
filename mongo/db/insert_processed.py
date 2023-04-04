

import uuid  
import sys  
sys.path.insert(1, './mongo/')
sys.path.insert(1, './mongo/User')
sys.path.insert(1, './mongo/Raw_data')
sys.path.insert(1, './mongo/Processed_data')

from getVariables import User, RawData, ProcessedData
from User_faker_data import genrate_user_data
from RawData_faker_data import generate_raw_data
#User.delete_one({"_id":0})
from tqdm import tqdm

    
all_id_request= RawData.distinct('_raw_id')

for i in  tqdm(all_id_request):
    print(i)


