# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def files():
    # change 'w' or 'r' or 'a', according to the action you want
    f = open("infile.txt", 'r')

    """
    # will not work twice because it moves the seek 
    print(f.readlines())
    print(f.readlines())
    """

    """
    # using readlines
    for line in f.readlines():
        print(line)
    """

    """"
    # using readline
    line = f.readline()
    while line != "":
        print(line)
        line = f.readline()
    """

    """
    # will never end because we move the seek to the beginning of the file
    for line in f:
        print(line)
        f.seek(0)
    """

    # write to the file
    f.write("\n\n\nLev")

    f.close()


def exceptions():
    liron = [1, 2]
    print("Liron!")
    while True:
        try:
            f = open("infile.txt", 'r')
            x = 1
            y = 0
            if y == 0:
                raise ZeroDivisionError("hahahaha")
            x/y
        except FileNotFoundError:
            print("File not found")
            break
        except Exception:
            print("Exception!")
        else:
            print("No exception")
        break

        try:
            # stuff on f
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))
            print("result: " + str(first/second))
        except ValueError:
            print("I asked for a NUMBER!")
        # except ZeroDivisionError:
        #    print("Cant devide by 0!")
        finally:
            print("I Love Adi and Lironosh")
            f.close()
    print("Adi!")


def liron():
    try:
        adi()
    except ValueError as err:
        print(len(err.args))


def adi():
    print(solve(1, 1, 2))
    print("Go Adi!")
    print(solve(0, 1, 2))


def solve(a, b, c):
    if a == 0:
        raise ValueError("a can't be 0", "wfe", 4)
    return a+b+c

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # files()
    #exceptions()
    liron()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
