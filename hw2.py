import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from numpy import mean, std


from google.colab import drive

drive.mount('/content/drive',force_remount=True)
path = r'/content/drive/My Drive/Colab Notebooks/pollution.csv'
df = pd.read_csv(path)

data = df.to_dict()
# ax = df.plot(subplots=True, layout=(8,1) , x='date',figsize=(12, 18)) 


date_array = []
pollution_array = []
dew_array = []
temp_array = []
press_array = []
wnd_dir_array = []
wnd_spd_array = []
snow_array = []
rain_array = []

def draw(date_array, pollution_array, dew_array, temp_array, press_array, wnd_dir_array, wnd_spd_array, snow_array, rain_array):
    plt.figure(figsize=(12,18),dpi=100)
    date_array = pd.to_datetime(date_array, format='%Y-%m-%d %H:%M:%S')
    plt.subplot(8,1,1)
    plt.plot(date_array,pollution_array,'b')
    plt.xlabel("date")
    plt.ylabel("pollution")
    plt.title("pollution")
    plt.subplot(8,1,2)
    plt.plot(date_array,dew_array,'g')
    plt.xlabel("date")
    plt.ylabel("dew")
    plt.title("dew")
    plt.subplot(8,1,3)
    plt.plot(date_array,temp_array,'r')
    plt.xlabel("date")
    plt.ylabel("temp")
    plt.title("temp")
    plt.subplot(8,1,4)
    plt.plot(date_array,press_array,'c')
    plt.xlabel("date")
    plt.ylabel("press")
    plt.title("press")
    plt.subplot(8,1,5)
    plt.plot(date_array,wnd_spd_array,'m')
    plt.xlabel("date")
    plt.ylabel("wnd_spd")
    plt.title("wnd_spd")
    plt.subplot(8,1,6)
    plt.plot(date_array,snow_array,'y')
    plt.xlabel("date")
    plt.ylabel("snow")
    plt.title("snow")
    plt.subplot(8,1,7)
    plt.plot(date_array,rain_array,'k')
    plt.xlabel("date")
    plt.ylabel("rain")
    plt.title("rain")



def function1():
    plt.figure(figsize=(10,8),dpi=100)
    plt.subplot(4,2,1)
    plt.plot(dew_array,pollution_array)
    plt.title("dew")
    plt.subplot(4,2,2)
    plt.plot(temp_array,pollution_array,".")
    plt.title("temp")
    plt.subplot(4,2,3)
    plt.plot(press_array,pollution_array,".")
    plt.title("press")
    plt.subplot(4,2,4)
    plt.plot(wnd_dir_array,pollution_array,".")
    plt.title("wnd_dir")
    plt.subplot(4,2,5)
    plt.plot(wnd_spd_array,pollution_array,".")
    plt.title("spd")
    plt.subplot(4,2,6)
    plt.plot(snow_array,pollution_array,".")
    plt.title("snow")
    plt.subplot(4,2,7)
    plt.plot(rain_array,pollution_array,".")
    plt.title("rain")


for col in data["date"]:
    date_array.append(data["date"][col])
for col in data["pollution"]:
    pollution_array.append(data["pollution"][col])
for col in data["dew"]:
    dew_array.append(data["dew"][col])
for col in data["temp"]:
    temp_array.append(data["temp"][col])
for col in data["press"]:
    press_array.append(data["press"][col])
for col in data["wnd_dir"]:
    wnd_dir_array.append(data["wnd_dir"][col])
for col in data["wnd_spd"]:
    wnd_spd_array.append(data["wnd_spd"][col])
for col in data["snow"]:
    snow_array.append(data["snow"][col])
for col in data["rain"]:
    rain_array.append(data["rain"][col])

draw(date_array, pollution_array, dew_array, temp_array, press_array,
     wnd_dir_array, wnd_spd_array, snow_array, rain_array)

day1_start = date_array.index("2010-02-01 00:00:00")
day1_end = date_array.index("2010-05-30 23:00:00")
day2_start = date_array.index("2011-02-01 00:00:00")
day2_end = date_array.index("2011-05-30 23:00:00")
day3_start = date_array.index("2012-02-01 00:00:00")
day3_end = date_array.index("2012-05-30 23:00:00")
day4_start = date_array.index("2013-02-01 00:00:00")
day4_end = date_array.index("2013-05-30 23:00:00")
day5_start = date_array.index("2014-02-01 00:00:00")
day5_end = date_array.index("2014-05-30 23:00:00")



collection_pollution = []
collection_dew = []
collection_temp = []


for i in range(day1_start, day1_end):
    collection_pollution.append(data["pollution"][i])
    collection_dew.append(data["dew"][i])
    collection_temp.append(data["temp"][i])

for i in range(day2_start, day2_end):
    collection_pollution.append(data["pollution"][i])
    collection_dew.append(data["dew"][i])
    collection_temp.append(data["temp"][i])

for i in range(day3_start, day3_end):
    collection_pollution.append(data["pollution"][i])
    collection_dew.append(data["dew"][i])
    collection_temp.append(data["temp"][i])

for i in range(day4_start, day4_end):
    collection_pollution.append(data["pollution"][i])
    collection_dew.append(data["dew"][i])
    collection_temp.append(data["temp"][i])
for i in range(day5_start, day5_end):
    collection_pollution.append(data["pollution"][i])
    collection_dew.append(data["dew"][i])
    collection_temp.append(data["temp"][i])


averge_pollution = mean(collection_pollution)
averge_dew = mean(collection_dew)
averge_temp = mean(collection_temp)

static_pollution = std(collection_pollution)
static_dew = std(collection_dew)
static_temp = std(collection_temp)


print("濃度平均值: {} 標準差: {}".format(averge_pollution,static_pollution))
print("溫度平均值: {} 標準差: {}".format(averge_temp,static_temp))
print("露點溫度平均值: {} 標準差: {}".format(averge_dew,static_dew))

function1()
