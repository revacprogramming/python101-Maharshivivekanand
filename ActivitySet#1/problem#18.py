fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
h=list()
count = 0
for line in fh:
    if not line.startswith("From "):
        
        continue
    if line.startswith("From"):
        
        y=line.split()
        print(y[1])
        
	count=count+1

print('There were',count,'lines in the file with From as the first word')