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
avg_file_path = os.path.join(data_processed_path, 'avg-2012-2021.npy')
sd_file_path = os.path.join(data_processed_path, 'sd-2012-2021.npy')

# Initialize auxiliary arrays
years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

months = {'JAN': '01', 'FEB': '02', 'MAR': '03', 'APR': '04', 'MAY': '05', 'JUN': '06', 'JUL': '07', 'AUG': '08',
          'SEP': '09', 'OCT': '10', 'NOV': '11', 'DEC': '12'}
# years = [2012, 2013]
# months = {'JAN': '01', 'FEB': '02'}
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
if os.path.isfile(avg_file_path):
    avg = np.load(avg_file_path, allow_pickle=True)
else:
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
    np.save(avg_file_path, avg, allow_pickle=True)

# Monthly standard deviation calculation

if os.path.isfile(sd_file_path):
    sd = np.load(sd_file_path, allow_pickle=True)
else:
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
    np.save(sd_file_path, sd, allow_pickle=True)

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

            os.makedirs(csv_out_path, exist_ok=True)
            csv_out_file_path = os.path.join(csv_out_path, 'MYD28M_' + str(year) + '-' + str(months[month]) + '_STD.CSV')
            pd.DataFrame(x).to_csv(csv_out_file_path)

        except Exception as e:
            print(e)



