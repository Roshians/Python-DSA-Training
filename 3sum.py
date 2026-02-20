def threeSum(nums: List[int]):
    nums.sort()
    res = []

    for i in nums:
        j = i+1
        k = len(nums) - 1
        