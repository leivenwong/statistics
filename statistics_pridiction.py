import pandas as pd
import random as rd
import math
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import cholesky

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

#initiate normal distribution sample
normal_sample = list(range(ai_settings.cycle_num))
normal_sample = np.random.normal(real_average, real_var, ai_settings.cycle_num)

#print predict value and real value
print("Predict average: "+str(predict_avg))
print("Predict var: "+str(predict_var))
print("Real average: "+str(real_average))
print("Real var: "+str(real_var))

#set window size for plot
plt.figure(dpi=128, figsize=(10,6))

#show hist plot
plt.figure(1)

plt.subplot(221)
plt.title("Nomal distribution",fontsize=12)
plt.hist(normal_sample, bins=ai_settings.hist_bins, color="Orange", density=1)

plt.subplot(222)
plt.title("Profit per day",fontsize=12)
plt.hist(profit_day, bins=200, color="Green", density=1)

plt.subplot(223)
plt.title("Predict average",fontsize=12)
plt.hist(avg_sample, bins=ai_settings.hist_bins, color="Blue", density=1)

plt.subplot(224)
plt.title("Predict var",fontsize=12)
plt.hist(e_var_sample, bins=ai_settings.hist_bins, color="Red", density=1)
plt.show()