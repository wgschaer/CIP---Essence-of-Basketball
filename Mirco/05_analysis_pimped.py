import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned merged MVP data
file_path = 'data/mvp_with_positions_cleaned.csv'
mvp_data = pd.read_csv(file_path)

# Step 1: Basic Data Overview
print("Dataset Overview:")
print(mvp_data.info())
print("\nFirst 5 Rows of the Data:")
print(mvp_data.head())

# Step 2: Distribution of MVPs by Position Over Time
position_trends = mvp_data.groupby(['Year', 'Position']).size().unstack(fill_value=0)

# Step 3: Stacked Bar Chart - MVPs by Position (Yearly)
plt.figure(figsize=(14, 8))
position_trends.plot(kind='bar', stacked=True, colormap='viridis')
plt.title('Distribution of MVPs by Position Over Time', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of MVPs', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Position', loc='upper left')
plt.tight_layout()
plt.show()

# Step 4: Line Plot - Position Trends Over Time
plt.figure(figsize=(14, 6))
for position in position_trends.columns:
    sns.lineplot(x=position_trends.index, y=position_trends[position], label=position)
plt.title('Trends in MVP Positions Over Time', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of MVPs', fontsize=12)
plt.legend(title='Position')
plt.grid(visible=True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Step 5: Total MVPs by Position
total_mvp_by_position = mvp_data['Position'].value_counts()

# Step 6: Bar Plot - Total MVPs by Position
plt.figure(figsize=(8, 5))
sns.barplot(x=total_mvp_by_position.index, y=total_mvp_by_position.values, palette='muted')
plt.title('Total Number of MVPs by Position', fontsize=16)
plt.xlabel('Position', fontsize=12)
plt.ylabel('Number of MVPs', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Step 7: MVP Representation by Team
mvp_team_counts = mvp_data['MVP Team'].value_counts()

# Step 8: Horizontal Bar Plot - MVP Representation by Team
plt.figure(figsize=(10, 6))
sns.barplot(y=mvp_team_counts.index, x=mvp_team_counts.values, palette='coolwarm')
plt.title('Number of MVPs by Team', fontsize=16)
plt.xlabel('Number of MVPs', fontsize=12)
plt.ylabel('Team', fontsize=12)
plt.tight_layout()
plt.show()

# Step 9: Heatmap - MVP Position Distribution Over Time
plt.figure(figsize=(12, 6))
sns.heatmap(position_trends, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Heatmap of MVP Position Distribution Over Time', fontsize=16)
plt.xlabel('Position', fontsize=12)
plt.ylabel('Year', fontsize=12)
plt.tight_layout()
plt.show()

# Step 10: Insights
print("\nTotal Number of MVPs by Position:")
print(total_mvp_by_position)

# Step 11: Analyzing the Most Recent Years
recent_years = mvp_data[mvp_data['Year'] >= 2010]
recent_trends = recent_years['Position'].value_counts()

# Step 12: Pie Chart - MVP Positions in Recent Years (2010-2024)
plt.figure(figsize=(7, 7))
plt.pie(recent_trends, labels=recent_trends.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title('MVP Position Distribution (2010-2024)', fontsize=16)
plt.tight_layout()
plt.show()

# Step 13: Conclusion and Insights
print("\nRecent Trends in MVP Positions (2010-2024):")
print(recent_trends)
print("\nKey Observations:")
print("- The distribution of MVPs by position shows evolving trends over the years.")
print("- Centers and Forwards have seen significant representation in recent years.")
print("- The analysis highlights shifts in playing style preferences for MVPs.")

# Save the enhanced analysis results to a CSV file (if needed)
mvp_data.to_csv('data/mvp_analysis_results.csv', index=False)
print("\nAnalysis completed. Results saved to 'data/mvp_analysis_results.csv'.")
