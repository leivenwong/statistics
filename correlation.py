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
hs300 = pd.read_excel(ai_settings.file_path_1)
hs300 = pd.DataFrame(hs300)
sh_all = pd.read_excel(ai_settings.file_path_2)
sh_all = pd.DataFrame(sh_all)
print(sh_all)

#select close price for compute
profit_ln = hs300.loc[0:, 'profit_ln']
profit_ln_2 = sh_all.loc[0:, 'profit_ln']

#compute r
r = fuc.compute_r(profit_ln, profit_ln_2)
out = pd.DataFrame()
out['sh300'] = profit_ln
out['sh_all'] = profit_ln_2
print(out)
print("Correlation r is: "+str(r))