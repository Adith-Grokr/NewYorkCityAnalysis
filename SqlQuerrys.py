import pandas as pd
import psycopg2

# Connect to your database
conn = psycopg2.connect(
    host="your_host",
    database="your_database",
    user="your_username",
    password="your_password"
)

# Function to execute SQL and return results in a DataFrame
def run_query(query):
    return pd.read_sql(query, conn)
SQL Queries
Use the run_query function to execute each query in the notebook cells and display the result.

Query 1: Most Common Complaint Types and Frequencies by Borough

query1 = """
SELECT 
    borough,
    complaint_type,
    COUNT(*) AS complaint_count
FROM 
    nypd_complaints
GROUP BY 
    borough, complaint_type
ORDER BY 
    complaint_count DESC;
"""

# Execute and display results
run_query(query1)
Query 2: Average Response Time by Complaint Type and Borough

query2 = """
SELECT 
    c.complaint_type,
    c.borough,
    AVG(rt.response_time) AS avg_response_time
FROM 
    nypd_complaints c
JOIN 
    response_times rt ON c.complaint_id = rt.incident_id
WHERE 
    rt.agency IN ('FDNY', 'NYPD')
GROUP BY 
    c.complaint_type, c.borough
ORDER BY 
    avg_response_time ASC;
"""

# Execute and display results
run_query(query2)
Query 3: Complaints That Resulted in Arrests by Borough and Complaint Type

query3 = """
SELECT 
    c.borough,
    c.complaint_type,
    COUNT(a.arrest_id) AS arrest_count
FROM 
    nypd_complaints c
LEFT JOIN 
    nypd_arrests a ON c.complaint_id = a.complaint_id
GROUP BY 
    c.borough, c.complaint_type
ORDER BY 
    arrest_count DESC;
"""

# Execute and display results
run_query(query3)
Query 4: Monthly Trend of Complaints and Arrests for the Current Year

query4 = """
SELECT 
    DATE_TRUNC('month', c.incident_date) AS month,
    COUNT(DISTINCT c.complaint_id) AS monthly_complaints,
    COUNT(DISTINCT a.arrest_id) AS monthly_arrests
FROM 
    nypd_complaints c
LEFT JOIN 
    nypd_arrests a ON c.complaint_id = a.complaint_id
WHERE 
    EXTRACT(YEAR FROM c.incident_date) = 2024
GROUP BY 
    month
ORDER BY 
    month;
"""

# Execute and display results
run_query(query4)
Query 5: Comparison of Response Times for Arrested vs. Non-Arrested Incidents by Borough

query5 = """
SELECT 
    c.borough,
    CASE 
        WHEN a.arrest_id IS NOT NULL THEN 'Arrest'
        ELSE 'No Arrest'
    END AS arrest_status,
    AVG(rt.response_time) AS avg_response_time
FROM 
    nypd_complaints c
LEFT JOIN 
    response_times rt ON c.complaint_id = rt.incident_id
LEFT JOIN 
    nypd_arrests a ON c.complaint_id = a.complaint_id
GROUP BY 
    c.borough, arrest_status
ORDER BY 
    c.borough, avg_response_time;
"""

# Execute and display results
run_query(query5)