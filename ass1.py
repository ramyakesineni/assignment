#1 Calculate the sum of all numbers from 1 to a given number
# n = int(input('ENTER THE LIMIT :'))
# k = 0
# for i in range(1,n+1):
#     k = k+i
# print(k)

#2 Write a program to print multiplication table of a given number
# n = int(input('ENTER THE NUMBER : '))
# for i in range(1, 11):
#     print(n, 'X', i, '=', n*i)

#3   Display numbers from a list using loop
# k = ['Joey','Pheobe','Rachel','Chandler','Monica','Ross']
# for i in k:
#     print(i)
    

# i = 0
# while i < len(k):
#   print(k[i])
#   i = i + 1

#4  Count the total number of digits in a number
# n = input('ENTER THE NUMBER : ')
# # n=['0','1','2','3','4','5','6','7','8','9','10']
# print(len(n))

#7  Count the total number of digits in a number
# n=['0','1','2','3','4','5','6','7','8','9','10']
# # n.reverse()
# # print(n)


# k = n[::-1]
# print(k)


#8  Display numbers from -10 to -1 using for loop
# for i in range(-10,1,1):
#     print(i,end=',')

#9  Use else block to display a message “Done” after successful execution of for loop
# for i in range(1,10):
#     print(i)
# else:
#     print('DONE...!!')



#10  Write a program to display all prime numbers within a range
# frst = int(input('ENTER YOUR FIRST VALUE :'))
# last = int(input('ENTER YOUR SECOND VALUE :'))
# print('PRIME NUMBERS BETWEEN', frst, "AND", last, "ARE :")
# for val in range(frst ,last):
#   if val > 1:
#     for i in range(2, val):
#       if (val % i) == 0:
#         break
#     else:
#       print(val, end=" ")


#11 Display Fibonacci series up to 10 terms
# limit=int(input('ENTER THE LIMIT :'))
# n1=0
# n2=1
# print(n1)
# print(n2)
# for i in range(2,limit+1):
#     n3=n1+n2
#     print(n3)
#     n1=n2
#     n2=n3