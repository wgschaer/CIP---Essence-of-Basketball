# Essence of Basketball: CIP Project

This repository contains the project files for the CIP course project titled **"Essence of Basketball"**. The project
investigates the skills of basketball players and explores the factors driving team success using public NBA data from
the 2004-2024 seasons.

## Repository Structure

The repository is structured as follows:

```
CIP---Essence-of-Basketball/
├── Kenny/
│   ├── 01_nba_team_data_scraping.py
│   ├── 02_nba_team_data_cleaning.py
│   ├── 03_nba_team_mvp_merge_data.py
│   └── 04_nba_team_success_analysis.py
├── Mirco/
│   ├── 01_nba_player_data_scraping.py
│   ├── 02_nba_player_data_cleaning.py
│   ├── 03_mvp_position_merged_data.py
│   └── 04_mvp_analysis_research_question.py
├── Sabin/
│   ├── 01_nba_mvp_championship_scrapping.py
│   ├── 02_data_cleaning_mvp_championship.py
│   ├── 03_mvp_championship_findings.py
│   └── 04_mvp_skill_stats.py
├── .idea/
├── .gitignore
├── 05_nba_player_skill_correlation_analysis.py
├── LICENSE
├── README.md
└── requirements.txt
```

## Project Overview

This project aims to answer the following research questions:

1. **What are the essential skills of basketball players?**
2. **Which factors contribute to team success?**
3. **What is the relationship between MVP awards and team championships?**

## Scripts

### Kenny’s Folder

- **01_nba_team_data_scraping.py**: Scrapes NBA team data for the 2004-2024 seasons.
- **02_nba_team_data_cleaning.py**: Cleans and preprocesses the raw team data.
- **03_nba_team_mvp_merge_data.py**: Merges the cleaned team data with MVP information for analysis.
- **04_nba_team_success_analysis.py**: Analyzes factors that drive team success, including offensive and defensive
  ratings.

### Mirco’s Folder

- **01_nba_player_data_scraping.py**: Collects NBA player statistics from 2004 to 2024.
- **02_nba_player_data_cleaning.py**: Cleans the scraped player data, standardizing columns and handling missing values.
- **03_mvp_position_merged_data.py**: Merges player data with MVP positions to identify trends and patterns.
- **04_mvp_analysis_research_question.py**: Investigates research questions related to MVP trends and player impact.

### Sabin’s Folder

- **01_nba_mvp_championship_scrapping.py**: Scrapes MVP and championship data for the given seasons.
- **02_data_cleaning_mvp_championship.py**: Cleans and merges MVP data with championship results.
- **03_mvp_championship_findings.py**: Analyzes the relationship between MVP awards and team championships.
- **04_mvp_skill_stats.py**: Provides a detailed analysis of MVP skill statistics and their impact.

### Root-Level Script (Group Research Question)

- **05_nba_player_skill_correlation_analysis.py**: Analyzes individual player skills using statistical methods,
  including:
    - Exploratory Data Analysis (EDA).
    - Correlation analysis of metrics like points, assists, and rebounds.
    - Visualizations of top player skills and performance.

## Installation

To set up the project locally, clone the repository and install the dependencies listed in `requirements.txt`:

```bash
git clone https://github.com/wgschaer/CIP---Essence-of-Basketball.git
cd CIP---Essence-of-Basketball
pip install -r requirements.txt
```

Alternatively, you can install the required packages using Conda which we used for the project:

```bash
conda install -c conda-forge selenium beautifulsoup4 pandas unidecode matplotlib seaborn
```

## Usage

1. Run the scripts in each contributor’s folder in the following order:

Kenny’s ETL-process:

```bash
python Kenny/01_nba_team_data_scraping.py
python Kenny/02_nba_team_data_cleaning.py
python Kenny/03_nba_team_mvp_merge_data.py
python Kenny/04_nba_team_success_analysis.py
```

Mirco’s ETL-process:

```bash
python Mirco/01_nba_player_data_scraping.py
python Mirco/02_nba_player_data_cleaning.py
python Mirco/03_mvp_position_merged_data.py
python Mirco/04_mvp_analysis_research_question.py
```

Sabin’s ETL-process:

```bash
python Sabin/01_nba_mvp_championship_scrapping.py
python Sabin/02_data_cleaning_mvp_championship.py
python Sabin/03_mvp_championship_findings.py
python Sabin/04_mvp_skill_stats.py
```

Group Script on root-level (General Research Question):

```bash
python 05_nba_player_skill_correlation_analysis.py
```

## Results

Key findings from the analysis include:

- MVPs and Championships: MVPs often belong to championship-winning teams, highlighting their influence.
- Team Success Factors: Offensive and defensive ratings are strong indicators of overall team performance.
- Player Skills: Scoring, assists, and rebounding are the most significant individual skills impacting player
  performance.

## Conclusion

The project provides comprehensive insights into the skills and factors that define basketball success. Future analysis
could explore deeper player role categorization or predictive modeling for team performance.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributors

- Kenny: NBA Team data scraping, data cleaning, MVP status merging and team success with & without MVP analysis.
- Mirco: NBA Player data scraping, data cleaning, MVP position merging and MVP position trend analysis.
- Sabin: NBA MVP & Champions data scraping, data cleaning, MVP & Champions merging and MVP player analysis.