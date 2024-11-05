import pandas as pd

# Load data
fio = pd.read_csv(r'data/cleaned_fio_data.csv')
detail = pd.read_csv(r'data/Detail_merged_cleaned.csv')

# Narrow down to essential columns before merging
fio = fio[['fc_num', 'contact_date_x', 'contact_officer', 'contact_officer_name']]
detail = detail[['RowId', 'Emp_Name', 'Start_date', 'Start_Time', 'End_Time']]

# Convert dates and times to the correct formats
fio['contact_date_x'] = pd.to_datetime(fio['contact_date_x'])
fio['date'] = fio['contact_date_x'].dt.date
fio['time'] = fio['contact_date_x'].dt.time
detail['Start_date'] = pd.to_datetime(detail['Start_date']).dt.date

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
detail['Start_Time'] = detail['Start_Time'].apply(parse_time)
detail['End_Time'] = detail['End_Time'].apply(parse_time)

# Filter `records` to the date range present in `fio` to minimize merge load
date_range = (fio['date'].min(), fio['date'].max())
records = detail[(detail['Start_date'] >= date_range[0]) & (detail['Start_date'] <= date_range[1])]

# Normalize officer names to lowercase and remove any spaces after commas for consistency
fio['contact_officer_name'] = fio['contact_officer_name'].str.strip().str.lower().str.replace(", ", ",", regex=False)
records['Emp_Name'] = records['Emp_Name'].str.strip().str.lower().str.replace(", ", ",", regex=False)

# Merge DataFrames based on date and name
merged_df = fio.merge(records, left_on=['date', 'contact_officer_name'], right_on=['Start_date', 'Emp_Name'], how='left')

# Drop rows where there was no match in `records`
merged_df = merged_df[merged_df['Emp_Name'].notna()]

# Filter for time overlaps (where fio time is within the range of records' STARTTIME and ENDTIME)
merged_df['time_overlap'] = merged_df.apply(lambda row: row['Start_Time'] <= row['time'] <= row['End_Time'] if pd.notnull(row['Start_Time']) and pd.notnull(row['End_Time']) else False, axis=1)

# Keep only rows where there is a time overlap
overlapping_df = merged_df[merged_df['time_overlap']]

# Check size after filtering for overlaps and display result
print("Shape after filtering for time overlaps:", overlapping_df.shape)
print(overlapping_df)
overlapping_df.to_csv("data/detail_results.csv", index=False)


