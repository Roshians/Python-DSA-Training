def areAlmostEqual(s1, s2):
    count = 0
    lst = []

    for i in range(len(s2)):
        if s2[i] == s1[i]:
            continue
        else:
            count += 1
            lst.append(i)
            print(lst, count, i)

    if count != 2:
        return False
    elif s1[lst[0]] == s2[lst[1]] and s1[lst[1]] == s2[lst[0]]:
        return True
    else:
        return False

    


s1 = "bank"
s2 = "kanb"
print(areAlmostEqual(s1,s2))