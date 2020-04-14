# --连接两个list
nums1 = [1, 2, 3]
nums2 = [10, 20, 30]
print('start', nums1)
# slice
nums1[1:2] = nums2
print('slice', nums1)
# .extend
nums3 = [6, 6, 6]
nums1.extend(nums3)
print('.extend', nums1)
