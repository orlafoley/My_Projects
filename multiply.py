def multiply(filename):
    filein = open(filename,'r')
    lines = filein.readlines()
    sublist = []
    for line in lines:
        line = line.strip('\n').split(' x ')
        sublist += [line]
    answers = []
    for pair in sublist:
        answers += [int(pair[0]) * int(pair[1])]
    return answers

'''
Example of input:
8 x 45
3 x 36
22 x 22
8 x 8
13 x 2
24 x 17
6 x 86
5 x 73
58 x 9
19 x 22
6 x 43
64 x 9
24 x 16
28 x 13
7 x 64
7 x 65
28 x 3
75 x 4
26 x 18
5 x 84

Example of output:
[360, 108, 484, 64, 26, 408, 516, 365, 522, 418, 258, 576, 384, 364, 448, 455, 84, 300, 468, 420]
'''

#print(multiply('numbers.txt'))