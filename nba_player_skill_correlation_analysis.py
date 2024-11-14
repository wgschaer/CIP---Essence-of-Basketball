import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the player stats dataset
player_data = pd.read_csv("Mirco/data/nba_player_stats_cleaned.csv")

# Step 2: Select relevant numerical player metrics for correlation analysis
numeric_columns = ['pts', 'ast', 'reb', 'stl', 'blk', 'tov', 'fg%', '3p%', 'ft%', 'fp', 'dd2', 'td3', '+/-']

# Step 3: Compute the correlation matrix
correlation_matrix = player_data[numeric_columns].corr()

# Step 4: Visualize the correlation matrix using a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, linewidths=0.5)
plt.title("Correlation Matrix of NBA Player Metrics")
plt.tight_layout()
plt.show()
