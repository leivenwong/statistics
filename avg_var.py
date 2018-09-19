import pandas as pd
import random as rd
import math
import matplotlib.pyplot as plt

#set sample numbers and cycle mumbers
sample_num = 1000
cycle_num = 5000

#read raw hs300 data
hs300 = pd.read_excel("399300.xlsx")
#hs300 = pd.DataFrame(hs300)

#select close price for compute
data_close = list()
data_close = hs300.loc[0: ,'close']
print(data_close)
profit_day = list(range(len(data_close)))
profit_day[0] = 0
for i in range(1,len(data_close)):
    profit_day[i] = (data_close[i]/data_close[i-1]-1) * 100
print(profit_day)

#set random sample mark
random_mark = list(range(len(profit_day)))


#iniciate sample list and average list
sample = list(range(sample_num))
avg_sample = list(range(cycle_num))
e_var_sample = list(range(cycle_num))

#compute real average value
real_average = sum(profit_day) / len(profit_day)

#compute real var value
var = list(range(len(profit_day)))
for n in range(len(profit_day)):
    var[n] = (profit_day[n] - real_average) ** 2
real_var = sum(var) / len(profit_day)

#start main cycle
for n in range(cycle_num):
    #refresh random_mark
    rd.shuffle(random_mark)

    #print cycle number
    print("Cycle "+str(n))
    for i in range(sample_num):
        sample[i] = profit_day[random_mark[i]]

    #compute sample's average value for this cycle
    avg_sample[n] = sum(sample) / len(sample)

    # compute sample's var value for this cycle
    var_sample = list(range(sample_num))
    var_bia = 1 / (sample_num - 1)
    for i in range(sample_num):
        var_sample[i] = (sample[i] - avg_sample[n]) ** 2
    e_var_sample[n] = sum(var_sample) * var_bia

#compute predict value
predict_avg = sum(avg_sample) / len(avg_sample)
predict_var = sum(e_var_sample) / len(e_var_sample)

#print predict value and real value
print("Predict average: "+str(predict_avg))
print("Predict var: "+str(predict_var))
print("Real average: "+str(real_average))
print("Real var: "+str(real_var))

#set window size
plt.figure(dpi=128, figsize=(10,6))

#show hist plot
plt.figure(1)
plt.subplot(121)
plt.hist(avg_sample, 100, color="Blue", density=1)
plt.subplot(122)
plt.hist(e_var_sample, 100, color="Red", density=1)
plt.show()