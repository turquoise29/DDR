import glob
import os
import csv

def merge_csv_by_ap_name(input_file, output_file):
    ap_data = {}
    with open(input_file, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        fieldnames = reader.fieldnames
        for row in reader:
            ap_name = row['AP_name']
            if ap_name not in ap_data:
                ap_data[ap_name] = []
            ap_data[ap_name].append(row)

    with open(output_file, 'w', newline='') as csv_file:
        fieldnames_extended = fieldnames
        for i in range(1, len(ap_data)):
            fieldnames_extended += [f'Location index_{i}', f'RSSI (dBm)_{i}', f'Center Freq(MHz)_{i}']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames_extended)
        writer.writeheader()

        # データの連結と出力
        for ap_name, rows in ap_data.items():
            merged_row = {}
            for i, row in enumerate(rows):
                for fieldname in fieldnames:
                    merged_row[f"{fieldname}_{i+1}"] = row.get(fieldname, '')
            writer.writerow({k: v for k, v in merged_row.items() if k in fieldnames_extended})

def process_csv_files(directory):
    file_list = glob.glob(os.path.join(directory, "*.csv"))
    for file_path in file_list:
        file_name = os.path.basename(file_path)
        output_dir = os.path.join(directory, "outputAP")
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, "output_" + file_name)
        merge_csv_by_ap_name(file_path, output_file)

# 指定されたディレクトリ内のCSVファイルを処理する
directory = r"G:\My Drive\Classroom\program\data\MeasurementData\output2"
process_csv_files(directory)
