# Input: nums = [1,2,3,3,4,4,5,6], k = 4
# ===Output: true
# Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
# Example 2:

# Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
# Output: true
# Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
# Example 3:
 
# Input: nums = [3,3,2,2,1,1], k = 3
# Output: true

from collections import Counter
def is_possible_divide(nums, k):
    if len(nums) % k != 0:
        return False

    freq = Counter(nums)
    for num in sorted(freq):
        while freq[num] > 0:
            # Try to form a group starting from num to num+k-1
            for i in range(k):
                if freq[num + i] <= 0:
                    return False
                freq[num + i] -= 1

    return True
nums = [1,2,3,3,4,4,5,6] 
k = 4
print(is_possible_divide(nums,k))