
import numpy as np
import random
import matplotlib.pyplot as plt
from scipy import interpolate

from dataStream import run


def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i])



if __name__ == '__main__':
    print("Starting the Skiplist experiment with Visualization")
    print("Please enter the count of numbers you want to experiment on")
    num_of_inputs = int(input())
    print("Please enter the limit of numbers you want to experiment on. EX: enter 1000 for experimenting on numbers from 1-1000")
    limit = int(input())
    print("Type of experiment: uar(uniformly distributed random numbers)/exp(exponentially distributed random numbers)")
    exp_type = input()
    if(exp_type == "exp"):
        print("please enter the distribution scale(int) EX: 1/2.5/3")
        scale = float(input())
    elif(exp_type == "uar"):
        scale = 0
    res = run(num_of_inputs, limit, exp_type, scale)
    
   

#    Graph 1(Time comparison during operation)
    # X_axis = np.arange(num_of_inputs)
    # x1 = np.linspace(X_axis.min(), X_axis.max(), 50)

    # y = interpolate.make_interp_spline(X_axis, res.get("times").get("skiplist1_basic"))
    # y = y(x1)
    # y = np.where(y < 0, 0, y)
    # plt.plot(x1, y,label='skiplist1_basic')

    # y = interpolate.make_interp_spline(X_axis, res.get("times").get("skiplist2_one"))
    # y = y(x1)
    # y = np.where(y < 0, 0, y)
    # plt.plot(x1, y,label='skiplist2_one')

    # y = interpolate.make_interp_spline(X_axis, res.get("times").get("skiplist3_top"))
    # y = y(x1)
    # y = np.where(y < 0, 0, y)
    # plt.plot(x1, y,label='skiplist3_top')

    # y = interpolate.make_interp_spline(X_axis, res.get("times").get("skiplist4_rand"))
    # y = y(x1)
    # y = np.where(y < 0, 0, y)
    # plt.plot(x1, y,label='skiplist4_rand')
    # plt.xticks(rotation=90)
    # plt.xlabel("Order of numbers")
    # plt.ylabel("Time taken(ms)")
    # plt.title("Time taken during operation of four variations of skiplist")
    # plt.legend()
    # plt.show()
    # plt.savefig("time_trend_comparison_during_operation.png")



#    Graph 2(Average Time comparison)
    # X_axis = np.arange(num_of_inputs)
    # plt.figure(figsize=(16,10), dpi= 80)
    # all_colors = list(plt.cm.colors.cnames.keys())
    # x1 = np.linspace(X_axis.min(), X_axis.max(), 50)
    # c = random.choices(all_colors, k=len(x1))
    # c = ["red", "blue", "green", "pink"]

    # x1 = ["Skiplist_Basic","Skiplist_One","Skiplist_Top","Skiplist_Rand"]
    # y = [res.get("times").get("skiplist1_basic_avg"), res.get("times").get("skiplist2_one_avg"), res.get("times").get("skiplist3_top_avg"), res.get("times").get("skiplist4_rand_avg")]
    # plt.bar(x1, y, color=c)
    # addlabels(x1, y)

    # plt.xticks(rotation=90)
    # plt.xlabel("Order of numbers")
    # plt.ylabel("Time taken(s)")
    # plt.title("Time taken during operation of four variations of skiplist")
    # # plt.legend()
    # plt.show()
    # plt.savefig("total_time_comparison_during_operation.png")




#    Graph 3(Average movement comparison)
    X_axis = np.arange(num_of_inputs)
    plt.figure(figsize=(16,10), dpi= 80)
    all_colors = list(plt.cm.colors.cnames.keys())
    x1 = np.linspace(X_axis.min(), X_axis.max())
    x1 = ["Skiplist_Basic","Skiplist_One","Skiplist_Top","Skiplist_Rand"]
    c = ["red", "blue", "green", "pink"]
    y = [res.get("movement_count").get("skiplist1_basic"), res.get("movement_count").get("skiplist2_one"), res.get("movement_count").get("skiplist3_top"), res.get("movement_count").get("skiplist4_rand")]
    plt.bar(x1, y, color=c)
    addlabels(x1, y)
    # plt.ylim(min(y), max(y))
    # plt.yticks(range(min(y), max(y)))
    plt.xticks(rotation=90)
    # plt.xlabel("Order of numbers")
    plt.ylabel("Movements taken")
    plt.title("Total movements during insertion/search of four variations of skiplist")
    # plt.legend()
    plt.show()
    plt.savefig("movement_comparison_during_operation.png")


    