import read_csv_file as file_reader

data = {}

data = file_reader.read_csv_to_dict('ap_surge_sensor_comparison.csv')

print(data)
