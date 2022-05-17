# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        
        continue
    if line.startswith("X-DSPAM-Confidence:"):
        
		m=line.find('0.')
   	 	maggy=float(line[m:])
    total=total+maggy
    count=count+1
                       
   #print(line)
   #print(maggy)
   #print(total)
   #print(count)
    
print('Average spam confidence:',total/count)
