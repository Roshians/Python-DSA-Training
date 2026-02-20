# def search(nums, target) -> int:
#     for i in range(len(nums)):
#         if nums[i] == target:
#             return i
#     return -1


def search(nums, target) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid  = left + (right - left) //2
        if nums[mid] == target:
            return mid
        elif nums [mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


n = [-1,0,3,5,9,12]
t = -1

n2 = [-1,0,3,5,9,12]
t2 = 2
print(search(n,t))