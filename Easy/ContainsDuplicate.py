# It is a 217 in dictionary


# The First method to solve:
map = {}
for i in range(len(nums)):
    if nums[i] in map:
        return True
    map[nums[i]] = nums[i]
return False

# The Second method to solve it:
return not len(set(nums)) == len(nums)
