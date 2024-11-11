import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
merged_df = pd.read_csv('data/cleaned_nba_data_mvp_with_teams.csv')

# Set up the plotting style
sns.set(style="whitegrid")

# Create a bar plot to visualize TRB, AST, STL, BLK for each MVP with player names
metrics = ['PTS','TRB', 'AST', 'STL', 'BLK']
plt.figure(figsize=(14, 12))

# Add player names to the x-axis
merged_df['Label'] = merged_df['Year'].astype(str) + " - " + merged_df['Season MVP']

# Loop through each metric and plot with player names
for i, metric in enumerate(metrics):
    plt.subplot(3, 2, i + 1)
    sns.barplot(x='Label', y=metric, data=merged_df, palette='viridis')
    plt.xticks(rotation=45, ha='right')
    plt.title(f'{metric} by MVP (Player)')
    plt.xlabel('Year - Season MVP')
    plt.ylabel(metric)

plt.tight_layout()
plt.show()


# Step 3: Check if Season MVP's team is also the Champion Team
merged_df['Season MVP'] = merged_df['MVP Team'] == merged_df['Champion Team']


# Count how many times the MVP was also the champion
mvp_championship_count = merged_df['MVP_Champion'].sum()
total_years = merged_df.shape[0]

print(f"\nThe MVP also won the Championship in the same season {mvp_championship_count} times out of {total_years} seasons.")

# Visualize the correlation
import seaborn as sns

plt.figure(figsize=(6, 4))
sns.countplot(x='MVP_Champion', data=merged_df)
plt.title('MVP Winning Championship in the Same Season')
plt.xlabel('MVP Won Championship')
plt.ylabel('Count')
plt.xticks([0, 1], ['No', 'Yes'])
plt.show()
