#BruteForce
'''
def sortColors(nums):
    leng = len(nums)
    for i in range(leng-1):
        for j in range(leng-i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    print(nums)
'''

# def sortColors(nums):
#     count0 = count1 = count2 = 0
#     print(count0,count1,count2)
#     for i in nums:
#         if nums[i] == 0:
#             count0 += 1
#         if nums[i] == 1:
#             count1 += 1
#         else:
#             count2 += 1

#     print(count0,count1,count2)
#     print(nums)





nums = [2,0,2,1,1,0]
sortColors(nums)