import random
import argparse

def main(args):
    with args.outfile as outfile:                                                    
        for i in range(0, args.n):
            batch = random.randint(1,args.b)
            x = round(random.uniform(0, 3))
            y = round(random.uniform(0, 3))
            measure = random.randint(10, 150)
            outfile.write('{}, {}, {}, {}\n'.format(batch, x, y, measure))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate batch data.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('n', type=int, default=30, help='The number of data points')
    parser.add_argument('b', type=int, default=7, help='The number of different batch IDs')
    parser.add_argument('outfile', type=argparse.FileType('w'), help='Put in the file name with .txt \ Output TXT-file')
    args = parser.parse_args()
    main(args)