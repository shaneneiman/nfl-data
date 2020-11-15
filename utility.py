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


# Print all columns containing a null value
def check_null_columns(df_list):
    for df in df_list:
        print("{}".format(df[df.columns[~df.isnull().all()]]))


# Print Pearson Correlation Coefficent and P-Value for input columns
def pval_pearson_coef(column1, column2):
    pearson_coefficient, p_value = stats.pearsonr(column1, column2)
    print("Pearson Correlation cofficient for {} is {}".format(column1.name, pearson_coefficient))
    print("P-Value for {} is {}".format(column1.name, p_value))
    if p_value > 0.05:
        print("Null cannot be rejected")
    else:
        print("Null can be rejected!!")