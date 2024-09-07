import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load shapefile
zone_data = gpd.read_file("NT_Croc_Capture_Zones.shp")
zone_data = zone_data.rename(columns={"ZONENAME": "ZONE_NAME"})


# Preview the data
print(zone_data)

# Plot the zone_data
zone_data.plot()
plt.show()

# df = pd.read_csv('NT Crocodile Capture.csv')

# # Convert 'DATE_CAPTURED' to datetime format
# df['DATE_CAPTURED'] = pd.to_datetime(df['DATE_CAPTURED'])

# # Extract the month from 'DATE_CAPTURED' and create a new column 'MONTH_CAPTURED'
# df['MONTH_CAPTURED'] = df['DATE_CAPTURED'].dt.month_name()

# # Preview the updated DataFrame
# print(df)

# # Group by 'ZONE_NAME' and 'MONTH_CAPTURED' and count the number of captures
# captures_per_zone_month = df.groupby(['ZONE_NAME', 'MONTH_CAPTURED']).size().reset_index(name='CAPTURE_COUNT')

# # Save the result to a new CSV file
# captures_per_zone_month.to_csv('captures_per_zone_month.csv', index=False)

# # Preview the new DataFrame
# print(captures_per_zone_month.head())





# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the data from the CSV
# df = pd.read_csv('captures_per_zone_month.csv')

# # Pivot the data to get months as columns and zones as rows
# pivot_table = df.pivot_table(index='MONTH_CAPTURED', columns='ZONE_NAME', values='CAPTURE_COUNT', aggfunc='sum').fillna(0)

# # Sort months if needed (assuming the data includes all months)
# month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# pivot_table = pivot_table.reindex(month_order)

# # Preview the pivot table
# print(pivot_table)

# # Create a stacked bar plot
# pivot_table.plot(kind='bar', stacked=True, figsize=(10, 7), colormap='tab10')

# # Add title and labels
# plt.title('Captures per Zone per Month')
# plt.xlabel('Month Captured')
# plt.ylabel('Number of Captures')

# # Add legend with title
# plt.legend(title='Zone Name')

# # Rotate x-axis labels for better readability
# plt.xticks(rotation=45)

# # Show the plot
# plt.tight_layout()
# plt.show()


# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Assuming 'captures_per_zone_month.csv' is the file created in the previous step
# df = pd.read_csv('captures_per_zone_month.csv')

# # Plot the data as a bar chart
# plt.figure(figsize=(12, 6))
# sns.barplot(x='MONTH_CAPTURED', y='CAPTURE_COUNT', hue='ZONE_NAME', data=df)

# plt.title('Captures per Zone per Month')
# plt.xlabel('Month Captured')
# plt.ylabel('Number of Captures')
# plt.legend(title='Zone Name')
# plt.xticks(rotation=45)
# plt.tight_layout()

# # Show the plot
# plt.show()
