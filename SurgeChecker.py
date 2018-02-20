

def checkforsurges(surgecurrentarray)
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

def deficitsgains(surgecurrentarray):
    sens_1=surgearray['sensor1']
    sens_2=surgearray['sensor2']
    stamp=surgearray['_date']
    surgelen=len(stamp)

    for v in range(0,surgelen):
        if sens_2[v]-sens_1[v]<0:
            deficit=sens_1[v]-sens_2[v] #although sens2 - sens1 is negative, the deficit should be printed as a positive number
            print('Found deficit of {} at time {}'.format(deficit,stamp[v]))
        else:
            if sens_2[v]-sens_1[v]>0:
                gains=sens_2[v]-sens_1[v]
                print('Found gain of {} at time {}'.format(gains,stamp[v]))
            else:
                continue
            continue
        return()


