
def get_csv_matrix(filename):
    list = []
    with open(filename) as fileReader:
        for eachLine in fileReader.readlines():
            num = eachLine.strip().split(',')
            try:
                num = [float(i) for i in num]
                list.append(num)
            except ValueError:
                raise Exception("There is a non float char in matrix")

        length = len(list[0])
        for eachlist in list:
            if length != len(eachlist):
                raise Exception("the length of each row is not the same")
    print(list)

get_csv_matrix("bad.csv")
