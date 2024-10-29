import numpy as np
import pandas as pd

fc2022 = pd.read_csv(r'C:\Users\ChairmanPao\Desktop\DS539\data\fio_fieldcontact_2022.csv')
fc2021 = pd.read_csv(r'C:\Users\ChairmanPao\Desktop\DS539\data\fio_fieldcontact_2021.csv')
fc2020 = pd.read_csv(r'C:\Users\ChairmanPao\Desktop\DS539\data\fio_fieldcontact_2020.csv')
fn2022 = pd.read_csv(r'C:\Users\ChairmanPao\Desktop\DS539\data\fio_fieldnames_2022.csv')
fn2021 = pd.read_csv(r'C:\Users\ChairmanPao\Desktop\DS539\data\fio_fieldnames_2021.csv')
fn2020 = pd.read_csv(r'C:\Users\ChairmanPao\Desktop\DS539\data\fio_fieldnames_2020.csv')

fn2020.rename(columns={"frisk/search" : "was_frisked"}, inplace=True)
fn2020 = fn2020.drop(['otherclothing', 'sex', 'race', 'age', 'build', 'ethnicity', 'skin_tone', 'license_state', 'license_type', 'hair_style', 'deceased', 'was_frisked'], axis=1, errors = 'ignore')
fn2021 = fn2021.drop(['otherclothing', 'sex', 'race', 'age', 'build', 'ethnicity', 'skin_tone', 'license_state', 'license_type', 'person_id', 'hair_style', 'deceased', 'was_frisked'], axis=1, errors = 'ignore')
fn2022 = fn2022.drop(['otherclothing', 'sex', 'race', 'age', 'build', 'ethnicity', 'skin_tone', 'license_state', 'license_type', 'person_id', 'hair_style', 'deceased', 'was_frisked'], axis=1, errors = 'ignore')

fc2020 = fc2020.drop(['vehicle_year', 'vehicle_state', 'vehicle_color', 'vehicle_model', 'vehicle_style', 'vehicle_type', 'weather','key_situations',], axis=1, errors = 'ignore')
fc2021 = fc2021.drop(['vehicle_year', 'vehicle_state', 'vehicle_color', 'vehicle_model', 'vehicle_style', 'vehicle_type', 'weather','key_situations',], axis=1, errors = 'ignore')
fc2022 = fc2022.drop(['vehicle_year', 'vehicle_state', 'vehicle_color', 'vehicle_model', 'vehicle_style', 'vehicle_type', 'weather','key_situations',], axis=1, errors = 'ignore')

all_field_names = pd.concat([fn2020, fn2021, fn2022], ignore_index=True)
all_contact_names = pd.concat([fc2020, fc2021, fc2022], ignore_index=True)
# print(f'fn2022{fn2022.columns}')
# print(f'fn2021{fn2021.columns}')
# print(f'fn2020{fn2020.columns}')
# print(f'fc2022{fc2022.columns}')
# print(f'fc2021{fc2021.columns}')
# print(f'fc2020{fc2020.columns}')
# print(all_field_names)
# print(all_contact_names)
merged_data = pd.merge(all_contact_names, all_field_names, on='fc_num', how='inner')
# print(merged_data)
merged_data = merged_data.drop(['contact_reason'], axis=1)
merged_data.to_csv("cleaned_fio_data.csv", index=False)

