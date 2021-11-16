class BatchObj:
    '''
    Create datapoint objects for the data in baches.
    Theese are batch numbers, x-coordinates, y-coordinates, and measurements.
    '''
    def __init__(self, batchnum, xco, yco, measure):
        self.batchnum = int(batchnum)
        self.xco = float(xco)
        self.yco = float(yco)
        self.measure = int(measure)
        if self.xco**2 + self.yco**2 <= 1:
            self.valid = True
        else:
            self.valid = False
        
class BatchData:
    '''
    Associate the batch numbers with the list of related measurement values.
    Create a method to get the average of measurements coreesponding to the batch number as 'get_ave'.
    '''
    def __init__(self, list_dataobj):
        self.batchnumber = list_dataobj[0].batchnum 
        self.batch_measure = []
        for data in list_dataobj:
            if data.valid == True:
                self.batch_measure.append(data.measure)

    def get_ave(self):
        '''
        A method to calculate the average of measurements for each batch.
        This method returns the average.
        '''
        self.get_ave = sum(self.batch_measure)/len(self.batch_measure)
        return self.get_ave
        


def get_batchdata(filename):
    '''
    Take in a string filename as a parameter, then extract values from the file, where the values are presented in this format: 1, 0.1, 0.2, 73.
    Seperate each values by splitting with ',' and create a list.
    Assign data in each line to the corresponding batch object by using class BatchObj into a list.
    The function returns a list containg batch objects.
    ''' 
    with open(filename, 'r') as f:
        list_batchdata = []
        for line in f:
            four_vals = line.split(',')         #Create a list of four columns name four_vals
            list_batchdata.append(BatchObj(four_vals[0], four_vals[1], four_vals[2], four_vals[3])) #Asssign the values in the list into corresponding object atributes in class BatchObj
    return list_batchdata

def group_batch(list_batchdata):
    '''
    Take in a list of batch objects as a parameter.
    Assign the objects into class BatchData.
    The function returns a list of grouped objects after being assigned to class BatchData
    '''
    pre_batch = []
    final_batches = [] 
    for i, values in enumerate(list_batchdata):
        if len(pre_batch) == 0:
            pre_batch.append(values)
        elif list_batchdata[i].batchnum == list_batchdata[i-1].batchnum:
            pre_batch.append(values)
        else:
            final_batches.append(BatchData(pre_batch))
            pre_batch = []
            pre_batch.append(values)
    final_batches.append(BatchData(pre_batch)) # Collect data after being grouped
    return final_batches

def main():
    batch_data = group_batch(get_batchdata('batch_data.txt'))
    for i in batch_data:
        print(str(i.batchnumber) + '\t' + str(round(i.get_ave(), 2)))

if __name__ == '__main__':
    main()