
from datetime import datetime, time

#this function returns the loc address of the given date
from sklearn.preprocessing import MinMaxScaler

def normalize_array(array):
    scaler = MinMaxScaler()
    normalized_array = scaler.fit_transform(array)
    return normalized_array

def mean_loc(list):
   
    total = sum(list)
    mean = total / len(list)
    return mean



#sort in a list the localisation of the user by date

def get_localisation_by_date(loc_object, date):

    loc_temp_table = []
    for loc in loc_object:
       
        date = loc["date"] 
        if isinstance(date, str):
            date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

            time_start = time(18, 0, 0)  # 18:00:00
            time_end = time(23, 59, 59)  # 23:59:59

            if time_start <= date.time() <= time_end:
                loc_temp_table.append(loc["loc"])
    return loc_temp_table
          

#find user location b
def user_loc(loc_list):
    normalized_long =  normalize_array(loc_list["long"])
    normalized_lat =  normalize_array(loc_list["lat"])
    filtered_array_long = [value for value in loc_list if value >= (normalized_long.mean()+3) and value <= (normalized_long.mean()-3)]
    filtered_array_lat = [value for value in loc_list if value >= (normalized_lat.mean()+3) and value <= (normalized_lat.mean()-3)]
    mean_long = mean_loc(filtered_array_long)
    mean_lat = mean_loc(filtered_array_lat)
    return mean_long, mean_lat
   
   