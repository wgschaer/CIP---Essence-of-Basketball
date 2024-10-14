###Overview

This repository contains the core work for our CIP (Data Collection, Integration and Processing) - project focused on the Essence of Basketball. We investigate the fundamental performance metrics that drive success in basketball, specifically exploring what defines an MVP (Most Valuable Player) and how this correlates with team success.
The project is divided into three main research questions:
MVP Performance Metrics: What are the common performance metrics of MVPs over the past 20 years?
Team Performance and MVPs: How do MVP teams perform compared to non-MVP teams, and which team-level statistics correlate most strongly with having an MVP on the roster?
Positional Trends Among MVPs: Have MVPs tended to be more guards, forwards, or centers in recent years?

###Project Structure

Sabin/
Contains the data and analysis related to Statistical Profiles, focusing on identifying common performance metrics for MVPs over the past 20 years.
Kenny/
Contains the code and analysis for Team Success, which compares MVP teams’ performance to non-MVP teams and explores which team-level statistics are strongly associated with having an MVP on the roster.
Mirco/
Contains the analysis related to Playing Style Trends, focusing on whether MVPs have tended to be more guards, forwards, or centers in recent years.

###Data Sources

We have scraped and utilized data from several official basketball sources, including:
NBA Official Website
Basketball Reference
ESPN NBA

###Methods & Tools

Our analysis leverages multiple machine learning techniques to derive insights from the data, including:
Linear Models
Generalized Linear Models (Poisson and Binomial families)
Generalized Additive Models
Neural Networks
Support Vector Machines
Additionally, generative AI models were used to enhance our data preparation and exploratory analysis.

###Setup

To replicate the environment and analysis:
Clone the repository.
Install the required Python packages listed in requirements.txt.
Run the analysis scripts within the Kenny and Mirco directories, depending on the area of interest.
Contributing

We welcome contributions to further extend the analysis or provide additional insights into basketball analytics. Please follow the repository’s guidelines for contributing.