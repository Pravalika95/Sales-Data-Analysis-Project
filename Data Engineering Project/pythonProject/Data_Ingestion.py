import pandas as pd
import mysql.connector

# Establish MySQL connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="samsara_analytics_db"
)

# Function to insert data into Opportunity table
def insert_into_opportunity(opportunity_data):
    cursor = mydb.cursor()
    insert_query = """
        INSERT INTO Opportunity (
            Opportunity_Type,
            Opportunity_Owner_ID,
            Opportunity_Created_Date,
            Opportunity_Close_Date,
            Stage,
            Probability,
            ACV_Bookings,
            Industry,
            Sub_Region,
            Region,
            Segment
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.executemany(insert_query, opportunity_data)
    mydb.commit()
    cursor.close()

# Function to insert data into Quota table
def insert_into_quota(quota_data):
    cursor = mydb.cursor()
    insert_query = """
        INSERT INTO Quota (
            Quota_Period_Start_Date, 
            Quota_Period_End_Date, 
            Quota_Period, 
            Quota_Region, 
            Quota_Sub_Region, 
            Quota_Segment, 
            Quota_Owner_ID, 
            Quota_Owner_Name, 
            Quota_Period_Timeframe, 
            q1_quota, 
            q2_quota, 
            q3_quota, 
            q4_quota
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.executemany(insert_query, quota_data)
    mydb.commit()
    cursor.close()

# Function to insert data into Fiscal_Calendar table
def insert_into_fiscal_calendar(fiscal_calendar_data):
    cursor = mydb.cursor()
    insert_query = """
        INSERT INTO Fiscal_Calendar (Date, Fiscal_Year, Fiscal_Quarter) 
        VALUES (%s, %s, %s)
    """
    cursor.executemany(insert_query, fiscal_calendar_data)
    mydb.commit()
    cursor.close()

# Read data from Excel files
opportunity_df = pd.read_excel('Samsara_-_Sales_Data_Analytics_Engineer_Exercise.xlsx', sheet_name='Opportunity')
quota_df = pd.read_excel('Samsara_-_Sales_Data_Analytics_Engineer_Exercise.xlsx', sheet_name='Quota')
fiscal_calendar_df = pd.read_excel('Samsara_-_Sales_Data_Analytics_Engineer_Exercise.xlsx', sheet_name='Fiscal_Calendar')

# Prepare data for insertion into Opportunity table
opportunity_data = opportunity_df[[
    'Opportunity_Type', 'Opportunity_Owner_ID', 'Opportunity_Created_Date', 'Opportunity_Close_Date',
    'Stage', 'Probability', 'ACV_Bookings', 'Industry', 'Sub_Region', 'Region', 'Segment'
]].values.tolist()

# Prepare data for insertion into Quota table
quota_data = quota_df[[
    'Quota_Period_Start_Date', 'Quota_Period_End_Date', 'Quota_Period', 'Quota_Region', 'Quota_Sub_Region',
    'Quota_Segment', 'Quota_Owner_ID', 'Quota_Owner_Name', 'Quota_Period_Timeframe', 'q1_quota', 'q2_quota',
    'q3_quota', 'q4_quota'
]].values.tolist()

# Prepare data for insertion into Fiscal_Calendar table
fiscal_calendar_data = fiscal_calendar_df[['Date', 'Fiscal_Year', 'Fiscal_Quarter']].values.tolist()

# Insert data into Opportunity table
insert_into_opportunity(opportunity_data)
print("This script connects to a MySQL database and inserts data from Excel sheets into Opportunity tables.")

# Insert data into Quota table
insert_into_quota(quota_data)
print("This script connects to a MySQL database and inserts data from Excel sheets into Quota tables.")

# Insert data into Fiscal_Calendar table
insert_into_fiscal_calendar(fiscal_calendar_data)
print("This script connects to a MySQL database and inserts data from Excel sheets into Fiscal_Calendar tables.")

# Close MySQL connection
mydb.close()
