"""
# An array (or subarray) is alternating if the numbers are in the pattern
# of alternating odd/even, for example [1,2,3] is alternating but [1,1] is not
# An array of length one is counted as alternating.
# Given an array, count how many subarrays does it contain that are alternating
# ex: [1,2,3], answer is 6 because [1], [2], [3], [1,2], [2,3], [1,2,3] are all
# alternating
# ex2: [4,5,5,4] answer is 6 because [4] [5] [5] [4] [4,5] [5,4] are alternating

# def alternatingSubarrays(arr):

# test = [1,2,3]
# 6
# test = [1,2,3,4,5]
# 15
# test = [1, 1, 1, 1, 1]
# 5
# test = [4, 5, 5, 6]
# 6
# test = [11, 16, 5, 35, 4, 88]
# 10
"""

def alternatingSubarrays(arr):
    if arr:
        streak = 1 # keep track of how long our streak is
        answer = 1 # keep track of our answer
        previous = arr[0] #initialize a previous tracker
        for i in arr[1:]: # iterate through the rest of the array
            if (i + previous) % 2 == 1: # if current and previous are alternating
                streak += 1 # increase the streak
            else: #otherwise
                streak = 1 # reset streak
            answer += streak # we add our streak to answer
            previous = i # advance previous
        
        return answer
    else:
        return 0
print(alternatingSubarrays([1,2,3,4,5]))