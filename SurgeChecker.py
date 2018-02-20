

def check_for_surges(surgecurrentarray):
    #surgearraylen=1000
    surgearray=surgecurrentarray['surge'] #read contents of key named 'surge' into surgearray
    surgelen=len(surgearray)
    for v in range(0,surgelen):
        if v==surgelen - 1: #check if the loop has reached the second last data point & exit if it has
            break
        if surgearray[v]>=4.9:
            if surgearray[v+1]>=4.9:
                print('A surge occured at position {}'.format(v+2))
            else:
                continue
        else:
            continue
    else:
        print('Surge check complete!')
    return()


def deficits_gains(surgecurrentarray):

    sens_1=surgecurrentarray['sensor1']
    sens_2=surgecurrentarray['sensor2']
    stamp=surgecurrentarray['_date']

    surgelen=len(stamp)
    print(surgelen)
    print('about to check for gains and losses.')

    for v in range(0,surgelen):
        print('checking {0}.'.format(v))
        if sens_1[v] - sens_2[v] > 0.0:
            deficit=sens_1[v]-sens_2[v] #although sens2 - sens1 is negative, the deficit should be printed as a positive number
            print(sens_2[v]-sens_1[v])
            print('Found deficit of {0} at time {1}'.format(deficit,stamp[v]))
        elif sens_1[v] - sens_2[v] < 0.0:
            gains=sens_2[v]-sens_1[v]
            print('Found gain of {0} at time {1}'.format(gains,stamp[v]))

    print('Finished.')
    return()


