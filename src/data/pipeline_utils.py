import numpy as np
import pandas as pd
from raster2xyz.raster2xyz import Raster2xyz
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import os

cwd = os.getcwd()
repo_path = os.path.abspath(os.path.join(cwd, os.pardir, os.pardir))
data_path = os.path.join(repo_path, 'data')
data_processed_path = os.path.join(repo_path, 'data', 'processed')

avg_file_path = os.path.join(data_processed_path, 'avg-2012-2021.npy')
sd_file_path = os.path.join(data_processed_path, 'sd-2012-2021.npy')

avg = np.load(avg_file_path, allow_pickle=True)
sd = np.load(sd_file_path, allow_pickle=True)


def tiff_to_csv(tiff_path, csv_path):
    # Transform TIFF file from tiff_path into pandas DataFrame
    rtxyz = Raster2xyz()
    rtxyz.translate(tiff_path, csv_path)
    myRasterDF = pd.read_csv(csv_path)

    # Assign the temperatures to each value of z (color hue)
    grey_to_temp = np.linspace(-2, 35, 255)
    grey_to_temp = np.append(grey_to_temp, 0.999999)
    myRasterDF['temp'] = grey_to_temp[myRasterDF['z']]

    # Reshape the new variable 'temp' and save it to path_csv_out, which is the path were you'll save the csv file
    temp = np.reshape(np.ravel(myRasterDF['temp']), (1800, 3600))
    pd.DataFrame(temp).to_csv('temp.csv')


def temperature_to_anomalies(input_csv_path, output_csb_path, month):
    x = np.array(pd.read_csv(input_csv_path, header=None).replace(99999.0, 0))
    # Subtract average
    x -= avg[month]
    # Divide sd and return 0 if sd is 0 for that point
    x = np.divide(x, sd[month], out=np.zeros_like(x), where=sd[month] != 0)


def csv_to_png(csv_path, png_path):
    cmap = LinearSegmentedColormap.from_list('rg', ["blue", "w", "r"], N=256)
    t = np.array(pd.read_csv(csv_path, header=None).replace(99999.0, 0))
    plt.figure(figsize=(36, 18))
    plt.imshow(t, cmap=cmap, interpolation='nearest')
    plt.savefig(png_path)
