

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
from datetime import datetime
id = "a28f697e-d328-11ed-b771-de5d40a64ae1 "
o = ProcessedData.find_one({"process_id": id, },{"_id"} )
if ProcessedData.find_one({"process_id": id, },{"_id"} ) == None:
    print(ProcessedData.find_one({"process_id": id, },{"_id"}) )
print(o)

