# Import the necessary libraries
import pandas as pd

# Load the cleaned dataset
df = pd.read_csv('data/cleaned_nba_data_mvp_with_teams.csv')

# Step 1: Add a column to check if the MVP's team also won the championship
df['MVP_Champion'] = df['MVP Team'] == df['Champion Team']

# Step 2: Calculate the number and percentage of times an MVP also won the championship
mvp_championship_count = df['MVP_Champion'].sum()
total_years = df.shape[0]

# Display the result
print(f"\nThe MVP also won the Championship in the same season: {mvp_championship_count} times out of {total_years}"
      f" seasons.")
print(f"Percentage of MVPs winning the Championship in the same season: {mvp_championship_count / total_years:.2%}\n")

# Step 3: Identify the player with the most MVPs in the dataset
most_mvp_player = df['Season MVP'].value_counts().idxmax()
most_mvp_count = df['Season MVP'].value_counts().max()
print(f"Player with the most MVPs in the last 20 years: {most_mvp_player} ({most_mvp_count} MVPs)")

# Step 4: Find the youngest and oldest MVPs
youngest_mvp = df.loc[df['Age'].idxmin()]
oldest_mvp = df.loc[df['Age'].idxmax()]
print(f"Youngest MVP in the last 20 years: {youngest_mvp['Season MVP']} ({youngest_mvp['Age']} years)")
print(f"Oldest MVP in the last 20 years: {oldest_mvp['Season MVP']} ({oldest_mvp['Age']} years)\n")

# Step 5: Identify the team with the most MVPs
most_mvp_team = df['MVP Team'].value_counts().idxmax()
most_mvp_team_count = df['MVP Team'].value_counts().max()
print(f"Team with the most MVPs in the last 20 years: {most_mvp_team} ({most_mvp_team_count} MVPs)")

# Step 6: Identify the team with the most championships
most_champion_team = df['Champion Team'].value_counts().idxmax()
most_champion_team_count = df['Champion Team'].value_counts().max()
print(f"Team with the most Championships in the last 20 years: {most_champion_team} ({most_champion_team_count} "
      f"Championships)")

# Step 7: Summary of Insights
summary = f"""
Key Insights:
1. The MVP also won the Championship {mvp_championship_count} out of {total_years} times ({mvp_championship_count / total_years:.2%}).
2. {most_mvp_player} has won the most MVP awards ({most_mvp_count}), showcasing consistent excellence.
3. The youngest MVP was {youngest_mvp['Season MVP']} at {youngest_mvp['Age']} years old.
4. The oldest MVP was {oldest_mvp['Season MVP']} at {oldest_mvp['Age']} years old.
5. The team with the most MVPs is {most_mvp_team} with {most_mvp_team_count} MVPs.
6. The team with the most Championships is {most_champion_team} with {most_champion_team_count} Championships.
"""

print("\n" + summary)
