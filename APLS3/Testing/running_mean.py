def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
  # YOUR CODE HERE
  ################
    total = 0
    result = []
    i = 1
    for num in sequence:
      total += num
      ave = total/i
      result.append(round(ave,2))
      i+=1
    return result
