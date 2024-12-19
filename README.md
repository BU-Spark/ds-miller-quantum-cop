# Project Overview

This repository contains data and scripts related to analyzing overtime and Field Interrogation and Observation (FIO) data, focusing on identifying patterns of double-dipping and cleaning datasets for analysis.

---

## DataSet Explanations

### General
- **fio_fieldcontact**: Descriptions of officers for a specific year.
- **fio_fieldnames**: Descriptions of the suspect associated with the FIO filed for a specific year.
- **cleaned_fio_data**: A combined and cleaned dataset with time adjustments for compatibility with overtime data.
- **Overtime_merged_cleaned CSVs**: Datasets from another branch, used for cross-examination with `cleaned_fio_data`.
- **Overtime_result CSVs**: Instances of double-dipping found between FIO and overtime data.

### From Branch: Taiyo
- **cleaned_data**: Contains cleaned overtime data files (2020–2022). Note: `Records_merged_cleaned` includes only 2020–2021 due to missing 2022 data for "Records Request."
- **data**: Source files used to produce the files in `cleaned_data`.
- **notebooks**: Jupyter notebooks used for processing `cleaned_data` files and comparing overtime shifts (e.g., `Intra_OT_EDA.ipynb`).

### From Branch: Jason
- **cleaned_data**: Includes `ACLU_merged_cleaned.csv`, which contains cleaned Boston MassDOT (traffic stop) data from 2020 to 2022.
- **data**: Contains the ACLU files (2020, 2021, 2022) used to produce `ACLU_merged_cleaned.csv`.
- **notebooks**: Includes `ACLU_merging_cleaning.ipynb` for producing `ACLU_merged_cleaned.csv` and notebooks for comparing MassDOT with overtime data.

---

## Data Script Explanations

### General
- **fio_cleaning.py**: Processes and merges datasets from `fio_fieldcontact` and `fio_fieldname`, including time conversions for compatibility with Overtime and MassDOT/ACLU time configurations.
- **Other scripts**: Detect double-dipping instances across overtime datasets, outputting CSVs with cross-examples.

---

## Cleaned Data Overview
- **cleaned_fio_data**: A combined and cleaned dataset, adjusted for time compatibility with overtime data.
- **ACLU_merged_cleaned.csv**: Cleaned MassDOT data from 2020–2022.
- **Overtime_merged_cleaned**: Cleaned overtime datasets from 2020–2022.

---

## Notebooks
- **Intra_OT_EDA.ipynb**: Compares overtime shifts.
- **ACLU_merging_cleaning.ipynb**: Produces `ACLU_merged_cleaned.csv` and facilitates comparison of MassDOT and overtime datasets.

---

## Final Steps
At the end of the semester, during project wrap-up, open a final pull request from the `dev` branch to the `main` branch.
