# Sample data:
# 1, 0.1, 0.2, 73
# 1, 0.11, 0.1, 101
# 2, 0.23, 0.01, 17
# 2, 0.12, 0.15, 23
#
# Pretend this is taken from two (or more) different experiments: batch 1 and batch 2.
# Columns are:
#   batch number
#   x coordinate
#   y coordinate
#   measurement


def get_batch(filename):
    '''
    Take in a string filename, then extract values from the file, where the values are presented in this format: 1, 0.1, 0.2, 73.
    Seperate each values by splitting with ',' and create a list.
    Assign index at position 0 of the list as the batch number.
    Assign Batch number as a key to the dictionary called data.
    The values of data are lists with tuples containing replicates data for each batch.
    The function return data.
    '''
    data = dict()               # Or data = {}
    with open(filename, 'r') as h:
        for line in h:
            four_vals = line.split(',')         #Create a list of four columns name four_vals
            batch = four_vals[0]                #Assign the batch number as index position 0 of the four_vals list
            if not batch in data:
                data[batch] = []
            data[batch] += [(float(four_vals[1]), float(four_vals[2]), float(four_vals[3]))] # Collect data from an experiment
        return data


def results_ave(data):
    '''
    Take the dictionary called data as an parameter,
    and output the batch numbers with respective averages of the measurements
    '''
    for batch, sample in data.items():
        final_list = []
        if len(sample) > 0:
            n = 0
            x_sum = 0
            for (x, y, val) in sample:
                if x**2 + y**2 <= 1:
                    x_sum += val
                    n += 1
            average = x_sum/n
            return batch, average
        else:
            return batch
