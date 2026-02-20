def groupAnagrams(strs):
    dic = {}
    for i in strs:
        key = ''.join(sorted(i))
        if key in dic:
            dic[key].append(i)
        else:
            dic[key] = [i]
    return list(dic.values())



strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
