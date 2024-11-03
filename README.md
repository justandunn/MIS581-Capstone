# MIS581-Capstone
CSU-Global MSDA Capstone
U.S. Federal Spending Analysis and Transparency Capstone Project
Author: Justan E. Dunn
Institution: Colorado State University Global
Course: MIS581-1: Capstone - Business Intelligence and Data Analytics
Date: October 2024

Project Overview
The rapid accumulation of U.S. national debt, surpassing $35.35 trillion in 2024, has raised significant concerns about fiscal management and transparency. This capstone project investigates the relationship between Omnibus spending bills and national debt growth, analyzing their impact on spending inefficiencies and exploring whether blockchain technology and big data could improve public oversight. The project combines federal data, statistical analysis, and data visualization to offer insights into potential accountability mechanisms for government spending.

Key Objectives
Analyze Federal Spending Patterns: Assess trends in spending and debt growth, with a focus on Omnibus and non-Omnibus years.
Evaluate Transparency Mechanisms: Explore how blockchain and big data could support civilian oversight and improve transparency in federal spending.
Test Hypotheses: Statistically examine the relationship between Omnibus bills and national debt growth through various hypothesis tests.

Data Sources
The datasets for this project come from:
Federal Reserve Economic Data (FRED): Provides Gross Federal Debt, Federal Government Expenditures, and Surplus/Deficit data. Available through the FRED API.
USAspending.gov: A comprehensive public database offering transaction-level details on U.S. government expenditures.

Hypotheses
Null Hypothesis (H0): There is no significant relationship between Omnibus bill usage and U.S. national debt growth.
Alternative Hypothesis (H1): Omnibus bill usage is associated with significant growth in the U.S. national debt.

Installation
Prerequisites
Python 3.7+
Jupyter Notebook
Required libraries: pandas, matplotlib, seaborn, scipy, statsmodels, and numpy
Installation Steps
Clone the repository:
git clone [https://github.com/YourUsername/U.S.-Federal-Spending-Analysis.git](https://github.com/justandunn/MIS581-Capstone.git)
Install dependencies:
pip install -r requirements.txt
Access the Jupyter Notebooks for full data analysis:
jupyter notebook

Repository Structure
/data: Contains datasets used in the analysis, including budget_appropriations_summary.csv.
/notebooks: Jupyter Notebooks for data processing, cleaning, and visualization.
/src: Python scripts for specific functions, such as data extraction from FRED and USAspending.gov, data cleaning, and statistical testing.
README.md: Project overview, objectives, and instructions.

Key Analyses
1. Statistical Testing
T-tests, Mann-Whitney U tests, ANOVA, and Kruskal-Wallis tests to analyze differences in budgetary allocations between Omnibus and non-Omnibus years.
Correlation analysis (Pearson and Spearman) to assess relationships among key budgetary measures, including total_budgetary_resources_amount, gross_outlay_amount_by_tas, and unobligated_balance.
2. Visualizations
Boxplots for budgetary distribution by Omnibus flag.
Heatmaps to illustrate correlations among budgetary metrics.
Time-series plots for historical trends, highlighting expenditure spikes during Omnibus years.

Results
The findings suggest a notable relationship between Omnibus bills and spending patterns, with Omnibus years often correlating with higher budgetary allocations and expenditure volatility. The project’s statistical analysis supports the need for increased oversight mechanisms, particularly through modern technologies like blockchain, to enhance fiscal accountability.

Ethical Considerations
The project addresses ethical and security considerations related to data privacy and transparency, especially in the context of blockchain for public sector financial data. The balance between transparency and data privacy is a central focus, aiming to enhance public trust in government spending practices.

Future Work
Further exploration could involve additional economic indicators, analysis of external influences (e.g., emergencies like the COVID-19 pandemic), and implementation of blockchain-based prototypes for public oversight.

Additional Resources
Final Paper:
Presentation:
GitHub Repository: [https://github.com/YourUsername/U.S.-Federal-Spending-Analysis.git](https://github.com/justandunn/MIS581-Capstone.git)
