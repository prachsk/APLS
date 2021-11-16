import random

total_experiment = int(input('Please put in the total number of experiments: '))                #Get the total number of experiments
total_replicate = int(input('Please put in the total number of replicates per experiment: '))   #Get the total number of replicates per experiment   
with open('batch_data.txt', 'w') as outfile:                                                    #Create a file called batch_data.txt to write the data on to it
    for i in range(1, total_experiment+1):
        for batchlist in range(0, total_replicate):
            batchlist = [i]
            batchlist += [round(random.uniform(0, 1), 2) for i in range(2)]
            batchlist += [random.randint(10, 150)]
            x = ', '.join(str(data) for data in batchlist)                                      #Extracting every data from the list and turn it into str
            outfile.write('{}\n'.format(x))                                                     #Outputting data onto batch_data.txt
