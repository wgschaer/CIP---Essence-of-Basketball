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
plt.figure(figsize=(8, 5))
total_mvp_by_position.plot(kind='bar', color='skyblue')
plt.title('Total Number of MVPs by Position')
plt.xlabel('Position')
plt.ylabel('Number of MVPs')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Step 5: Output summary statistics
print("Total Number of MVPs by Position:")
print(total_mvp_by_position)
