import json
with open('precipitation.json') as file:
  precipitation_file = json.load(file)

import csv
with open('stations.csv') as filecsv:
    stations_file = csv.reader(filecsv)
#CSV file was just loaded for later. I realised we didnt need it immediately after loading it in.

seattle = "GHCND:US1WAKG0038"
total = {}
for precip_data in precipitation_file:
    if precip_data["station"] == seattle:
        print(precip_data)
#So what I have done above is defined the seatlle code first and then run a for loop to filter out the dictionaries. This way if my seattle code changes later, it will also change in the loop.
        date = precip_data["date"]
        split_date = date.split("-")
        print(split_date)
        month = split_date[1]
        print(month)
        # if month == "01":
        #     print (month)
        #     if "01" in total:
        #         total["01"] +=precip_data["value"]
        #     else:
        #         total["01"] = precip_data["value"]

# Above, the dates were split by '-' and the month was printed for january. Then the total value of precipitation for january was calculated.

        if month in total:
            total[month] +=precip_data["value"]
        else:
            total[month] = precip_data["value"]
print(total)

# In the above loop, the total value was found for all months

# Part 2






    


    

