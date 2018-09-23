import pandas as pd
import random as rd
import math
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import cholesky

from statistics_settings import Settings
import statistics_functions as fuc
import sys
sys.path.append('D:\\python_project\\strategy_test')
import strategy_functions
import back_testing

#initiate settings
ai_settings = Settings()

#read raw hs300 data
hs300 = back_testing.out_net_value['target_net_value']
hs300 = pd.DataFrame(hs300)
net_value = back_testing.out_net_value['net_value']
net_value = pd.DataFrame(net_value)

#select x,y for compute correlation
profit_ln_x = hs300.loc[0:, 'target_net_value']
profit_ln_y = net_value.loc[0:, 'net_value']

#compute r
r = fuc.compute_r(profit_ln_x, profit_ln_y)
out = pd.DataFrame()
out['x'] = profit_ln_x
out['y'] = profit_ln_y
print(out)
print("Correlation r is: "+str(r))