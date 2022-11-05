#1.solve me first

def solveMeFirst(a,b):
    return a+b
    
num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)
#2.simple array sum

#!/bin/python3

import os
import sys

def simpleArraySum(ar):
    result = 0
    for i in ar:
        result = result+i
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()




#3.compare the triplets
#!/bin/python3

import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    score = [0,0]
    for i in range(len(a)):
        if (a[i] > b[i]):
            score[0] = score[0] + 1
        elif(a[i] < b[i]):
            score[1] = score[1] + 1
        else:
            pass
    return score

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()





#4.a very big sum
#!/bin/python3

import os

def aVeryBigSum(ar):
    result = 0
    for i in range(len(ar)):
        result = result + ar[i]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()












#5.diagonal difference
#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    
    primary=0
    secondary=0 
    n = len(arr)
    print(n)
    for i in range(n):
         for j in range(n):
             if i==j:
                 primary = primary + arr[i][j]
             if i==n-j-1:
                 secondary = secondary + arr[i][j]
    return abs(primary-secondary)
                
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


#6.plusminus
#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    plus = 0
    minus = 0
    zero = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            plus = plus + 1
        elif arr[i] < 0:
            minus = minus + 1
        else:
            zero = zero + 1 
    print("{0:.6f}".format(plus/len(arr)))
    print("{0:.6f}".format(minus/len(arr)))
    print("{0:.6f}".format(zero/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)







#7.staircase
#!/bin/python3

import math
import os
import random
import re
import sys

def staircase(n):
   for i in range(1, n + 1):
        print(' ' * (n - i) + '#' * i)

if __name__ == '__main__':
    n = int(input())

    staircase(n)

#8.mini max sum
#!/bin/python3

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    x = sum(map(int,arr))
    print ((x-(max(arr))), (x-(min(arr))))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


#9.birthday cake candles
#!/bin/python3

import math
import os
import random
import collections
import re
import sys

def birthdayCakeCandles(ar):
    return (max(collections.Counter(ar).values()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()







#10.time conversion
#!/bin/python3

import os
import sys

def timeConversion(s):
    #
    # Write your code here.
    #
    print(str(s))
    time = (s.split(":"))
    ampm = time[2][2:4]
    if ampm == "PM":
        if time[0] != "12":
            time[0]=int(int(time[0])+12)
            time[0] = str(time[0])
    elif ampm == "AM":
        if time[0] == "12":
            time[0] = "00"
        
    ntime = ':'.join(time)
    print(str(ntime))
    return str(ntime[:-2])
    
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()


#11.big sorting

t = int(input())
unsorted = []
for _ in range(t):
    unsorted.append(input())
    
unsorted.sort(key=int)
for s in unsorted:
    print(s)

#12.super reduced string
s = input()

i=0
while i<len(s)-1:
    if s[i]==s[i+1]:
        s = s[0:i] + s[i+2:]
        i=0
    else:
        i+=1
print(s if s!="" else "Empty String")

#13.intro to tutorial challenge

import os

def introTutorial(V, arr):
    return arr.index(V)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input())
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result))
    fptr.close()

#14.camelcase
s = input()

c = 1
for i in s:
    if i.isupper():
        c+=1
print(c)

#15.insertion sort part 1
def insertionSort1(n, arr):
    tmp = arr[-1]
    for i in range(n-2, -1, -1):
        if arr[i] > tmp:
            arr[i+1] = arr[i]
            print(' '.join(map(str, arr)))
        else:
            arr[i+1] = tmp
            print(' '.join(map(str, arr)))
            return

    arr[0] = tmp
    print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)





#15.strong password
import os

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    requiredNumber = 1
    requiredLower = 1
    requiredUpper = 1
    requiredSpecial = 1

    for i in password:
        if i in numbers:
            requiredNumber = 0
        elif i in lower_case:
            requiredLower = 0
        elif i in upper_case:
            requiredUpper = 0
        elif i in special_characters:
            requiredSpecial = 0

    ret = requiredNumber + requiredLower + requiredUpper + requiredSpecial

    if len(password) + ret < 6:
        return 6 - len(password)

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer))
    fptr.close()
#16.two characters
import collections
import itertools

n = int(input())
str = input()

max = 0

c = collections.Counter(str)
if(len(c)>1):
    for i in itertools.combinations(c, len(c)-2):
        s = str
        for j in i:
            s = s.replace(j, "")
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                break
            if i==len(s)-2:
                if max<len(s):
                    max = len(s)
print(max)









#17.insertion sort part 2
def insertionSort2(n, arr):
    for i in range(1, n):
        tmp = arr[i]
        j = i-1

        while j >= 0 and arr[j] > tmp:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = tmp

        print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
    
#18.currectness and loop invariant
def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))



#19.caesar cipher
n = int(input())
s = input()
r = int(input())%26

for i in s:
    if i.isupper():
        print(chr(ord(i)+r) if ord(i)<=ord('Z')-r else chr(ord('A')+r-(ord('Z')+1-ord(i))), end="")
    elif i.islower():
        print(chr(ord(i)+r) if ord(i)<=ord('z')-r else chr(ord('a')+r-(ord('z')+1-ord(i))), end="")
    else:
        print(i, end="")













#20.counting sort 1
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    mx = max(arr)
    l = [0 for i in range(100)]
    for a in arr:
        l[a] += 1
    return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()






#21.counting sort part 2

def insertionSort2(n, arr):
    for i in range(1, n):
        tmp = arr[i]
        j = i-1

        while j >= 0 and arr[j] > tmp:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = tmp

        print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)










#22. running time of algorithems

import os

def runningTime(arr):
    ret = 0
    for i in range(1, n):
        tmp = arr[i]
        j = i-1

        while j >= 0 and arr[j] > tmp:
            arr[j+1] = arr[j]
            j -= 1
            ret += 1

        arr[j+1] = tmp

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result))
    fptr.close()






#23.find median
import math
import os
import random
import re
import sys
#import numpy as np
# Complete the findMedian function below.
def findMedian(arr):
    arr.sort()
    if((len(arr)%2)!=0):
        x=len(arr)//2
        return(arr[x])
    else:
        x=arr[len(arr)//2]+arr[(len(arr)//2)+1]
        return x/2
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()






#24. the full counting sort
def countSort(arr):
    n = len(arr)
    ret = [[] for _ in range(n // 2 + 1) ]

    for i in range(n):
        if i < n // 2:
            arr[i][1] = '-'

        ret[int(arr[i][0])].append(arr[i][1])

    ret = [' '.join(i) for i in ret if not len(i) == 0]

    print(' '.join(ret))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)








#25.quicksort1
import os

def quickSort(arr):
    pivot = arr[0]
    left, right = [], []

    for i in arr[1:]:
        if i <pivot:
            left.append(i)
        else:
            right.append(i)

    return left + [pivot] + right

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.close()







