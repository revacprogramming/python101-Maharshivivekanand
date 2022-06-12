def get_cs():
    return input('enter  a string')
def cs_to_dict(cs):
    maharshi = {}
    m=cs.split(";")
    print(m)
    for x in m:
        maggy=x.split("=")
        print(maggy)
        maharshi[maggy[0]]=maggy[1]
    return maharshi
def dict_to_cs(d):
    maggy=""
    sum=0
    for x in d:
        maggy+=x+"="+d[x]+";"

        sum+=1

    return maggy
def main():
    cs = get_ cs()
    d = cs_to_dict(cs) # convert connect string to a dictionary
    print(d)
    cs = dict_to_cs(d)
    print(cs)
if __name__ == '__main__':
    main() in