import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from statsmodels.graphics.gofplots import qqplot

class Plotter:
    def __init__(self, dataframe):
        self.df = dataframe
    
    def discrete_probability_distribution(self, column_to_plot):
        plt.rc("axes.spines", top=False, right=False)
        probs = self.df[column_to_plot].value_counts(normalize=True)
        dpd=sns.barplot(y=probs.index, x=probs.values, color='b')
        plt.xlabel('Values')
        plt.ylabel('Probability')
        plt.title('Discrete Probability Distribution')
        plt.show()

    def histogram(self, column_to_plot):
        sns.histplot(data=self.df, x=column_to_plot, kde=True)
        sns.despine()
        plt.title('Histogram')
        plt.show()

    def box_plot(self, column_to_plot):
        sns.boxplot(x=self.df[column_to_plot])
        plt.title('Box Plot')
        plt.xlabel(column_to_plot)
        plt.show()

    def qq_plot(self, column_to_plot):
        qqplot(self.df[column_to_plot], line='s')
        plt.title('Q-Q Plot')
        plt.show()

    def kde_plot(self, column_to_plot):
        sns.kdeplot(data=self.df[column_to_plot], shade=True)
        plt.title('Kernel Density Estimate Plot')
        plt.xlabel(column_to_plot)
        plt.ylabel('Density')
        plt.show()

    def compare_distributions(self, column_to_plot, original_df, transformed_df):
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
        sns.set(font_scale=0.7)
        f = pd.melt(self.df, value_vars=columns_to_plot)
        g = sns.FacetGrid(f, col="variable",  col_wrap=3, sharex=False, sharey=False)
        g = g.map(sns.histplot, "value", kde=True)

    def correlation_heatmap(self, columns_to_plot, mask_upper=True, cmap='coolwarm'):
        # Extract the specified columns
        subset_df = self.df[columns_to_plot]

        # Compute the correlation matrix for the subset of columns
        correlation_matrix = subset_df.corr()

        # Create a mask to hide the upper triangle of the correlation matrix
        if mask_upper:
            mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
        else:
            mask = None

        # Draw the heatmap
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, mask=mask, square=True, linewidths=.5, annot=True, cmap=cmap)
        plt.yticks(rotation=0)
        plt.title('Correlation Matrix of Specified Columns')
        plt.show()