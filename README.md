# NYC Open Data Analysis Project

## Project Overview

This project is designed to empower data exploration, analysis, and insights extraction from real-world data related to New York City. The primary objective is to analyze NYC's data, focusing on areas like public safety, emergency response times, and public service requests. Through this project, we utilize a range of data science and collaborative tools, including SQL, Python, and Git version control.

Our analysis leverages three datasets from NYC Open Data:
- **NYPD Complaint Data**: Information on reported incidents and complaints, allowing for insights into crime trends and public safety concerns.
- **FDNY and NYPD Response Times**: Data on emergency response times, highlighting the effectiveness and speed of emergency services across boroughs.
- **NYPD Arrest Data__Year-to-Date__20241112:** Records of arrests made by the NYPD year-to-date (as of November 12, 2024) provide insights into crime patterns and enforcement activities. Analyzing arrest data alongside reported incidents can offer a more comprehensive view of criminal activity.

### Project Objectives

1. **Analyze Crime Trends**: Identify patterns in reported incidents, including high-frequency crime categories and neighborhoods with elevated complaint rates.
2. **Evaluate Emergency Response Times**: Assess average response times across boroughs and incident types to determine where improvements could be made.
3. **Exploration of Arrest Trends:** Analyzing trends in arrests by crime type, location, and time of day (using arrest data) can provide valuable insights into patterns of criminal activity. This information can be used to inform targeted policing strategies and resource allocation.


### Data Sources
The datasets used in this project were sourced from [NYC Open Data](https://opendata.cityofnewyork.us/):
1. **NYPD Complaint Data**
2. **FDNY and NYPD Response Times**
3. **NYPD Arrest Data__Year-to-Date__20241112s**

## Project Structure

- **Data Exploration and Cleaning**: Using Python (pandas), we performed data cleaning, including handling missing values, outliers, and inconsistencies.
- **SQL Queries**: We used SQL to retrieve, filter, aggregate, and join data from the datasets, streamlining data retrieval for analysis.
- **Data Analysis and Visualization**: Python libraries like `pandas`, `matplotlib`, and `seaborn` were used to conduct analysis and create visualizations to communicate findings.
- **Collaborative Development**: The project was developed collaboratively, with Git used for version control, including branching strategies, merge practices, and conflict resolution.

## Getting Started

### Prerequisites

- **Python 3.x**: Required for data analysis and visualization.
- **Jupyter Notebook** (recommended) or another IDE: For interactive data exploration and visualization.
- **Git**: For version control and collaboration.
- **SQL Database**: Ensure you have access to a SQL-compatible database (e.g., PostgreSQL, MySQL) to run SQL queries against the datasets.

### Installation

1. Clone the repository:
   git clone https://github.com/yourusername/nyc-data-analysis.git
   cd nyc-data-analysis

### Install required Python libraries:
```
  pip install pandas matplotlib seaborn sqlalchemy
```
### Project Components

## Data Exploration and Cleaning
Data was imported and cleaned in Python using pandas:

**Handling Missing Values:** Imputed or removed rows/columns with missing values as appropriate.
**Removing Outliers:** Identified and removed outliers based on statistical metrics.
**Standardizing Data:** Converted categorical fields and standardized date/time formats for consistency.

### SQL Queries
## We used SQL to:

- **Extract and aggregate data from each dataset.**
- **Perform joins between datasets for combined analysis.**
- **Filter data based on specific conditions (e.g., date ranges, incident types).**
  
## Examples of SQL queries used:
```
-- Query to get average response time by borough
SELECT borough, AVG(response_time) AS avg_response_time
FROM response_times
GROUP BY borough;

-- Query to retrieve top crime types in NYPD Complaint Data
SELECT offense, COUNT(*) AS count
FROM nypd_complaint_data
GROUP BY offense
ORDER BY count DESC
LIMIT 10;
```
### Python Analysis and Visualizations
## Using Python libraries (pandas, matplotlib, seaborn), we created visualizations to uncover insights:

- **Bar Charts:** Crime frequency by category and borough.
- **Line Charts:** Monthly trends in response times and incident volumes.
- **Heat Maps:** Geographic distribution of 311 Service Requests.
## Key Findings
- **Crime Patterns:** Certain neighborhoods had higher crime rates, with specific categories of crime more prevalent in those areas.
- **Emergency Response Times:** Boroughs with high incident volumes experienced slower response times, suggesting areas where resources could be optimized.
- **311 Service Requests:** Issues varied significantly by borough, with common requests related to noise complaints, illegal parking, and housing quality.

### Collaborative Development

## This project was developed in collaboration with team members using Git:

- **Branching:** Each team member created their own feature branches for independent work.
- **Merging:** Changes were merged through pull requests, reviewed by team members before final integration.
- **Conflict Resolution:** Conflicts were resolved through Git's merge conflict resolution features, fostering a smooth collaborative experience.
- 
### Challenges and Solutions

- **Data Quality Issues:** Some datasets contained missing or inconsistent data. Solution: We used imputation strategies and statistical methods to handle missing values and outliers.
- **Collaborative Difficulties:** Version control conflicts arose during branch merges. Solution: We improved branch management by enforcing regular merging and thorough code reviews.

### Future Directions

- **Expanded Analysis:** Future work could integrate additional datasets (e.g., transportation data) to provide a broader context to the analysis.
- **Automated Data Pipeline:** An automated data pipeline could be implemented to pull updated data regularly and update analysis findings.
Results and Visualizations

### Please see the notebooks/ directory for detailed analysis and visualizations. Each visualization is accompanied by an explanation to help interpret the findings.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
 
### References
##Data Sources
- **NYPD Complaint Data:** NYC Open Data provides information on complaints made to the NYPD, detailing incidents by location, date, complaint type, and borough.
- **NYC Open Data Portal** - https://opendata.cityofnewyork.us/
- **FDNY and NYPD Response Times:** These datasets contain details on response times to incidents, categorized by agency and borough, and are available through NYC’s public data resources.
- **NYPD Arrest Data:** This dataset includes information about arrests made by NYPD, capturing arrest dates, related complaint IDs, and descriptions.
- **NYC Data Portal Documentation:** Official documentation to understand dataset attributes and guidelines.
https://data.cityofnewyork.us/
### SQL for Data Analysis and Manipulation
- **PostgreSQL Documentation:** Comprehensive reference for SQL syntax and advanced functions used in PostgreSQL, useful for understanding SQL commands.
- **PostgreSQL Official Docs -** https://www.postgresql.org/docs/
- **SQL Joins and Aggregations:** Tutorial resources explaining SQL joins, aggregations, grouping, and filtering, specifically focused on multi-table analysis.
- **SQL Tutorial - W3Schools** - https://www.w3schools.com/sql/
- **SQL for Data Analysis - Mode Analytics SQL Tutorial** - https://mode.com/sql-tutorial/
- **Data Analysis and Visualization** in Jupyter Notebooks
- **Pandas Documentation:** Pandas library documentation, which is helpful for handling SQL query results, data manipulation, and basic visualizations within a Jupyter Notebook.
- **Pandas Docs** - https://pandas.pydata.org/pandas-docs/stable/
- **Matplotlib and Seaborn:** These libraries are commonly used for visualizations in Python and are helpful for graphically representing SQL query results.
- **Matplotlib **- https://matplotlib.org/stable/contents.html
- **Seaborn **- https://seaborn.pydata.org/

