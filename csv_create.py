import os
import glob
import pandas as pd

def makecsv(file_path, save_dir):
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    df = pd.read_csv(file_path, header=None, skiprows=1, encoding="shift-jis", engine='python')
    RSSI = df[2]
    times = [1]
    threshold = 20
    df = df[df[1].str.contains('1F')]

    for i in range(1, len(df)):
        current_value = RSSI[i]
        previous_value = RSSI[i-1]

        if current_value - previous_value >= threshold:
            times.append(times[-1] + 1)
        else:
            times.append(times[-1])

    df['times'] = times

    df.columns = ['Location index', 'AP_name', 'RSSI (dBm)', 'Center Freq(MHz)', 'times']

    output_file = os.path.join(save_dir, file_name + "_times.csv")
    df.to_csv(output_file, sep=',', index=False)

dir = "G:\\My Drive\\Classroom\\program\\data\\MeasurementData"
outdir = os.path.join(dir, "output1")

file_list = glob.glob(os.path.join(dir, "*.csv"))
for file_path in file_list:
    makecsv(file_path, outdir)
