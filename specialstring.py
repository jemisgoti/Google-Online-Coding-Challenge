"""Google’s Online Challenge for 2021 Intern (India)
The coding test was held on HackerEarth, it consists of 2 questions one was easy and the other one was a little tricky. We had 60 minutes to solve these questions. I solved both questions. So, the questions were like this:

Question 1: Unspecified Words

Problem Statement: There are N words in a dictionary such that each word is of fixed length M and consists only of lowercase English letters, that is (‘a’, ‘b’, ‘c’, ………’z’).



A query word is denoted by Q.  The length of a query word is M. These words contain lowercase English letters but at some places instead of a letter between ‘a’, ‘b’……’z’ there is ‘?’. Refer to the Sample Input section to understand this case.

A match count of Q, denoted by match_count(Q), is the count of words that are in the dictionary and contain the same English letters(excluding a letter that can be in the position of ‘?’) in the same position as the letters are there in the query word  Q. In other words, a word in the dictionary can contain any letters at the position of ‘?’ but the remaining alphabets must match with the query word.

You are given a query word Q and you have required top compute match_count.

Input format:

The first line contains two space-separated integers N and M denoting the number of words in the dictionary and length of each word respectively
The next N lines contain one word each from the dictionary.
The next line contains an integer Q  denoting the number of query words for which you have to compute match_count,
The next Q lines contain one query word each.
Output format: For each query word print  match_count  for a specific word in a new line."""




import re
n,m=map(int,input().split())
l=list()
for i in range(n):
  l.append(input())
qn=int(input())
q=list()
for i in range(qn):
  q.append(input())
for k in range(qn):
  rgx="^"+q[k].replace('?','[a-z]{1}')+"$"
  r=re.compile(rgx)
  nl = list(filter(r.match, l)) # Read Note
  print(len(nl))
  #print(q[k].replace('?','*'))
