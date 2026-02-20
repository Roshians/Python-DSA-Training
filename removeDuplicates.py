def removeDuplicates(num):
    s = set(num)
    if not(len(num) == len(s)):
        return True
    return False

l1 = [1,2,3,4,1,5]
print(removeDuplicates(l1))

# Using HashMap
def containsDuplicate(nums):
    m = {}
    index = 0
    for i in nums:
        if i in m:
            return True
        else:
            m[i] = index
            index += 1
    return False
        
l2 = [1,2,3,4,5,5]
print(containsDuplicate(l2))