import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


# Print all columns names for the inputted dataframe
def print_column_names(df):
    for col in df.columns:
        print(col)


# Print shape for all dataframes in the input list of dataframes
def print_shape(df_list):
    for df in df_list:
        print("{}".format(df.shape))


# Print Pearson Correlation Coefficent and P-Value for input columns
def pval_pearson_coef(column1, column2):
    pearson_coefficient, p_value = stats.pearsonr(column1, column2)
    print("Pearson Correlation cofficient is {}".format(pearson_coefficient))
    print("P-Value is {}".format(p_value))