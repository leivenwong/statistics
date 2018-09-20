import pandas as pd
import random as rd

from settings import Settings

def read_file(ai_settings):
    """read data from data_path"""
    ai_settings = Settings()
    file_path = ai_settings.file_path
    loads = pd.read_excel(file_path)
    return loads

def frofit_per(data_close):
    """compute profit rate per day or other cycle"""
    profit_per = list(range(len(data_close)))
    profit_per[0] = 0
    for i in range(1, len(data_close)):
        profit_per[i] = (data_close[i] / data_close[i - 1] - 1) * 100
    return profit_per

def compute_var(data):
    """compute var for data"""
    compute_average = sum(data) / len(data)
    var = list(range(len(data)))
    for n in range(len(data)):
        var[n] = (data[n] - compute_average) ** 2
    compute_var = sum(var) / len(data)
    return compute_var

def compute_var_bia(data):
    """compute var for data concider bias"""
    var_bia = 1 / (len(data) - 1)
    compute_average = sum(data) / len(data)
    var_sample = list(range(len(data)))
    for i in range(len(data)):
        var_sample[i] = (data[i] - compute_average) ** 2
    compute_var = sum(var_sample) * var_bia
    return compute_var

def random_sample(ai_settings, data, random_mark):
    """initiate random sample"""
    sample = list(range(ai_settings.sample_num))
    # refresh random_mark
    rd.shuffle(random_mark)
    for i in range(ai_settings.sample_num):
        sample[i] = data[random_mark[i]]
    return sample