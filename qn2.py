def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# Test two_sum function
print("Indices of numbers that add up to target:")
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]

