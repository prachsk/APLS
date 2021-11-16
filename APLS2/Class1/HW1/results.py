def main():
    '''
    Script to import gget_batch and results_ave from batch_mean.py
    It also takes input of the file name and print out the results of the function.
    '''
    from batch_means import get_batch
    from batch_means import results_ave
    filename = str(input('Which data file? '))
    final = results_ave(get_batch(filename))
    for i in final:
        print(i)

if __name__ == '__main__':
    main()