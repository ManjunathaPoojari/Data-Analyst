# Input: arr = [4,2,1,3]
# ==Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
# Example 2:
 
# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]
# Example 3:
 
# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]

def abs_difference(arr):
    arr.sort()  
    min_diff = float('inf')
    
    result = []

    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if diff < min_diff:
            min_diff = diff
            result = [[arr[i - 1], arr[i]]]
        elif diff == min_diff:
            result.append([arr[i - 1], arr[i]])

    return result
print(abs_difference([4, 2, 1, 3]))