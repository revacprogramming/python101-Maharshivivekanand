

def get_cs():
    return input("enter a string")


def cs_to_lot(cs):
    return cs.split()

def lot_to_cs(lot):
    maggy=""

    for x in lot:
      maggy +=" "+x
    return maggy

def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
    main()
