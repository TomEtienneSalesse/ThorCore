import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import kurtosis

def basic_statistics(data):
    statistics = data.describe()
    return statistics

def get_gap(list):
    gap = [list[i] - list[i-1] for i in range(1, len(list))]
    return gap

def statistics_data(data):
    grouped_data = data.groupby(0)
    test_statistics = []

    for i in range  (1,len(grouped_data)):
        max_value_time = max(list(grouped_data.get_group(i)[3]))
        nuclei_variation = get_gap(list(grouped_data.get_group(i)[4]))
        mass_variation = get_gap(list(grouped_data.get_group(i)[5]))
        energy_variation = get_gap(list(grouped_data.get_group(i)[6]))
        test_statistics.append([i, max_value_time, nuclei_variation, mass_variation, energy_variation])

    stats=[]

    for test in test_statistics:
        test_number = test[0]
        for parameter in [2,3,4]:
            # Mean
            mean_value = np.mean(test[parameter])
            # Range
            range_value = np.ptp(test[parameter])
            # Variance
            variance = np.var(test[parameter])
            # median
            median = np.median(test[parameter])
            # Mean Deviation
            mean_deviation = np.mean(np.abs(test[parameter] - mean_value))
            # tandard deviation
            standard_deviation = np.std(test[parameter])
            # Fisher-Pearson coeffcient of Skewness
            data_array = np.array(test[parameter])
            if len(test[parameter])>1 :
                skewness = np.mean((data_array - mean_value) ** 3) / (standard_deviation ** 3)
            if len(test[parameter])<=1 :
                skewness = None
            # Kurtosis measure
            if len(test[parameter])>1 :
                kurt = kurtosis(data_array)
            if len(test[parameter])<=1 :
                kurt = None
            stats.append( {
                "Test number" : test_number,
                "Value" : parameter,
                "Mean Value": mean_value,
                "Range": range_value,
                "Variance": variance,
                "Median": median,
                "Mean Deviation": mean_deviation,
                "Standard Deviation": standard_deviation,
                "Skewness": skewness,
                "Kurtosis": kurt
                })
    return(stats)