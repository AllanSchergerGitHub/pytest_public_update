
def optional_method(val):
    print("don't do this method during testing")
    x = val
    print("x=", x)
    return x


def mandatory_method(val):
    optional_method(7)
    print("do this during testing")
    y = val
    print("y=", y)
    return y


def main():
    mandatory_method(77)


if __name__ == '__main__':
    main()
