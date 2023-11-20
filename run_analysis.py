import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from scipy import stats
from scipy.stats import mannwhitneyu

# Perform normality test on a given column using the Shapiro-Wilk test
def perform_normality_test(column):
    # Removing NaN values to ensure accurate test results
    cleaned_data = df[column].dropna()
    # Conducting the Shapiro-Wilk test
    stat, p_val = stats.shapiro(cleaned_data)
    return stat, p_val

# Perform either t-test or Mann-Whitney U test based on data normality
def perform_statistical_test(column, is_normal):
    if is_normal:
        # Performing a t-test for normally distributed data
        t_stat, p_val = stats.ttest_ind(df[df['pcg'] == True][column], df[df['pcg'] == False][column])
        test_type = 't-test'
    else:
        # Performing a Mann-Whitney U test for non-normally distributed data
        u_stat, p_val = mannwhitneyu(df[df['pcg'] == True][column], df[df['pcg'] == False][column])
        t_stat = u_stat  # Using u_stat as the test statistic
        test_type = 'Mann-Whitney U test'
    return t_stat, p_val, test_type

# Plot and save a bar chart for the given data column
def plot_bar_chart(column, stat_values, test_stat, p_val, test_type, title, ylabel, fig_name):
    # Choosing label based on test type
    stat_label = 'Median' if 'Mann-Whitney' in test_type else 'Average'
    # Displaying test findings in the console
    print(f"{title}\n{stat_label} for PCG: {stat_values[stat_values['pcg'] == True][column].values[0]:.2f}, "
          f"{stat_label} for non-PCG: {stat_values[stat_values['pcg'] == False][column].values[0]:.2f}, "
          f"{test_type}: {test_stat:.5f}, P-val: {p_val:.5f} ({'Statistically significant' if p_val < 0.05 else 'Not statistically significant'})\n")
    # Creating and configuring the bar plot
    plt.figure(figsize=(8, 6))
    sns.barplot(x='pcg', y=column, data=stat_values)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel('Uses PCG')
    plt.text(0.5, max(stat_values[column]), f'{test_type} Stat: {test_stat:.5f}, P-val: {p_val:.5f}', 
             horizontalalignment='center', color='black', weight='semibold')
    plt.tight_layout()
    # Saving the figure
    plt.savefig(fig_name)
    plt.close()

# Plot and save a histogram for the given data column
def plot_histogram(column, hue, title, xlabel, ylabel, fig_name):
    # Creating and configuring the histogram
    plt.figure(figsize=(12, 6))
    sns.histplot(df, x=column, hue=hue, kde=True, element="step")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # Saving the figure before closing
    plt.savefig(fig_name)
    plt.close()

# Set up argument parser for command line options
parser = argparse.ArgumentParser(description='Process data including or excluding generated data.')
parser.add_argument('--include_generated', type=bool, default=False, help='Include generated data if True, exclude if False')
args = parser.parse_args()

# Load and preprocess the dataset
df = pd.read_csv('game_data.csv')
# Conditional logic for handling generated data
if not args.include_generated:
    df.drop(['performance', 'innovation'], axis=1, inplace=True)
    metrics = ['avg_dev_time', 'budget', 'user_satisfaction', 'profit']
else:
    metrics = ['avg_dev_time', 'budget', 'profit', 'performance', 'innovation', 'user_satisfaction']

# Cleaning data: removing commas and converting to float for specific columns
columns_with_commas = ['budget', 'revenue', 'profit']
for column in columns_with_commas:
    df[column] = df[column].str.replace(',', '').astype(float)

# Creating directories for saving plots if they don't exist
histogram_dir = 'results/distributions'
bar_chart_dir = 'results'

os.makedirs(histogram_dir, exist_ok=True)
os.makedirs(bar_chart_dir, exist_ok=True)

# Looping through metrics to plot histograms and visualize data distribution
for metric in metrics:
    plot_histogram(metric, 'pcg', f'Distribution of {metric.replace("_", " ").title()} by PCG Status', 
                   metric.replace("_", " ").title(), 'Frequency', f'results/distributions/{metric}.png')

# Conducting statistical analysis and plotting bar charts for each metric
print("\nStatistics")
for i in range(100):
    print("-", end="")
print("\n")

for metric in metrics:
    # Performing normality test
    stat, p_val = perform_normality_test(metric)
    is_normal = p_val >= 0.05

    # Deciding on mean or median based on normality
    stat_values = df.groupby('pcg')[metric].mean().reset_index() if is_normal else df.groupby('pcg')[metric].median().reset_index()
    
    # Performing the appropriate statistical test
    test_stat, test_p_val, test_type = perform_statistical_test(metric, is_normal)

    # Displaying results and plotting the bar chart
    plot_bar_chart(metric, stat_values, test_stat, test_p_val, test_type, f'Bar Chart for {metric}', 'Value', f'results/{metric}_bar_chart.png')
