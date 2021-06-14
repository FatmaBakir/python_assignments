#Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.
#For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.
liste = [6, 1, 3, 3, 3, 6, 6]

def nonrepeater(x):
    for i in x:
        if x.count(i) == 1:
            return i
print(nonrepeater(liste))