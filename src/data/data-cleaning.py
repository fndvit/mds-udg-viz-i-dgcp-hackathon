import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Get routes
cwd = os.getcwd()
repo_path = os.path.abspath(os.path.join(cwd, os.pardir, os.pardir))
print(repo_path)
data_path = os.path.join(repo_path, 'data')
data_raw_path = os.path.join(repo_path, 'data', 'raw')
sst_csv_path = os.path.join(repo_path, 'data', 'raw', 'SST-CSVs')

# Output file folders
data_processed_path = os.path.join(repo_path, 'data', 'processed')
csv_out_path = os.path.join(repo_path, 'data', 'processed', 'CSV')

# Initialize auxiliary arrays
years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
months = {'JAN': '01', 'FEB': '02', 'MAR': '03', 'APR': '04', 'MAY': '05', 'JUN': '06', 'JUL': '07', 'AUG': '08',
          'SEP': '09', 'OCT': '10', 'NOV': '11', 'DEC': '12'}

avg = {}
sd = {}
tmp = {}
for month in months:
    avg[month] = None
    sd[month] = None

avg = {}
sd = {}
for month in months:
  avg[month] = 0
  sd[month] = 0

# Monthly mean calculation
print("Monthly mean calculation: ")
for month in months:
    print("Processing: " + month)
    total = 0
    for year in years:
        try:
            # Compute mean
            avg[month] += np.array(pd.read_csv(os.path.join(
                sst_csv_path, 'MYD28M_' + str(year) + '-' + str(months[month]) + '.CSV.gz'), header=None)
                                   .replace(99999.0, 0))
            total += 1
        except:
            None

    avg[month] = avg[month]/total


# Monthly standard deviation calculation
print("Monthly standard deviation calculation: ")

for month in months:
    print("Processing: " + month)
    total = 0
    for year in years:
        try:
            x = np.array(pd.read_csv(os.path.join(
                sst_csv_path, 'MYD28M_' + str(year) + '-' + str(months[month]) + '.CSV.gz'), header=None)
                         .replace(99999.0, 0)) - avg[month]
            sd[month] += x*x
            total += 1

        except:
            None

    sd[month] = np.sqrt(sd[month]/total)

# Standarize data (Subtract mean and divide sd)
print("Subtract mean and divide sd: ")
for month in months:
    print("Processing: " + month)
    total = 0
    for year in years:
        try:
            x = np.array(pd.read_csv(os.path.join(
                sst_csv_path, 'MYD28M_' + str(year) + '-' + str(months[month]) + '.CSV.gz'), header=None)
                         .replace(99999.0, 0))
            # Subtract average
            x -= avg[month]
            # Divide sd and return 0 if sd is 0 for that point
            x = np.divide(x, sd[month], out=np.zeros_like(x), where=sd[month] != 0)

            pd.DataFrame(x).to_csv(
                path=os.path.join(csv_out_path, 'MYD28M_' + str(year) + '-' + str(months[month]) + '_STD.CSV.gz'),
                compression='gzip'
            )

        except:
            None

