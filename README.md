# DataSet Exaplanations 

fio_fieldcontact files are for descriptions of officers for that particular year fio_fieldnames are for descriptions of the suspect that the FIO filed on for that particular year

All Overtime_merged_cleaned csv's are from another branch that were needed to do cross examinations with cleaned_fio_data

Overtime_result csv's are all the instances of double dipping found between FIO and overtime data.

fio_cleaning.py contains the cleaned and merged datasets for fio_fieldcontact and fio_fieldname tables. These also have time conversions to fit Overtime data and MassDOT/ACLU time configurations

All other files are detecting double dipping between all other instances of overtimes which return a csv that contains all cross examples

# Cleaned_data 

Each file contains cleaned overtime data from 2020 to 2022 (2020 to 2021 for Records_merged_cleaned, due to missing 2022 data for "Records Request"). cleaned_fio_data is the combined and cleaned dataset with adjusted times to work with overtime data All files in this folder are used to produce those in cleaned_data.

The ACLU_merged_cleaned.csv contains Boston's cleaned MassDOT (traffic stop) data from 2020 to 2022. The (2020, 2021, 2022) ACLU files in this folder are used to produce the ACLU_merged_cleaned.csv.

# Notebooks 
All files in this folder are Jupyter notebooks used to either produce the files in cleaned_data or to compare overtime shifts (Intra_OT_EDA.ipynb). This folder contains the Jupyter notebook (ACLU_merging_cleaning.ipynb) used to produce the cleaned ACLU_merged_cleaned.csv (MassDOT) in cleaned_data and the notebooks to compare MassDOT with Overtime.
