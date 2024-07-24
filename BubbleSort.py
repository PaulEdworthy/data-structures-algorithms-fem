nums = [5, 2, 9, 0, 7]
l = len(nums)

for i in range(l):
    for j in range(l - 1 - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(nums)