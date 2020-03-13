# -*- coding: utf-8 -*-

# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '105070039.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
      
# Remove the data whose value of the WDSD (wind speed) column is '-99.000' or '-999.000'.
filter_data = list(filter(lambda item: item['WDSD'] != '-99.000' and item['WDSD'] != '-999.000' , data))

# Retrive all data points which station id are "C0A880","C0F9A0","C0G640","C0R190" and "C0X260" as a list individually.
C0A880_data = list(filter(lambda item: item['station_id'] == 'C0A880', filter_data))
C0F9A0_data = list(filter(lambda item: item['station_id'] == 'C0F9A0', filter_data))
C0G640_data = list(filter(lambda item: item['station_id'] == 'C0G640', filter_data))
C0R190_data = list(filter(lambda item: item['station_id'] == 'C0R190', filter_data))
C0X260_data = list(filter(lambda item: item['station_id'] == 'C0X260', filter_data))

# Define lists to store the values of the WDSD (wind speed) except for '-99.000' or '-999.000' for "C0A880","C0F9A0","C0G640","C0R190" and "C0X260".
C0A880_WDSD_value = []
C0F9A0_WDSD_value = []
C0G640_WDSD_value = []
C0R190_WDSD_value = []
C0X260_WDSD_value = []

# Processing the data which station id is "C0A880"
if (len(C0A880_data) >= 2):   
    for index1 in range(len(C0A880_data)):
        C0A880_WDSD_value.append(C0A880_data[index1]['WDSD'])
    C0A880_WDSD_max = max(C0A880_WDSD_value)
    C0A880_WDSD_min = min(C0A880_WDSD_value)
    C0A880_WDSD_range = float(C0A880_WDSD_max) - float(C0A880_WDSD_min)
    C0A880_dict = ['C0A880',C0A880_WDSD_range]
else:
    C0A880_dict = ['C0A880','None'] 

# Processing the data which station id is "C0F9A0"
if (len(C0F9A0_data) >= 2):   
    for index2 in range(len(C0F9A0_data)):
        C0F9A0_WDSD_value.append(C0F9A0_data[index2]['WDSD'])
    C0F9A0_WDSD_max = max(C0F9A0_WDSD_value)
    C0F9A0_WDSD_min = min(C0F9A0_WDSD_value)
    C0F9A0_WDSD_range = float(C0F9A0_WDSD_max) - float(C0F9A0_WDSD_min)
    C0F9A0_dict = ['C0F9A0',C0F9A0_WDSD_range]
else:
    C0F9A0_dict = ['C0F9A0','None'] 

# Processing the data which station id is "C0G640"    
if (len(C0G640_data) >= 2):   
    for index in range(len(C0G640_data)):
        C0G640_WDSD_value.append(C0G640_data[index]['WDSD'])
    C0G640_WDSD_max = max(C0G640_WDSD_value)
    C0G640_WDSD_min = min(C0G640_WDSD_value)
    C0G640_WDSD_range = float(C0G640_WDSD_max) - float(C0G640_WDSD_min)
    C0G640_dict = ['C0G640',C0G640_WDSD_range]
else:
    C0G640_dict = ['C0G640','None']  

# Processing the data which station id is "C0R190"       
if (len(C0R190_data) >= 2):   
    for index in range(len(C0R190_data)):
        C0R190_WDSD_value.append(C0R190_data[index]['WDSD'])
    C0R190_WDSD_max = max(C0R190_WDSD_value)
    C0R190_WDSD_min = min(C0R190_WDSD_value)
    C0R190_WDSD_range = float(C0R190_WDSD_max) - float(C0R190_WDSD_min)
    C0R190_dict = ['C0R190',C0R190_WDSD_range]
else:
    C0R190_dict = ['C0R190','None']

# Processing the data which station id is "C0X260"   
if (len(C0X260_data) >= 2):   
    for index in range(len(C0X260_data)):
        C0X260_WDSD_value.append(C0X260_data[index]['WDSD'])
    C0X260_WDSD_max = max(C0X260_WDSD_value)
    C0X260_WDSD_min = min(C0X260_WDSD_value)
    C0X260_WDSD_range = float(C0X260_WDSD_max) - float(C0X260_WDSD_min)
    C0X260_dict = ['C0X260',C0X260_WDSD_range]
else:
    C0X260_dict = ['C0X260','None']   

# Merge the processed data into a list named target_data
target_data = [C0A880_dict,C0F9A0_dict,C0G640_dict,C0R190_dict,C0X260_dict] 
target_data.sort() # Sort target_data in the lexicographical order   
#=======================================

# Part. 4
#=======================================
# Print result
print(target_data)
#========================================
