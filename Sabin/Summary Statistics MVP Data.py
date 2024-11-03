# Let's calculate summary statistics without using ace_tools so that the output is visible directly.
import pandas as pd

# Load the dataset provided
file_path ="D:/MDS 2024/2nd Semester/CIP02 Data Collection, Integration and Preprocessing/CIP---Essence-of-Basketball/Sabin/nba_mvp_data_1999_2023.csv"
mvp_data = pd.read_csv(file_path)

# Let's calculate summary statistics for key columns
summary_stats = mvp_data[['PTS', 'TRB', 'AST', 'STL', 'BLK', 'FG%', 'FT%', 'WS']].describe()
print(summary_stats)
