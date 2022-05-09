# Functions


def computepay(h, r):
	if h > 40:
		return (40 * r) + (h - 40) * 1.5 * r
	else:
		return h * r


hrs = float(input("Enter hours? "))
rte = float(input("Enter rate per hour? "))

p = computepay(hrs, rte)
print("Pay:", p)
