# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned merged MVP data
file_path = 'data/mvp_with_positions_cleaned.csv'
mvp_data = pd.read_csv(file_path)

# Step 1: Count the number of MVPs by position for each year
position_trends = mvp_data.groupby(['Year', 'Position']).size().unstack(fill_value=0)

# Step 2: Plot the trends
plt.figure(figsize=(12, 6))
position_trends.plot(kind='bar', stacked=True, figsize=(14, 7))
plt.title('Distribution of MVPs by Position (Yearly)')
plt.xlabel('Year')
plt.ylabel('Number of MVPs')
plt.xticks(rotation=45)
plt.legend(title='Position')
plt.tight_layout()
plt.show()

# Step 3: Calculate the total MVPs by position
total_mvp_by_position = mvp_data['Position'].value_counts()

# Step 4: Plot the total distribution of MVPs by position

# Define custom colors for the bar plot
color_map = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Blue, Orange, Green

plt.figure(figsize=(10, 6))
bars = plt.bar(
    total_mvp_by_position.index,
    total_mvp_by_position.values,
    color=color_map[:len(total_mvp_by_position)],  # Use distinct colors
    edgecolor='black'
)
plt.title('Total Number of MVPs by Position', fontsize=16)
plt.xlabel('Position', fontsize=14)
plt.ylabel('Number of MVPs', fontsize=14)
plt.xticks(rotation=0, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Annotate bar plot with values
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, int(yval), ha='center', va='bottom', fontsize=12)

plt.tight_layout()
plt.show()

# Step 5: Output summary statistics
print("Total Number of MVPs by Position:")
print(total_mvp_by_position)
