def check_current_losses(data_dict):

    # Get the Acme Power dataset from get_csv.py
    acme_power_dictionary = data_dict

    # Create a list for the required data
    timestamp = acme_power_dictionary.get('_date')
    first_sensor = acme_power_dictionary.get('sensor1')
    last_sensor = acme_power_dictionary.get('sensor2')

    # Create a list to store the current gains or losses
    current_loss = []

    # Create a variable to sum of all current losses
    total_current_loss = 0.0

    # Calculate a loss or gain for each value in the dataset
    # A positive value indicates a loss
    for i in range(0, 1000):
        loss_gain = first_sensor[i] - last_sensor[i]
        current_loss.append(loss_gain)

    # Check for current losses
    for x, value in enumerate(current_loss):
        if value >= 0.0:
            total_current_loss = total_current_loss + value

            # Write losses to a log file
            with open('current_losses.log', 'a') as logfile:
                logfile.write('{0}\t\tCurrent Loss of {1} at row {2}.'.format(timestamp[x], value, x+1))
                logfile.write('\n')

    print('The total sum of current loss across the entire system is {0}'.format(total_current_loss))
