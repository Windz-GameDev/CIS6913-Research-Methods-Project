import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the dataset
df = pd.read_csv('game_data.csv')

# Function to perform t-test and return the statistic and p-value
def perform_t_test(column):
    t_stat, p_val = stats.ttest_ind(df[df['pcg'] == True][column], df[df['pcg'] == False][column])
    return t_stat, p_val

# Function to plot bar chart with t-test results and save the figure
def plot_bar_chart(column, title, ylabel, fig_name):
    # Calculate average values
    avg_values = df.groupby('pcg')[column].mean().reset_index()

    # Perform t-test
    t_stat, p_val = perform_t_test(column)

    # Print findings to console
    print(f"{title}\nAverage for PCG: {avg_values[avg_values['pcg'] == True][column].values[0]:.2f}, "
          f"Average for non-PCG: {avg_values[avg_values['pcg'] == False][column].values[0]:.2f}, "
          f"T-stat: {t_stat:.2f}, P-val: {p_val:.2e}")

    # Plotting
    plt.figure(figsize=(8, 6))
    sns.barplot(x='pcg', y=column, data=avg_values)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel('Uses PCG')
    plt.text(0.5, max(avg_values[column]), f'T-stat: {t_stat:.2f}\nP-val: {p_val:.2e}', 
             horizontalalignment='center', color='black', weight='semibold')
    plt.tight_layout()
    plt.savefig(fig_name)
    plt.close()

# Plotting and saving each bar chart
plot_bar_chart('dev_time', 'Average Development Time by PCG Usage', 'Average Time (months)', 'results/avg_dev_time.png')
plot_bar_chart('cost', 'Average Development Cost by PCG Usage', 'Average Cost (USD)', 'results/avg_dev_cost.png')
plot_bar_chart('performance', 'Average Game Performance by PCG Usage', 'Performance Rating', 'results/avg_performance.png')
plot_bar_chart('innovation', 'Average Innovation Score by PCG Usage', 'Innovation Rating', 'results/avg_innovation.png')
plot_bar_chart('user_satisfaction', 'Average User Satisfaction by PCG Usage', 'Satisfaction Rating', 'results/avg_user_satisfaction.png')
