import matplotlib.pyplot as plt

def calculate(hei,wei,year):
    bmr = 5*hei+13.7*wei - 6.8*year+66
    return bmr


year,hei,wei = 20,175,80

insert_calo = 1639
lost_calo = 7700

day = 0 
buffer =0 

day_list = [0] 
wei_list = [80] 

energe_buffer = 0

while True:
    day+=1
    out_calo = calculate(hei,wei,year)- 1639 - 5

    if out_calo <=0:
        break

    energe_buffer = energe_buffer+out_calo

    if lost_calo <= energe_buffer:
        wei-=1
        energe_buffer = energe_buffer- lost_calo
        day_list.append(day)
        wei_list.append(wei)

plt.plot(day_list,wei_list,".")
plt.xlabel("Day")
plt.ylabel("Weight")
plt.title("schedule")
tag_68_index = wei_list.index(68)
#達到目標體中
plt.text(day_list[tag_68_index], wei_list[tag_68_index], "* (Day is {},weight is {})".format(day_list[tag_68_index],wei_list[tag_68_index]))
#這輩子再也瘦不下去
plt.text(day_list[len(day_list)-1],wei_list[len(wei_list)-1],"O {},{}".format(day_list[len(day_list)-1],wei_list[len(wei_list)-1]))
plt.show()