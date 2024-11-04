import pandas as pd

# Load data
fio = pd.read_csv(r'cleaned_fio_data.csv')
records = pd.read_csv(r'data/Records_Request_2020_2021.csv')

# Narrow down to essential columns before merging
fio = fio[['fc_num', 'contact_date_x', 'contact_officer', 'contact_officer_name']]
records = records[['IDNO6', 'NAME', 'OTDATE', 'STARTTIME', 'ENDTIME']]

# Convert dates and times to the correct formats
fio['contact_date_x'] = pd.to_datetime(fio['contact_date_x'])
fio['date'] = fio['contact_date_x'].dt.date
fio['time'] = fio['contact_date_x'].dt.time
records['OTDATE'] = pd.to_datetime(records['OTDATE']).dt.date

# Filter `records` to the date range present in `fio` to minimize merge load
date_range = (fio['date'].min(), fio['date'].max())
records = records[(records['OTDATE'] >= date_range[0]) & (records['OTDATE'] <= date_range[1])]

# Normalize officer names to lowercase and remove any spaces after commas for consistency
fio['contact_officer_name'] = fio['contact_officer_name'].str.strip().str.lower().str.replace(", ", ",", regex=False)
records['NAME'] = records['NAME'].str.strip().str.lower().str.replace(", ", ",", regex=False)

# Perform a left merge to reduce the resulting DataFrame size
merged_df = fio.merge(records, left_on='date', right_on='OTDATE', how='left')

# Drop rows where there was no match in `records`
merged_df = merged_df[merged_df['NAME'].notna()]

# Check size after merge and filtering
print("Shape after filtering merged DataFrame:", merged_df.shape)

# Proceed with further filtering on time and name if needed
# Apply time matching logic only on reduced DataFrame
print(merged_df)
