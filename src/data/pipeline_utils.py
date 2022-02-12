import numpy as np
import pandas as pd
from raster2xyz.raster2xyz import Raster2xyz
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

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


def csv
cmap=LinearSegmentedColormap.from_list('rg',["blue", "w", "r"], N=256)

t = np.array(pd.read_csv('./drive/MyDrive/HACKATTON/MYD28M_2021-11.CSV',header = None).replace(99999.0,0))
t = t - avg['NOV']
for i in range(1800):
  for j in range(3600):
    try:
      t[i][j] = t[i][j]/sd['NOV'][i][j]

    except:
      None

print('Standarized anomalies')
plt.figure(figsize = (36,18))
plt.imshow(t, cmap=cmap, interpolation='nearest')

pd.DataFrame(t).to_csv('./Lastest_anomalies.csv')
plt.savefig('./Lastest_anomalies.png')