#Task 0
# def mat_diya(a, b, c):
#    if c=="*":
#       res=a*b
#    elif c=="/":
#       res=a/b
#    elif c=="+":
#       res=a+b
#    elif c=="-":
#       res=a-b
#    print(f"{a}{c}{b}={res}")
# num1,num2=map(int,input("Enter a numbers: ").split())
# symbol=input("Enter a mat symbol: ")
# mat_diya(num1,num2,symbol)
#Task 0.1
# def suma(a, b):
#    res=a+b
#    print(res)
# def dell(a, b):
#    res=a/b
#    print(res)
# def minus(a, b):
#    res=a-b
#    print(res)
# def dobytok(a, b):
#    res=a*b
#    print(res)
# num1,num2=map(int,input("Enter a numbers: ").split())
# suma(num1,num2)
# dell(num1,num2)
# minus(num1,num2)
# dobytok(num1,num2)
#Part 1
#Task 1
# def text():
#    print(f"\033[90m\"Don't let the noise of others' opinions ")
#    print(f"\tdrown out your own inner voice.\"\033[0m")
#    print("\t\t\033[33mSteve Jobs\033[0m")
#
# text()
#Task 2
# def number(start, end):
#    if start>end:
#       start,end=end,start
#    for i in range(start,end):
#       if i%2!=0:
#          print(i,end=",")
# num1,num2=map(int,input("Enter a numbers: ").split())
# number(num1,num2)
#Task 3
#Task 3.1
# def line(l,d,s):
#    if d=="vertical":
#       for _ in range(l):
#          print(s)
#    elif d=="horizontal":
#       print((s+" ")*l)
#    else:
#       print("Incorrect direction")
# length=int(input("Enter a length: "))
# direction=input("vertical or horizontal: ")
# symbol=input("Enter a symbol: ")
# line(length, direction, symbol)
# def line_vertical(length,symbol):
#    i=0
#    while i<length:
#       print(f"{symbol}")
#       i+=1
# def line_gorisont(length,symbol):
#    i=0
#    while i<length:
#       print(f"{symbol}",end="")
#       i+=1
#
# leng=int(input("Length: "))
# sym=input("Symbol: ")
# line_gorisont(leng,sym)
# line_vertical(leng,sym)
#Task 4
# def maximal(l):
#    max_num=l[0]
#    for i in l:
#       if i>max_num:
#          max_num=i
#    print(f"Maximal nuber in seved list: {max_num}")
#
# def get_numbers():
#    nums = []
#    while True:
#       user_input = input("Введи число (або Enter для завершення): ")
#       if not user_input:
#          break
#       nums.append(int(user_input))
#    print(nums)
#    return nums
# nums=get_numbers()
# if nums:
#    maximal(nums)
# else:
#    print("Not list")
#Task 5
# def simple(l):
#    if l<2:
#       return False
#    for i in range(2,int(l**0.5)+1):
#       if l%i==0:
#          return False
#    return True
#
# number=int(input("Enter a number: "))
# if simple(number):
#    print("simple number")
# else:
#    print("not simple number")
#Task 6
# def lucky(l):
#    if len(l)!=6 or not l.isdigit():
#       return False
#    first=int(l[0])
#    second=int(l[1])
#    third=int(l[2])
#    fourth=int(l[3])
#    fifth=int(l[4])
#    six=int(l[5])
#    sum_left=first+second+third
#    sum_right=fourth+fifth+six
#    if sum_left==sum_right:
#       return True
#    else:
#       return False
#
# number=input("Enter a mb lucky numbers: ")
# if lucky(number):
#    print("Its lucky number")
# else:
#    print("Not lucky")
#------------------------------------------------------------------------------------
#Task 6.0
# def lucky(n):
#     first_3=int(n[0]+int(n[1])+int(n[2]))
#     second_3=int(n[3]+int(n[4])+int(n[5]))
#     if first_3==second_3:
#         return True
#
#     return False
#
# num=int(input("Enter a number: "))
# if len(num)==6:
#     res=lucky(num)
#     if res:
#         print("Lucky")
#     else:
#         print("Not lucky")
# else:
#     print("Errror")
#Part 2
#Task 1
# def sum_in_range(a, b):
#     if a>b:
#         a,b=b,a
#     sum_in_range2=1
#     for i in range(a,b+1):
#         sum_in_range2*=i
#     return sum_in_range2
#
# print(sum_in_range(2,15))
# print(sum_in_range(10,2))
#Task 2
# from random import randrange
# def maximum(numbers):
#     if not numbers:
#         return None
#     max_numbers=numbers[0]
#     for i in numbers[1:]:
#         if i>max_numbers:
#             max_numbers=i
#     return max_numbers
# lists=[randrange(-5,20)for _ in range(10)]
# print(lists)
# res=maximum(lists)
# print("Максимальне зі списку: ",res)
#Task 3
# from random import randrange
# def suma(numbers):
#     if not numbers:
#         return None
#     sum_numbers=0
#     for i in numbers:
#         sum_numbers+=i
#     return sum_numbers
# lists=[randrange(-5,20)for _ in range(10)]
# print(lists)
# res=suma(lists)
# print(res)
#Task 4
# from random import randrange
# def nums_counter(numbers):
#     if not numbers:
#         return None
#     count_plus=0
#     count_minus=0
#     count_par=0
#     count_nepar=0
#     for i in numbers:
#         if i%2==0:
#             count_par+=1
#         else:
#             count_nepar+=1
#         if i>0:
#             count_plus+=1
#         else:
#             count_minus+=1
#     return count_par, count_nepar, count_plus, count_minus
#
# lists=[randrange(-5,20)for _ in range(10)]
# print(lists)
# res=nums_counter(lists)
# print("Парних:", res[0])
# print("Непарних:", res[1])
# print("Додатних:", res[2])
# print("Від'ємних:", res[3])
#task 5
# from random import randrange
# def relode_list(numbers):
#     return numbers[::-1]
#
# lists=[randrange(-5,20)for _ in range(10)]
# print("Start list: ",lists)
# res=relode_list(lists)
# print("Revers list: ",res)
#Task 6
# from random import randrange
# def factorial_list(numbers):
#     def factorial(n):
#         if n == 0 or n == 1:
#             return 1
#         result = 1
#         for i in range(2, n+1):
#             result *= i
#         return result
#
#     new_list = []
#     for i in numbers:
#         if i >= 0:
#             new_list.append(factorial(i))
#         else:
#             continue
#     return new_list
#
# lists=[randrange(-5,20)for _ in range(10)]
# print("Start list: ",lists)
# res = factorial_list(lists)
# print("Factorial list: ", res)
#Task 7
# from random import randrange
# def fibonachi(numbers):
#     fibonachi_list=[]
#     for i in numbers:
#         if i<0:
#             continue
#         else:
#             a=0
#             b=1
#             while b<i:
#                     next=a+b
#                     a=b
#                     b=next
#             if a==i or b==i:
#                 fibonachi_list.append(i)
#                 return fibonachi_list
# lists=[randrange(-5,20)for _ in range(10)]
# print("Start list: ",lists)
# res=fibonachi(lists)
# print("List of numbers Fibonachi: ",res)
#Part 3
#Task 1
# def power(num,exponent):
#     if exponent==0:
#         return 1
#     if exponent<0:
#         return 1/power(num,-exponent)
#     return num*power(num,exponent-1)
# print(power(2,3))
# print(power(4,3))
# print(power(6,3))
#Task 2
# def suma(a,b):
#     if a>b:
#         return suma(b,a)
#     if a==b:
#         print(f"suma({a},{b})={a}")
#         return a
#     else:
#         print(f"suma({a},{b})={a}+suma({a + 1},{b})")
#         result=a+suma(a+1,b)
#         print(f"Після обчислення: suma({a}, {b}) = {result}")
#         return result
# a = int(input("Введіть a: "))
# b = int(input("Введіть b: "))
#
# result = suma(a, b)
# print(f"Сума чисел від {a} до {b} дорівнює {result}")

