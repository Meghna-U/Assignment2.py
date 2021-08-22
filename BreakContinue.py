#break in while
print("Break in while")
i=10
while i>=0:
    if i==7:
        break
    print(i)
    i-=1
#continue in while
print("Continue in while")
i=10
while i>=0:
    i-=1
    if i==7:
        continue
    print(i)
#break in for
print("Break in for")
s="HelloEveryone"
for i in s:
    if i=='E':
        break
    print(i)
#continue in for
print("Continue in for")
for i in s:
    if i=='E':
        continue
    print(i)
