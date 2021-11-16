import argparse
from collections import OrderedDict

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
            try:
                if 'O' not in line:
                    four_vals = line.split(',')         #Create a list of four columns name four_vals
                    batch = four_vals[0]                #Assign the batch number as index position 0 of the four_vals list
                    if (len(four_vals)) == 4:
                        if not batch in data:
                            data[batch] = []
                        data[batch] += [(float(four_vals[1]), float(four_vals[2]), float(four_vals[3]))] # Collect data from an experiment
                    else:
                        pass
                        raise ValueError ('invalid format (wrong number of values)')
                else:
                    pass
                    raise ValueError ('invalid string: "O" ')
            except ValueError:
                print('Invalid data format {}'.format(line))
                pass
        return data

def results_ave(data, radius=1):
    '''
    Take the dictionary called data as an parameter,
    and output the batch numbers with respective averages of the measurements
    '''
    batch_average = {}
    for batch, sample in sorted(data.items(), key=lambda x: int(x[0])):
        if len(sample) > 0:
            n = 0
            x_sum = 0
            for (x, y, val) in sample:
                if x**2 + y**2 <= radius:
                    x_sum += val
                    n += 1
                try:
                    average = round(x_sum/n, 2)
                except ZeroDivisionError:
                    average = 'The coordinates are not within the radius.'
            batch_average[batch] = average
        else:
            batch_average[batch] = 'No Data'
    return batch_average
    
def main(args):
    final = results_ave(get_batch(args.infile), args.radius)
    for batch, ave in final.items():
        print(batch, '\t', ave)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Find the mean of the batch measurements.",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('radius', type=float, default=1)
    parser.add_argument('infile', type=str, help='input data file as .txt')

    args = parser.parse_args()
    main(args)

