'''
CS1113 Problem Sheet 9

Write algorithms which do the tasks specified below. For each one, for an input list of size n,
count how many operations are carried out in the worst case.


(i) takes a list of integers in non-decreasing order, and counts the number of distinct values
(i.e. if a number appears twice, don’t count it twice) (note: non-decreasing means that a number
is never followed by a number that is less than it).


(ii) takes a list of integers, and outputs the list of differences between successive values
(e.g. if the input list is 4,8,2,5,1,9, then the output should be 4,-6,3,-4,8).
You can assume a function add(L, i) which adds value i to the end of a list L.

(iii) checks if an input list of characters is a palindrome
(a palindrome is a word which reads the same backwards as forwards).


(iv) takes a list of integers, and returns the value which appears most often.
'''

#n = [4,8,1,2,9,5]
#n = [4,8,1,2,9,5,3,8,6,4,3,2,7]

def qu1(n):
    return len(set(n))

def qu2(n):
    return [n[i]-n[i-1] for i in range(1,len(n))]

def qu3(n):
    if n == n[::-1]:
        return True
    return False

def qu4(n):
    d = {}
    high = 0
    for i in n:
        d[i] = n.count(i)
        if n.count(i) > high:
            high = n.count(i)
    new = {}
    for key, value in d.items():
        if value not in new:
            new[value] = [key]
        else:
            new[value] += [key]
    return str(new[high])[1:-1]