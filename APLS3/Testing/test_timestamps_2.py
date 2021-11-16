import pytest
from timestamps import sum_timestamps

# YOUR CODE HERE
################
@pytest.mark.parametrize("input_argument, expected_return", [
    (['5:32', '4:48'], '10:20'),
    (['03:10', '01:00'],'4:10'),
    (['2:10', '1:59'], '4:09'),
    (['15:32', '45:48'], '1:01:20'),
    (['6:15:32', '2:45:48'], '9:01:20'),
    (['6:35:32', '2:45:48', '40:10'], '10:01:30'),
])
def test_timestamps_2(input_argument, expected_return):
    assert sum_timestamps(input_argument) == expected_return
