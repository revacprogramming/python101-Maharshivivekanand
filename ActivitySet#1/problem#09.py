fname = input("Enter file name: ")
fh = open(fname)
maggy= list()
y=fh.read()
lines=y.split()

for line in lines:
    if line not in maggy:
            maggy.append(line)
            
maggy.sort()  
print(maggy)
