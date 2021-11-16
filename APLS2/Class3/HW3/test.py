import unittest
from batch_means import get_batch, results_ave


class TestBatchMeans(unittest.TestCase):

    def test_batch_data(self):
        '''Test the file test_file.txt to correctly produce ditionary'''
        with open('test_data.txt', 'w') as f:
            f.write('1, 0.5, 0.5, 135\n')
        self.assertEqual(get_batch('test_data.txt'), {'1': [(0.5, 0.5, 135.0)]})

    def test_batch_ave(self):
        '''Test the average data with the default radius of 1, with unacceptable radius'''
        data = {'1': [(999999, 999999, 135)]}
        self.assertRaises(Exception, results_ave(data), data)

if __name__ == '__main__':
    unittest.main()