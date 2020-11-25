"""
Two Sum can be easily performed in the time complexity of O of N^2
but what matters the most is it's not efficient
so doing better way is to do in a linear time
"""

arr = [7,2,3,2,4,4]
target = 8
my_dict = dict()
def two_sum():
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in my_dict:
            return(i,my_dict[complement])
        else:
            my_dict[arr[i]] = i
print(two_sum())
