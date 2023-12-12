import pandas as pd
import numpy as np
from scipy.stats import boxcox, zscore

class DataTransform:
    def __init__(self, dataframe):
        self.df = dataframe

    def convert_dates_to_datetime(self, date_columns):
        for column in date_columns:
            self.df[column] = pd.to_datetime(self.df[column], format='%b-%Y', errors='coerce')

    def convert_categorical_columns(self, categorical_columns):
        self.df[categorical_columns] = self.df[categorical_columns].astype('category')

    def drop_rows(self, dropped_rows):
        self.df = self.df.dropna(subset=dropped_rows)

    def drop_columns(self, columns_to_drop):
        self.df = self.df.drop(columns=columns_to_drop)
    
    def impute_mode(self, column_to_impute):
        self.df[column_to_impute].fillna(self.df[column_to_impute].mode()[0], inplace=True)

    def impute_mean(self, column_to_impute):
        self.df[column_to_impute].fillna(self.df[column_to_impute].mean(), inplace=True)

    def log_transform(self, column_to_transform):
        self.df[column_to_transform] = np.log1p(self.df[column_to_transform])
    
    def boxcox_transform(self, column_to_transform):
        original_values = self.df[column_to_transform]
        transformed_values, lmbda = boxcox(original_values)
        self.df[column_to_transform] = transformed_values

    def remove_outliers_zscore(self, column_to_transform, z_threshold=2):
        z_scores = zscore(self.df[column_to_transform])
        outliers = np.abs(z_scores) > z_threshold
        self.df = self.df[~outliers]
 
