
import pandas as pd

# Load the data from CSV files
mvp_data = pd.read_csv("D:/MDS 2024/2nd Semester/CIP02 Data Collection, Integration and Preprocessing/CIP---Essence-of-Basketball/Sabin/data/nba_mvp_data_1999_2024.csv")
# "D:\MDS 2024\2nd Semester\CIP02 Data Collection, Integration and Preprocessing\CIP---Essence-of-Basketball\Sabin\nba_champions_1999_2024.csv"


champion_data = pd.read_csv("D:/MDS 2024/2nd Semester/CIP02 Data Collection, Integration and Preprocessing/CIP---Essence-of-Basketball/Sabin/data//nba_champions_1999_2024.csv")

# Display the first few rows of each DataFrame
print(mvp_data.head())
print(champion_data.head())
