# # first-unique-character-in-a-string

# def firstUniqChar(s: str) -> int:
#     dict = {}
#     index = 0

#     for i in s:
#         dict[i] = dict.get(i, 0) + 1  
#         # print(dict)


#     for _ in s:
#         if dict[_] == 1:
#             # print(dict)
#             return index
        
#         # print(_)
#         index += 1

#     return -1

# s = "dddccdbba"

# print(firstUniqChar(s))



def firstUniqChar(s: str) -> int:
    m ={}
    for val in m:
        m[val]+=1 if val in m else (m[val]=1)

    for val in m:
        if (m[val]==1):
            return s.index(val)
    return -1