import matplotlib.pyplot as plt


# bmr 計算公式
def bmr(weight, height, age):
    return 13.7*weight + 5*height - 6.8*age+66

# 畫圖
def draw(x,y):
    plt.plot(x,y,".")
    plt.xlabel("Day")
    plt.ylabel("Weight")
    plt.title("schedule")

    tag_68_index = y_list.index(68)

    #達到目標體中
    plt.text(x[tag_68_index], y[tag_68_index], "* (Day is {},weight is {})".format(x[tag_68_index],y[tag_68_index]))
    #這輩子再也瘦不下去
    plt.text(x[len(x)-1],y[len(y)-1],"O {},{}".format(x[len(x)-1],y[len(x)-1]))

    plt.show()  


# 年齡 身高 體中
age = 20
height = 175
weight = 80

# 每天攝取熱量
everyday_eat_calo = 1639

# 消耗7700大卡可瘦下1公斤
lost_weight_calo = 7700

day = 0 #天數計算 
buffer =0 #卡路里暫存器

x_list = [0] #天數
y_list = [80] #體重


while 1:
    day = day + 1
    everyday_lost_calo = bmr(weight, height, age) - 1639 - 5

    if everyday_lost_calo <=0:
        break

    buffer = buffer + everyday_lost_calo

    if buffer >= lost_weight_calo:
        weight = weight -1 
        buffer = buffer - everyday_eat_calo
        print("Day {} weight is {}".format(day,weight))
        x_list.append(day)
        y_list.append(weight)
        
draw(x_list,y_list)


