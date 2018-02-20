import csv as c
import  datetime as date

def read_csv_to_dict(file_path):

    dict_data = {}
    date_list = []
    surge_list = []
    sensor1_list = []
    sensor2_list = []

    row_counter = 0
    time = date.datetime.now()

    with open(file_path) as csv_file:
        data = c.reader(csv_file,dialect='excel')

        for row in data:

            if row_counter == 0:
                print('skipping header')
            else:
                for index,value in enumerate(row):

                    if index == 0:
                        date_list.append((time + date.timedelta(seconds=row_counter)).strftime('%d/%m/%Y %H:%M:%S'))
                    elif index == 1:
                        surge_list.append(float(value))
                    elif index == 2:
                        sensor1_list.append(float(value))
                    else:
                        sensor2_list.append(float(value))
            row_counter = row_counter + 1

        dict_data.update({'_date': date_list})
        dict_data.update({'surge': surge_list})
        dict_data.update({'sensor1': sensor1_list})
        dict_data.update({'sensor2': sensor2_list})

    return dict_data
