import pandas as pd
import random as rd
import math
import matplotlib.pyplot as plt

from settings import Settings
import functions as fuc

#initiate settings
ai_settings = Settings()

#read raw hs300 data
hs300 = fuc.read_file(ai_settings)
hs300 = pd.DataFrame(hs300)

#select close price for compute
data_close = hs300.loc[0:, 'close']
print(data_close)
profit_day = fuc.frofit_per(data_close)

#set random sample mark
random_mark = list(range(len(profit_day)))

#iniciate sample list and average list
avg_sample = list(range(ai_settings.cycle_num))
e_var_sample = list(range(ai_settings.cycle_num))

#compute real average value
real_average = sum(profit_day) / len(profit_day)

#compute real var value
real_var = fuc.compute_var(profit_day)

#start main cycle
for n in range(ai_settings.cycle_num):
    #print cycle number
    print("Cycle "+str(n))

    #compute random sample for this cycle
    sample = fuc.random_sample(ai_settings, profit_day, random_mark)

    #compute sample's average value for this cycle
    avg_sample[n] = sum(sample) / len(sample)

    # compute sample's var value for this cycle
    e_var_sample[n] = fuc.compute_var_bia(sample)

#compute predict value
predict_avg = sum(avg_sample) / len(avg_sample)
predict_var = sum(e_var_sample) / len(e_var_sample)

#print predict value and real value
print("Predict average: "+str(predict_avg))
print("Predict var: "+str(predict_var))
print("Real average: "+str(real_average))
print("Real var: "+str(real_var))

#set window size for plot
plt.figure(dpi=128, figsize=(10,6))

#show hist plot
plt.figure(1)
plt.subplot(121)
plt.hist(avg_sample, 100, color="Blue", density=1)
plt.subplot(122)
plt.hist(e_var_sample, 100, color="Red", density=1)
plt.show()