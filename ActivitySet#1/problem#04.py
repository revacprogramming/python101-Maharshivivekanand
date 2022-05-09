# Conditional Execution

hours=input("enter a hours:")
rate=input("enter a rate:")
h=int(hours)
r=float(rate)

if h>40:
	print((40*r)+(h-40)*1.5*r)
else:
	print(h*r)

