#lists
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

maharshi = open(fname)
h=list()
count = 0
for line in maharshi:
    if not line.startswith("From "):
        
        continue
    if line.startswith("From "):
        #print(m)
        maggy=line.split()
        print(maggy[1])
        
	count=count+1

print('There were',count,'lines in the file with From as the first word')
