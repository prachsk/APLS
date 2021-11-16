def sum_timestamps(l):
    """
    >>> sum_timestamps(['5:32', '4:48'])
    '10:20'
    >>> sum_timestamps(['03:10', '01:00'])
    '4:10'
    >>> sum_timestamps(['2:10', '1:59'])
    '4:09'
    >>> sum_timestamps(['15:32', '45:48'])
    '1:01:20'
    >>> sum_timestamps(['6:15:32', '2:45:48'])
    '9:01:20'
    >>> sum_timestamps(['6:35:32', '2:45:48', '40:10'])
    '10:01:30'
    """
    # YOUR CODE HERE
    ################
    sum_t = 0
    for time in l:
        time_unit = time.split(':')
        if len(time.split(':')) == 2:
            if int(time_unit[0]) > 12:
                sum_t += int(time_unit[0])*60 + int(time_unit[1])
            else:
                sum_t += int(time_unit[0])*3600 + int(time_unit[1])*60
        else:
            sum_t += int(time_unit[0])*3600 + int(time_unit[1])*60 + int(time_unit[2])
    
    if sum_t%60 == 0:
       return "%d:%02d" % (sum_t / 3600, sum_t / 60 % 60) 
    else:
        return "%d:%02d:%02d" % (sum_t / 3600, sum_t / 60 % 60, sum_t % 60)
