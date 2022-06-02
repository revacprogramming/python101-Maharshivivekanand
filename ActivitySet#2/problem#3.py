

def get_cs():
    m=input("enter a string")
    return m


def cs_to_lot(cs):
    a=cs.split()
    return a


def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()
