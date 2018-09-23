import pandas as pd
import random as rd
import matplotlib.pyplot as plt

from settings import Settings

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

def draw_out(normal_sample, profit_day, avg_sample, e_var_sample, ai_settings):
    # show hist plot
    plt.figure(1)

    plt.subplot(221)
    plt.title("Nomal distribution", fontsize=12)
    plt.hist(normal_sample, bins=ai_settings.hist_bins, color="Orange",
             density=1)

    plt.subplot(222)
    plt.title("Profit per day", fontsize=12)
    plt.hist(profit_day, bins=200, color="Green", density=1)

    plt.subplot(223)
    plt.title("Predict average", fontsize=12)
    plt.hist(avg_sample, bins=ai_settings.hist_bins, color="Blue", density=1)

    plt.subplot(224)
    plt.title("Predict var", fontsize=12)
    plt.hist(e_var_sample, bins=ai_settings.hist_bins, color="Red", density=1)
    plt.show()

def compute_r(profit_ln, profit_ln_roll):
    e_profit_ln = sum(profit_ln) / len(profit_ln)
    e_profit_ln_roll = sum(profit_ln_roll) / len(profit_ln_roll)
    var_profit_ln = compute_var(profit_ln)
    var_profit_ln_roll = compute_var(profit_ln_roll)
    cov_raw = [0] * len(profit_ln)
    for i in range(len(profit_ln)):
        cov_raw[i] = (profit_ln[i] - e_profit_ln) * (profit_ln_roll[i] -
            e_profit_ln_roll)
    cov = sum(cov_raw) / len(cov_raw)
    r = cov / (var_profit_ln ** (1 / 2) * var_profit_ln_roll ** (1 / 2))
    return r

def compute_roll(profit_ln, roll):
    profit_ln_roll = [0] * len(profit_ln)
    for n in range(roll):
        profit_ln_roll[n] = 0
    for i in range(roll, len(profit_ln)):
        profit_ln_roll[i] = profit_ln[i - 1]
    return profit_ln_roll