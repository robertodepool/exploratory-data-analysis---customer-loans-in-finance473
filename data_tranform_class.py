import pandas as pd
import numpy as np
from scipy.stats import boxcox, zscore

class DataTransform:
    """
    A class for performing various transformations on a Pandas DataFrame.

    Attributes:
        df (pd.DataFrame): The input Pandas DataFrame.

    Methods:
        convert_dates_to_datetime(date_columns): Convert specified columns to datetime format.
        convert_categorical_columns(categorical_columns): Convert specified columns to categorical data type.
        drop_rows(dropped_rows): Drop rows with missing values in specified columns.
        drop_columns(columns_to_drop): Drop specified columns from the DataFrame.
        impute_mode(column_to_impute): Impute missing values in a column with its mode.
        impute_mean(column_to_impute): Impute missing values in a column with its mean.
        log_transform(column_to_transform): Apply a log transformation to a specified column.
        boxcox_transform(column_to_transform): Apply a Box-Cox transformation to a specified column.
        remove_outliers_zscore(column_to_transform, z_threshold=2): Remove outliers using z-score method.
    """
    def __init__(self, dataframe):
        self.df = dataframe

    def convert_dates_to_datetime(self, date_columns):
        """
        Convert specified columns to datetime format.

        Args:
            date_columns (list): List of column names to be converted to datetime format.
        """
        for column in date_columns:
            self.df[column] = pd.to_datetime(self.df[column], format='%b-%Y')

    def convert_categorical_columns(self, categorical_columns):
        """
        Convert specified columns to categorical data type.

        Args:
            categorical_columns (list): List of column names to be converted to categorical data type.
        """
        self.df[categorical_columns] = self.df[categorical_columns].astype('category')

    def drop_rows(self, dropped_rows):
        """
        Drop rows with missing values in specified columns.

        Args:
            dropped_rows (list): List of column names to check for missing values.
        """
        self.df = self.df.dropna(subset=dropped_rows)

    def drop_columns(self, columns_to_drop):
        """
        Drop specified columns from the DataFrame.

        Args:
            columns_to_drop (list): List of column names to be dropped from the DataFrame.
        """
        self.df = self.df.drop(columns=columns_to_drop)
    
    def impute_mode(self, column_to_impute):
        """
        Impute missing values in a column with its mode.

        Args:
            column_to_impute (str): Name of the column to be imputed.
        """
        self.df[column_to_impute].fillna(self.df[column_to_impute].mode()[0], inplace=True)

    def impute_mean(self, column_to_impute):
        """
        Impute missing values in a column with its mean.

        Args:
            column_to_impute (str): Name of the column to be imputed.
        """
        self.df[column_to_impute].fillna(self.df[column_to_impute].mean(), inplace=True)

    def log_transform(self, column_to_transform):
        """
        Apply a log transformation to a specified column.

        Args:
            column_to_transform (str): Name of the column to be log-transformed.
        """
        self.df[column_to_transform] = np.log1p(self.df[column_to_transform])
    
    def boxcox_transform(self, column_to_transform):
        """
        Apply a Box-Cox transformation to a specified column.

        Args:
            column_to_transform (str): Name of the column to be Box-Cox transformed.
        """
        original_values = self.df[column_to_transform]
        transformed_values, lmbda = boxcox(original_values)
        self.df[column_to_transform] = transformed_values

    def remove_outliers_zscore(self, column_to_transform, z_threshold=2):
        """
        Remove outliers using z-score method.

        Args:
            column_to_transform (str): Name of the column to be processed for outlier removal.
            z_threshold (float): Z-score threshold beyond which values are considered outliers.
        """
        z_scores = zscore(self.df[column_to_transform])
        outliers = np.abs(z_scores) > z_threshold
        self.df = self.df[~outliers]
 
