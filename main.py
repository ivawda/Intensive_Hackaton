import read_csv_file as file_reader
import current_gain_loss  as gain_loss
import SurgeChecker as surge_checker

data = {}

data = file_reader.read_csv_to_dict('ap_surge_sensor_comparison.csv')

print('Checking for surges')

surge_checker.check_for_surges(data)

print('Checking for gains and deficits')

surge_checker.deficits_gains(data)

print('Checking for total current loss')

gain_loss.check_current_losses(data)


print('Finished executing programme')
