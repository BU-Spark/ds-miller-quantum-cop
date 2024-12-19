import pandas as pd

# Load data
fio = pd.read_csv(r'data/cleaned_fio_data.csv')
events = pd.read_csv(r'data/Events_merged_cleaned.csv')

# Narrow down to essential columns before merging
fio = fio[['fc_num', 'contact_date_x', 'contact_officer', 'contact_officer_name']]
events = events[['ID', 'NAME', 'OTDATE', 'STARTTIME', 'ENDTIME']]

# Convert dates and times to the correct formats
fio['contact_date_x'] = pd.to_datetime(fio['contact_date_x'])
fio['date'] = fio['contact_date_x'].dt.date
fio['time'] = fio['contact_date_x'].dt.time
events['OTDATE'] = pd.to_datetime(events['OTDATE']).dt.date
events['STARTTIME'] = events['STARTTIME'].astype(int)
events['ENDTIME'] = events['ENDTIME'].astype(int)

# Function to parse time in different formats
def parse_time(time_str):
    if pd.isna(time_str):
        return None
    time_str = str(time_str).zfill(4)  # Ensure it's 4 characters, padding with zeroes if needed
    if ':' in time_str:  # If the time already contains colons, parse it directly
        return pd.to_datetime(time_str, format='%H:%M:%S').time()
    else:  # If time is in "HHMM" format, convert it
        return pd.to_datetime(time_str, format='%H%M').time()

# Apply the parse_time function to STARTTIME and ENDTIME columns
events['STARTTIME'] = events['STARTTIME'].apply(parse_time)
events['ENDTIME'] = events['ENDTIME'].apply(parse_time)

# Filter `records` to the date range present in `fio` to minimize merge load
date_range = (fio['date'].min(), fio['date'].max())
records = events[(events['OTDATE'] >= date_range[0]) & (events['OTDATE'] <= date_range[1])]

# Normalize officer names to lowercase and remove any spaces after commas for consistency
fio['contact_officer_name'] = fio['contact_officer_name'].str.strip().str.lower().str.replace(", ", ",", regex=False)
records['NAME'] = records['NAME'].str.strip().str.lower().str.replace(", ", ",", regex=False)

# Merge DataFrames based on date and name
merged_df = fio.merge(records, left_on=['date', 'contact_officer_name'], right_on=['OTDATE', 'NAME'], how='left')

# Drop rows where there was no match in `records`
merged_df = merged_df[merged_df['NAME'].notna()]

# Filter for time overlaps (where fio time is within the range of records' STARTTIME and ENDTIME)
merged_df['time_overlap'] = merged_df.apply(lambda row: row['STARTTIME'] <= row['time'] <= row['ENDTIME'] if pd.notnull(row['STARTTIME']) and pd.notnull(row['ENDTIME']) else False, axis=1)

# Keep only rows where there is a time overlap
overlapping_df = merged_df[merged_df['time_overlap']]

# Check size after filtering for overlaps and display result
print("Shape after filtering for time overlaps:", overlapping_df.shape)
print(overlapping_df)
overlapping_df.to_csv("data/events_results.csv", index=False)


