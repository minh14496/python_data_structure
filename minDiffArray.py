"""
You are given two integer arrays a and b of the same length. 

Let's define the difference between a and b as the sum of absolute differences of corresponding elements: 

difference = |a[0] - b[0]| + |a[1] - b[1]| + ... + |a[a.length - 1] - b[b.length - 1]| 
 

You can replace one element of a with any other element of a. Your task is to return the minimum possible difference between a and b that can be achieved by performing at most one such replacement on a. You can also choose to leave the array intact. 

Example 

For a = [1, 3, 5] and b = [5, 3, 1], the output should be minDiffOfArrays(a, b) = 4. 

If we leave the array a intact, the difference is |1 - 5| + |3 - 3| + |5 - 1| = 8; 

If we replace a[0] with a[1], we get a = [3, 3, 5] and the difference is |3 - 5| + |3 - 3| + |5 - 1| = 6; 

If we replace a[0] with a[2], we get a = [5, 3, 5] and the difference is |5 - 5| + |3 - 3| + |5 - 1| = 4; 

If we replace a[1] with a[0], we get a = [1, 1, 5] and the difference is |1 - 5| + |1 - 3| + |5 - 1| = 10; 

If we replace a[1] with a[2], we get a = [1, 5, 5] and the difference is |1 - 5| + |5 - 3| + |5 - 1| = 10; 

If we replace a[2] with a[0], we get a = [1, 3, 1] and the difference is |1 - 5| + |3 - 3| + |1 - 1| = 4; 

If we replace a[2] with a[1], we get a = [1, 3, 3] and the difference is |1 - 5| + |3 - 3| + |3 - 1| = 6; 

So the final answer is 4, since it's the minimum possible difference. 
"""
def minDiffArray(a,b):
    # a = [1, 3, 5, 8] and b = [5, 3, 2, 2]
    # If we leave the array a intact, the difference is |1 - 5| + |3 - 3| + |5 - 2| + |8-1| = 8; 
    # |1 - 5| + |3 - 3| + |5 - 2| + |8-2| = 13
    #  4 + 0 + 3 + 6 -> [4,0,3,6]
    #|1 - 5| + |3 - 3| + |5 - 2| + |1-2| = 8
    # 4 + 0 + 3 + 1
    # lower 4 by replacing it with any number in the array
    diff = [] # original diferent array
    for i in range(len(a)):
        diff.append(abs(a[i]-b[i]))
    # find the index of the max diff
    idx = 0 # for example
    temp = diff[0]
    for i in range(len(a)):
        if diff[i] >= temp:
            temp = diff[i]
            idx = i
    min_ = diff[idx]
    # [4,0,3,6] -> idx = 3
    for i in range(len(a)):
        if i != idx:
            if abs(a[i]-b[idx]) <= min_:
                min_ = abs(a[i]-b[idx])
    diff[idx] = min_
    return sum(diff)

a = [9,3,4]
b = [7,3,6]
print(minDiffArray(a,b))


