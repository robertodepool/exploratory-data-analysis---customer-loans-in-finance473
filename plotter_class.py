import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from statsmodels.graphics.gofplots import qqplot

class Plotter:
    """
    A class for creating various plots and visualizations based on a Pandas DataFrame.

    Attributes:
        df (pd.DataFrame): The input Pandas DataFrame.

    Methods:
        discrete_probability_distribution(column_to_plot): Plot a discrete probability distribution for a specified column.
        histogram(column_to_plot): Plot a histogram for a specified column.
        box_plot(column_to_plot): Plot a box plot for a specified column.
        qq_plot(column_to_plot): Plot a Q-Q plot for a specified column.
        kde_plot(column_to_plot): Plot a Kernel Density Estimate (KDE) plot for a specified column.
        compare_distributions(column_to_plot, original_df, transformed_df): Compare the distributions of a column before and after transformation.
        kde_hist_multi(columns_to_plot): Plot multiple KDE histograms for specified columns.
        correlation_heatmap(columns_to_plot, mask_upper=True, cmap='coolwarm'): Plot a correlation heatmap for specified columns.

    """
    def __init__(self, dataframe):
        self.df = dataframe
    
    def discrete_probability_distribution(self, column_to_plot):
        """
        Plot a discrete probability distribution for a specified column.

        Args:
            column_to_plot (str): Name of the column to be plotted.
        """
        plt.rc("axes.spines", top=False, right=False)
        probs = self.df[column_to_plot].value_counts(normalize=True)
        dpd=sns.barplot(y=probs.index, x=probs.values, color='b')
        plt.xlabel('Values')
        plt.ylabel('Probability')
        plt.title('Discrete Probability Distribution')
        plt.show()

    def histogram(self, column_to_plot):
        """
        Plot a histogram for a specified column.

        Args:
            column_to_plot (str): Name of the column to be plotted.
        """
        sns.histplot(data=self.df, x=column_to_plot, kde=True)
        sns.despine()
        plt.title('Histogram')
        plt.show()

    def box_plot(self, column_to_plot):
        """
        Plot a box plot for a specified column.

        Args:
            column_to_plot (str): Name of the column to be plotted.
        """
        sns.boxplot(x=self.df[column_to_plot])
        plt.title('Box Plot')
        plt.xlabel(column_to_plot)
        plt.show()

    def qq_plot(self, column_to_plot):
        """
        Plot a Q-Q plot for a specified column.

        Args:
            column_to_plot (str): Name of the column to be plotted.
        """
        qqplot(self.df[column_to_plot], line='s')
        plt.title('Q-Q Plot')
        plt.show()

    def kde_plot(self, column_to_plot):
        """
        Plot a Kernel Density Estimate (KDE) plot for a specified column.

        Args:
            column_to_plot (str): Name of the column to be plotted.
        """
        sns.kdeplot(data=self.df[column_to_plot], shade=True)
        plt.title('Kernel Density Estimate Plot')
        plt.xlabel(column_to_plot)
        plt.ylabel('Density')
        plt.show()

    def compare_distributions(self, column_to_plot, original_df, transformed_df):
        """
        Compare the distributions of a column before and after transformation.

        Args:
            column_to_plot (str): Name of the column to be compared.
            original_df (pd.DataFrame): Original DataFrame before transformation.
            transformed_df (pd.DataFrame): Transformed DataFrame after transformation.
        """
        plt.figure(figsize=(12, 6))
        
        plt.subplot(1, 2, 1)
        sns.histplot(data=original_df, x=column_to_plot, kde=True)
        plt.title(f'Distribution of {column_to_plot} (Before)')
        
        plt.subplot(1, 2, 2)
        sns.histplot(data=transformed_df, x=column_to_plot, kde=True)
        plt.title(f'Distribution of {column_to_plot} (After)')

        plt.tight_layout()
        plt.show()

    def kde_hist_multi(self, columns_to_plot):
        """
        Plot multiple KDE histograms for specified columns.

        Args:
            columns_to_plot (list): List of column names to be plotted.
        """
        sns.set(font_scale=0.7)
        f = pd.melt(self.df, value_vars=columns_to_plot)
        g = sns.FacetGrid(f, col="variable",  col_wrap=3, sharex=False, sharey=False)
        g = g.map(sns.histplot, "value", kde=True)

    def correlation_heatmap(self, columns_to_plot, mask_upper=True, cmap='coolwarm'):
        """
        Plot a correlation heatmap for specified columns.

        Args:
            columns_to_plot (list): List of column names to be included in the heatmap.
            mask_upper (bool): Whether to mask the upper triangle of the heatmap. Default is True.
            cmap (str): Colormap for the heatmap. Default is 'coolwarm'.
        """
        subset_df = self.df[columns_to_plot]

        correlation_matrix = subset_df.corr()

        if mask_upper:
            mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
        else:
            mask = None

        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, mask=mask, square=True, linewidths=.5, annot=True, cmap=cmap)
        plt.yticks(rotation=0)
        plt.title('Correlation Matrix of Specified Columns')
        plt.show()