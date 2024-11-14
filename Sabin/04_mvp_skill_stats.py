# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
merged_df = pd.read_csv('data/cleaned_nba_data_mvp_with_teams.csv')

# Set up the plotting style
sns.set(style="whitegrid")

# Define the metrics and their full names for the chart titles
metrics = {
    'PTS': 'Points',
    'TRB': 'Total Rebounds',
    'AST': 'Assists',
    'STL': 'Steals',
    'BLK': 'Blocks'
}

# Define a color palette for the different metrics
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2']

# Create a figure
plt.figure(figsize=(14, 12))

# Add player names to the x-axis
merged_df['Label'] = merged_df['Year'].astype(str) + " - " + merged_df['Season MVP']

# Loop through each metric and plot with player names
for i, (metric, color) in enumerate(zip(metrics.keys(), colors)):
    plt.subplot(3, 2, i + 1)
    sns.barplot(x='Label', y=metric, data=merged_df, color=color)
    plt.xticks(rotation=45, ha='right')
    plt.title(f'{metrics[metric]} by MVP', fontsize=14)
    plt.xlabel('Year - Season MVP')
    plt.ylabel(metrics[metric])
    plt.grid(axis='y')

# Add an overall bold title
plt.suptitle('MVP Skills Set', fontsize=18, fontweight='bold', y=1.05)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()
