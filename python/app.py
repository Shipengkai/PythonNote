
def removeDuplicates(nums):
    i = 0
    while True:
        i += 1
        if i == len(nums):
            break
        if nums[i] == nums[i-1]:
            nums.pop(i)
            i -= 1
    return len(nums), nums


print('start')
print(removeDuplicates([1, 1, 2]))
