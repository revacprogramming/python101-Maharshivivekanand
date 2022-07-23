import math
def anallyse_the_area(x1, y1, x2, y2, x3, y3):
    base = round((sqrt(pow((x2 - x1), 2) + pow(y2 - y1, 2))),1)
    height = round((sqrt(pow(x3 - x1, 2) + pow(y3 - y1, 2))),1)
    print(base, height, base * height)


rectangles_to_be_analysed = int(input("how many rectangles are to be analyzed"))


def rectangle_cordinate_input():
    for x in range(rectangles_to_be_analysed):
        co_rdinates = input("enter x1, y1, x2, y2, x3 and y3, separated by spaces")
        co_rdinates = co_rdinates.split()
        for x in range(6):
          co_rdinates[x] = float(co_rdinates[x])


        anallyse_the_area(co_rdinates[0], co_rdinates[1], co_rdinates[2], co_rdinates[3], co_rdinates[4],co_rdinates[5])


rectangle_cordinate_input()
