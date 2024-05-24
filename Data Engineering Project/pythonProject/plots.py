import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Establish MySQL connection
mydb = mysql.connector.connect(
  host="your_host",
  user="your_username",
  password="your_password",
  database="your_database"
)

# Function to fetch data from MySQL
def fetch_data(query):
    cursor = mydb.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(data, columns=columns)
    cursor.close()
    return df

# Example queries to fetch data for plotting
opportunity_query = "SELECT * FROM Opportunity"
quota_query = "SELECT * FROM Quota"
fiscal_calendar_query = "SELECT * FROM Fiscal_Calendar"

# Fetch data from MySQL
opportunity_df = fetch_data(opportunity_query)
quota_df = fetch_data(quota_query)
fiscal_calendar_df = fetch_data(fiscal_calendar_query)

# Plotting examples
# Example 1: Histogram of ACV Bookings
plt.hist(opportunity_df['ACV_Bookings'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('ACV Bookings')
plt.ylabel('Frequency')
plt.title('Histogram of ACV Bookings')
plt.show()

# Example 2: Bar plot of Quota Attainment by Quota Owner
quota_attainment_by_owner = quota_df.groupby('Quota_Owner_Name')['Quota_Attainment'].mean().reset_index()
plt.bar(quota_attainment_by_owner['Quota_Owner_Name'], quota_attainment_by_owner['Quota_Attainment'], color='lightgreen')
plt.xlabel('Quota Owner')
plt.ylabel('Average Quota Attainment')
plt.title('Average Quota Attainment by Quota Owner')
plt.xticks(rotation=45)
plt.show()

# Example 3: Line plot of Fiscal Year-wise ACV Bookings
acv_bookings_by_year = opportunity_df.groupby('Fiscal_Year')['ACV_Bookings'].sum().reset_index()
plt.plot(acv_bookings_by_year['Fiscal_Year'], acv_bookings_by_year['ACV_Bookings'], marker='o', color='orange', linestyle='-')
plt.xlabel('Fiscal Year')
plt.ylabel('Total ACV Bookings')
plt.title('Total ACV Bookings by Fiscal Year')
plt.xticks(rotation=45)
plt.show()

# Example 4: Scatter plot of ACV Bookings vs. Probability
plt.scatter(opportunity_df['ACV_Bookings'], opportunity_df['Probability'], color='salmon', alpha=0.5)
plt.xlabel('ACV Bookings')
plt.ylabel('Probability')
plt.title('ACV Bookings vs. Probability')
plt.show()

# Close MySQL connection
mydb.close()
