# DataSet Exaplanations

fio_fieldcontact files are for descriptions of officers for that particular year
fio_fieldnames are for descriptions of the suspect that the FIO filed on for that particular year

cleaned_fio_data is the combined and cleaned dataset with adjusted times to work with overtime data

All Overtime_merged_cleaned csv's are from another branch that were needed to do cross examinations with cleaned_fio_data 

Overtime_result csv's are all the instances of double dipping found between FIO and overtime data. 



# Data Script Explanations

fio_cleaning.py contains the cleaned and merged datasets for fio_fieldcontact and fio_fieldname tables. These also have time conversions
to fit Overtime data and MassDOT/ACLU time configurations

all other files are detecting double dipping between all other instances of overtimes which return a csv that contains all 
cross examples


