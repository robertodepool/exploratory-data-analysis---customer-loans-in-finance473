import pandas as pd
import numpy as np
from scipy.stats import boxcox, skew
import matplotlib.pyplot as plt
import seaborn as sns

class DataFrameInfo:
    """
    A class for providing insights and information about a Pandas DataFrame.

    Attributes:
        df (pd.DataFrame): The input Pandas DataFrame.

    Methods:
        describe_columns(columns=None): Get data types of specified columns or all columns.
        extract_statistical_values(columns=None): Extract statistical values (mean, std, min, max, etc.) of specified columns or all columns.
        count_distinct_values(columns=None): Count distinct values in specified columns or all columns.
        print_shape(): Print the shape of the DataFrame.
        count_null_values(columns=None): Count null values and calculate the percentage of null values in specified columns or all columns.
        data_skew(columns=None): Calculate skewness of specified columns or all columns.
        compare_transformations(column_to_transform): Compare the skewness and histograms of original, Box-Cox transformed, and log-transformed values of a column.
    """
    def __init__(self, df):
        self.df = df

    def describe_columns(self, columns=None):
        """
        Get data types of specified columns or all columns.

        Args:
            columns (list, optional): List of column names. If None, returns data types of all columns.
        Returns:
            pd.Series: Data types of specified columns or all columns.
        """
        if columns:
            return self.df[columns].dtypes
        else:
            return self.df.dtypes

    def extract_statistical_values(self, columns=None):
        """
        Extract statistical values (mean, std, min, max, etc.) of specified columns or all columns.

        Args:
            columns (list, optional): List of column names. If None, returns statistical values for all columns.
        Returns:
            pd.DataFrame: Statistical values for specified columns or all columns.
        """
        if columns:
            return self.df[columns].describe()
        else:
            return self.df.describe()

    def count_distinct_values(self, columns=None):
        """
        Count distinct values in specified columns or all columns.

        Args:
            columns (list, optional): List of column names. If None, counts distinct values for all columns.
        Returns:
            pd.Series: Counts of distinct values for specified columns or all columns (excluding columns with only one unique value).
        """
        if columns:
            distinct_counts = self.df[columns].nunique()
        else:
            distinct_counts = self.df.nunique()
        return distinct_counts[distinct_counts > 1]

    def print_shape(self):
        """
        Print the shape of the DataFrame.
        """
        return self.df.shape

    def count_null_values(self, columns=None):
        """
        Count null values and calculate the percentage of null values in specified columns or all columns.

        Args:
            columns (list, optional): List of column names. If None, counts null values for all columns.
        Returns:
            pd.DataFrame: Null counts and percentage null for specified columns or all columns.
        """
        if columns:
            null_counts = self.df[columns].isnull().sum()
        else:
            null_counts = self.df.isnull().sum()
        percentage_null = (null_counts / len(self.df)) * 100
        null_info = pd.DataFrame({
            'Null Count': null_counts,
            'Percentage Null': percentage_null
        })
        return null_info
    
    def data_skew(self, columns=None):
        """
        Calculate skewness of specified columns or all columns.

        Args:
            columns (list, optional): List of column names. If None, calculates skewness for all columns.
        Returns:
            pd.Series: Skewness values for specified columns or all columns.
        """
        return self.df[columns].skew(axis = 0, skipna = True)
    

    def compare_transformations(self, column_to_transform):
        """
        Compare the skewness and histograms of original, Box-Cox transformed, and log-transformed values of a column.

        Args:
            column_to_transform (str): Name of the column to be transformed.
        """
        original_values = self.df[column_to_transform]
        original_skew = skew(original_values)
        boxcox_transformed_values, _ = boxcox(original_values)
        boxcox_df = pd.DataFrame({f'Box-Cox Transformed {column_to_transform}': boxcox_transformed_values})
        boxcox_skew = skew(boxcox_transformed_values)
        log_transformed_values = np.log1p(original_values)
        log_df = pd.DataFrame({f'Log Transformed {column_to_transform}': log_transformed_values})
        log_skew = skew(log_transformed_values)
        print(f'Skewness - Original {column_to_transform}: {original_skew}')
        print(f'Skewness - Box-Cox Transformed {column_to_transform}: {boxcox_skew}')
        print(f'Skewness - Log Transformed {column_to_transform}: {log_skew}')
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 3, 1)
        sns.histplot(original_values, kde=True)
        plt.title(f'Original {column_to_transform}')
        plt.subplot(1, 3, 2)
        sns.histplot(boxcox_transformed_values, kde=True)
        plt.title(f'Box-Cox Transformed {column_to_transform}')
        plt.subplot(1, 3, 3)
        sns.histplot(log_transformed_values, kde=True)
        plt.title(f'Log Transformed {column_to_transform}')
        plt.tight_layout()
        plt.show()


    