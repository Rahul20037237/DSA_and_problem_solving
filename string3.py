import re
name,s="abcdebdde bde".split(" ")
matches = re.findall(rf'{s[0]}(.[^{s[-1]}]+){s[-1]}', name)
print(matches)
for i in s[1:-1]:
    for j in matches:
        if i in j:
            pass
        else:
            matches.remove(j)
a=list(map(len,matches))  
b=matches[a.index(min(a))]
# print('{}{}{}'.format(s[0],b,s[-1]))
import sys
lines=sys.stdin.read
data=lines().split()
print(data)
