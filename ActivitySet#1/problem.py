import re
a=open('maharshi.txt')
g=list()
m={}
count=0
for line in a:
    line=line.rstrip()
    if re.search('From:',line):

        m=line.split()
        a=m[1]
        print(a)
        count = count + 1
    g.append(a)
#print(g)

for word in g:
    print(word)
    m[word]=m.get(word,0)
print(m)



print(count)