#have assumed a file name of 'parking_log.csv'
#have calculated time in mins 
#now works for multiple entry/exits of a single car 
#this is just the attempted solution for average time 

import csv 
import datetime

#converting the cvs to a dictionary 

with open('parking_log.csv', mode='r') as file:
    headernames = ['timestamp', 'reg', 'vehicle_type','entry/exit']
    csv_reader = csv.DictReader(file, headernames)

    data_list = []

    for row in csv_reader:
        data_list.append(row)

#finding the average length of car stay 

car_time = []

for data in data_list:
    if (data['vehicle_type']=='Car'):
        car_matched = False #logic to ensure each car entry is only matched to one exit 
        for car in data_list: 
            if (car_matched == False) and (data['reg'] == car['reg']) and (data['entry/exit'] == 'Entry') and (car['entry/exit'] == 'Exit'): 
                datetime_obj1 = datetime.datetime.strptime(data['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
                datetime_obj2 = datetime.datetime.strptime(car['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
                datetime_delta = datetime_obj2 - datetime_obj1
                total_mins = (datetime_delta.total_seconds())/60
                car_time.append((total_mins))
                car_matched = True
average_time = sum(car_time)/len(car_time)
print(f'the average time spent in the carpark,is {average_time} mins')

# finding the car that has entered the parking lot more than once. 

for data in data_list: 
    if (data['vehicle_type']=='Car'):
        for car in data_list: 
            if (data['reg'] == car['reg']) and (data['entry/exit'] == 'Entry') and (car['entry/exit'] == 'Entry'):
                count = 1
                count +=1 
print(f"car reg {data['reg']} has entered the car park {count} times")