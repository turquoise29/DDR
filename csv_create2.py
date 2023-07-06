import os
import glob
import pandas as pd

def makecsv(file_path, save_dir):
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    df = pd.read_csv(file_path, header=None, skiprows=1, encoding="shift-jis", engine='python')
    df.columns = ['AP_name', 'Location index', 'RSSI (dBm)', 'Center Freq(MHz)']
    AP_name = df['AP_name']
    df['AP_name'] = df['Location index']
    df['Location index'] = AP_name
    df = df[df['AP_name'].str.contains('1F')]
    df_sorted = df.sort_values(by='AP_name')

    output_dir = os.path.join(save_dir, "output2")
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, file_name + "_APname.csv")
    df_sorted.to_csv(output_file, sep=',', index=False)

dir = "G:\\My Drive\\Classroom\\program\\data\\MeasurementData"

file_list = glob.glob(os.path.join(dir, "*.csv"))
for file_path in file_list:
    makecsv(file_path, dir)
