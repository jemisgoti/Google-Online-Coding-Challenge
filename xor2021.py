"""we have array and some queries which are of 2 types :

Type 1: Insert the given element into the array
 Type 2: XOR all the elements present in the array with the given element.
Input format:

An integer Q which represent the count of queries that are going to be asked
Q lines having two integers n and m
n represents the type of operation i.e 1 or 2
m represents the element that will be used to do operation according to the given type of operation.
Output format: Print the final array after all the given queries in sorted order.

Constraints

1<=Q<=107 
n = 1 or 2
1<=m<=109 
Sample Input:

6
1   3
1   5 
2   5
1   6
1   7
2   6
Sample Output:

0   0   1   6"""

l=list()
for i in range(int(input())):
    n,m=map(int,input().split())
    if n==1:
       a=[m]
       l=a+l
    elif n==2:
        for j in range(len(l)):
            l[j]=l[j] ^ m
print(l)
