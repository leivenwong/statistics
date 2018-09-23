import pandas as pd
import random as rd
import math
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import cholesky

from statistics_settings import Settings
import statistics_functions as fuc


#initiate settings
ai_settings = Settings()

#read raw hs300 data
hs300 = pd.read_excel(ai_settings.file_path_1)
hs300 = pd.DataFrame(hs300)

#select close price for compute
data_close = hs300.loc[0:, 'close']
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


#if settings is true show hist plot
if ai_settings.draw_out and __name__ == '__main__':
    fuc.draw_out(normal_sample, profit_day, avg_sample, e_var_sample,
        ai_settings)