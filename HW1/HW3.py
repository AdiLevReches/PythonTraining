'''Q1'''

print("q1")

def flip_float_part(num) :
    num_as_str = str(num)
    num_as_str = num_as_str.split(".")

    print(float(str(num_as_str[1] + "." + num_as_str[0])))

flip_float_part(12.34)

'''Q2'''

print("q2")

def sum_according_to_divisor(num_lst) :
    sum_two = 0
    sum_three = 0
    sum_five = 0
    sum_rest = 0

    for i in num_lst:
        if i%2==0:
            sum_two += i

        elif i%3==0 and i%2!=0:
            sum_three += i

        elif i % 5 == 0 and i % 3 != 0 and i % 2 != 0:
            sum_five += i

        else:
            sum_rest += i

    new_list = [sum_two,sum_three,sum_five,sum_rest]
    print(new_list)

sum_according_to_divisor([6,7,3,4])

'''q3'''
print("q3 part a")

def final_digit_sum(number):
    num_as_str = str(number)
    while len(num_as_str)>1:
        sum_number = 0
        for i in num_as_str:
            sum_number += int(i)
        num_as_str = str(sum_number)
    '''print(num_as_str)'''
    return(num_as_str)

final_digit_sum(888)

print("q3 part b")

def final_digit_sum_string(number):
    new_list = []
    num_as_str = str(number)
    a = len(num_as_str)

    for i in range(0,a-2):
        b = int(num_as_str[i:i+3])
        c = final_digit_sum(b)
        new_list.append(c)
    print(new_list)

final_digit_sum_string(1234)

'''q4'''
print("q4")

def switch_couples_in_lst(lst, couples_lst):
    new_list = lst[:]

    a = len(couples_lst)

    for i in range(0,a):
        num1 = couples_lst[i][0]
        num2 = couples_lst[i][1]

        ind_1 = new_list.index(num1)
        ind_2 = new_list.index(num2)

        save = new_list[ind_1]
        new_list[ind_1] = num2
        new_list[ind_2] = save

    print(new_list)

switch_couples_in_lst([3,5,"adi",7,"yuval",1,2,4,"adi"],[[1,2],[3,4],["adi","yuval"]])


'''q5'''

print("q5")

def add_scalar_to_mat(mat,scalar):
    m = len(mat)
    n = len(mat[0])

    for i in range(0,m):
        for j in range(0,n):
            mat[i][j] = mat[i][j] + scalar

    print(mat)
add_scalar_to_mat([[1,2,3],[4,5,6]],4)


'''q6'''

print("q6")

def reshape_lst(lst,ncols):
    length_list = len(lst)
    new_list = []
    if length_list % ncols != 0 :
        print("invalid row length")
    else:
        for i in range(0,length_list,ncols):
            sub_list = lst[i:i+ncols]
            new_list.append(sub_list)

    print(new_list)

reshape_lst([1,2,3,4,5,6],3)


'''q7'''
print("q7")

def map_names_to_grade(list_keys,list_values):
    new_dict = {}
    j = 0
    for i in list_keys:
        new_dict[i] = list_values[j]
        j = j+1

    print(new_dict)

map_names_to_grade(["adi","liron","yuval"],[12,13,15])