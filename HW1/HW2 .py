'''Q1'''
numbers = [3,1,5,3,8.5,5]
maxi = numbers[0]

for i in numbers :
    if i > maxi:
        maxi = i
print(maxi)

n=0
while n == len(numbers) :
    if numbers[n] > maxi :
        maxi = numbers[n]

print(maxi)

'''Q2'''
print(" ")
print("q2")
numbers2 = [4,7,1,2,5,3]
numbers_up_3 = []
m=0
for i in numbers2 :
    if i > 3:
        numbers_up_3.append(i)
        m+=1

sum_list=0
if m>0 :
     for n in range(0,m):
        sum_list += numbers_up_3[n]
     print("the list is :" + str(numbers_up_3) + ". the length is : " + str(m) + ". the mean is : " + str(sum_list / m))
else:
    print(0)

'''Q3'''
print("q3")
numbers3 = [4,7,1,2,5,3]
numbers_sum = []

for i in range(2,len(numbers3)):
    a = sum([numbers3[i-2],numbers3[i-1]])
    numbers_sum.append(a)

print(numbers_sum)

'''Q4'''
print("q4")
list1 = ['fnghrb','vubvurir','nhrugbrururu','jijij']
new_list = []

for i in list1:
    a = len(i)
    j = 0
    if a % 3 == 0 :
        while j+3 <= a :
            new_list.append(str(i)[j:j+3])
            j += 3
    if a % 2 == 0 and a % 3 != 0:
        while j+2 <= a :
            new_list.append(str(i)[j:j+2])
            j += 2
    else:
        next
print(new_list)

'''Q5'''
print("q5")

a=str('nhhyhhruggggegbrururu')
b=5
j=0
for i in range(1,len(a)):
    if a[i-1]==a[i] :
        j += 1
        if j == (b-1):
            print("the first substring of length " + str(b) + " is " + a[i]*b)
            break
    else:
        j = 0
        if i == (len(a)-1) :
            print("nothing was found for the string : " + a)

'''Q6'''
print("q6")

mat = [[3,5,4],[1,6,8]]

maxi = mat[0][0]
for i in range(0,len(mat)):
    print(i)
    for j in range(0,len(mat[i])):
        if mat[i][j]>maxi :
            maxi = mat[i][j]


print(maxi)
