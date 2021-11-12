from datetime import datetime
import numpy as np
all_movies={}
movies = True
serial_no = 0
tuple_arr =[]
duration_arr = []
sorted_duration_arr = []
day_arr = []
sorted_day_arr = []
final_arr =[]
ll = 0
hl = 0
index = 0
# no input validation
# therefore, follow instrunctions
print("mm/dd/yy date to be entered in this format(same year) ")


# Asking user for movie details
while movies:
    serial_no = serial_no + 1
    movie_name=input("enter movie name - ")
    start_date=input("enter the starting date - ")
    end_date=input("enter the ending date - ")
    start_day = datetime.strptime(start_date, '%m/%d/%y').timetuple().tm_yday
    end_day = datetime.strptime(end_date, '%m/%d/%y').timetuple().tm_yday
    all_movies.update({serial_no:{"name":movie_name,"start_date":start_date,"end_date":end_date,"tuple":(start_day,end_day-start_day,serial_no)}})
   
    repeat = input("do you want to add more?yes/no - ")
    if repeat == "no":
        movies =False

# display all movie details
print(all_movies)

# create tuples array for (start day and duration)
for item in all_movies:
    tuple_arr.append(all_movies.get(item).get("tuple"))


# sorting tuples based on duration
#------------------------------------------
for item in tuple_arr:
    duration_arr.append(item[1])
duration_arr.sort()
print(duration_arr)

for item in np.unique(duration_arr):
    for tup in tuple_arr:
        if tup[1] == item:
            sorted_duration_arr.append(tup)
print(sorted_duration_arr)


# sorting tuples based on starting day
#------------------------------------------
for item in sorted_duration_arr:
    day_arr.append(item[0])
day_arr.sort()
print(day_arr)

for item in np.unique(day_arr):
    for tup in sorted_duration_arr:
        if tup[0] == item:
            sorted_day_arr.append(tup)
print(sorted_day_arr)


# movie recommendation logic for max profit
final_arr.append(sorted_day_arr[0])
ll = sorted_day_arr[0][0]
hl = sorted_day_arr[0][0] + sorted_day_arr[0][1]
for item in sorted_day_arr[1:]:
    if (item[0] > ll  and (item[0] + item[1])< hl):
        ll = item[0]
        hl = item[0] + item[1]
        final_arr.pop(index)
        final_arr.append(item)  
    elif (item[0] > hl):
        ll = item[0]
        hl = item[0] + item[1]
        final_arr.append(item)
        index = index + 1
print(final_arr)

# recommended movies
for item in final_arr:
    print(all_movies.get(item[2]))

# revenue made 
print("profit:"+str(len(final_arr))+"cr")