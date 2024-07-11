def printme(x=""):
    if not x.strip():
        print()
    else:
        print(x)


def sayhello(a):
    print("Helo dear {}".format(a))


PI_VALUE = 3.14

if __name__ == "__main__":

    print("hi")
    printme("hello")
    sayhello("hi")



