'''q4'''
print("q4")


def find_word_in_file(word,filename):
    row_num = 1
    col_num = 1

    with open(filename) as fileReader:
        for eachLine in fileReader.readlines():
            list = eachLine.strip().replace(",","").replace(".","").split(' ')
            print(list)
            for i in list:
                i = i.lower()
                if i ==word:
                    return (row_num,col_num)
                col_num +=1
            row_num +=1

print(find_word_in_file("queens","demo4.txt"))
