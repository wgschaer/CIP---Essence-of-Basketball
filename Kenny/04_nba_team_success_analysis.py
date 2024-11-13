# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the merged dataset
file_path = "data/merged_nba_data_with_mvp_status.csv"
merged_data = pd.read_csv(file_path)

# Step 1: Check the structure of the dataset
print("Columns in the dataset:", merged_data.columns)
print("Sample data:")
print(merged_data.head())

# Step 2: Identify key team-level statistics for analysis
team_stats_columns = ['offrtg', 'defrtg', 'netrtg', 'ast%', 'ast/to', 'oreb%', 'dreb%', 'tov%', 'efg%', 'ts%', 'pace']

# Step 3: Calculate the average performance of MVP teams vs. non-MVP teams
mvp_teams = merged_data[merged_data['is_mvp_team']]
non_mvp_teams = merged_data[~merged_data['is_mvp_team']]

mvp_avg_stats = mvp_teams[team_stats_columns].mean()
non_mvp_avg_stats = non_mvp_teams[team_stats_columns].mean()

# Combine the results into a DataFrame
performance_comparison = pd.DataFrame({
    'MVP Teams': mvp_avg_stats,
    'Non-MVP Teams': non_mvp_avg_stats
})

# Step 4: Visualize the comparison of MVP vs. Non-MVP teams
plt.figure(figsize=(12, 8))
performance_comparison.plot(kind='bar', figsize=(14, 7))
plt.title('Comparison of Team Performance: MVP Teams vs. Non-MVP Teams')
plt.ylabel('Average Value')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.legend()
plt.tight_layout()
plt.show()

# Step 5: Analyze correlations of team stats with MVP status
merged_data['is_mvp_team_numeric'] = merged_data['is_mvp_team'].astype(int)
correlation_matrix = merged_data[team_stats_columns + ['is_mvp_team_numeric']].corr()

# Step 6: Visualize the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation of Team Statistics with MVP Status')
plt.show()

# Step 7: Identify the strongest correlations
strong_correlations = correlation_matrix['is_mvp_team_numeric'].sort_values(ascending=False)
print("Strongest correlations with MVP status:")
print(strong_correlations)
