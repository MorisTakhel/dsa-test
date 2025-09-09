def rotateList(lst, count):
    while count:
        lst.append(lst.pop(0))
        count -= 1
    return lst

print(rotateList([1,2,3,4,5,6,7,8], 4))