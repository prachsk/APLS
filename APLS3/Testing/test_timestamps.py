import timestamps
from timestamps import sum_timestamps
# YOUR CODE HERE
################
def test_seum_timestamps():
    assert sum_timestamps(['5:32', '4:48']) == '10:20'
    assert sum_timestamps(['03:10', '01:00']) == '4:10'
    assert sum_timestamps(['2:10', '1:59']) == '4:09'
    assert sum_timestamps(['15:32', '45:48']) == '1:01:20'
    assert sum_timestamps(['6:15:32', '2:45:48']) == '9:01:20'
    assert sum_timestamps(['6:35:32', '2:45:48', '40:10']) == '10:01:30'
