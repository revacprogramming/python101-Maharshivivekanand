# Tuples

filename= "dataset/mbox-short.txt"
name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
y=list()
maharshi={}
for line in handle:
    if not line.startswith("From "):
    	continue
    if line.startswith("From "):
        m=line.split()
        a=m[5]
    g=a.split(':')
    g=g[0]
    y.append(g)
    y.sort()
for word in y:
    maharshi[word]=maharshi.get(word,0)+1

for word,s in maharshi.items():
    print(word,s)