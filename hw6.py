#Task1
# num1=int(input("Number 1:"))
# num2=int(input("Number 2:"))
# x=num1+1
# while x<num2:
#     print(x,end="-")
#     x+=1
#Task2
# num1 = int(input("Number 1: "))
# num2 = int(input("Number 2: "))
# x = num1 + 1
# while x < num2:
#     if x % 2 != 0:
#         print(x, end="-")
#     x += 1
#Task3
# num1=int(input("Number 1:"))
# num2=int(input("Number 2:"))
# x=num2-1
# while x>num1:
#     if x%2==0:
#         print(x, end="-")
#     x-=1
#Task4
# num1=int(input("Number 1:"))
# num2=int(input("Number 2:"))
# choice=input("Choice 1 or 2:")
# if choice=="1":
#     x=num2-1
#     while x>num1:
#         print(x, end="-")
#         x-=1
# elif choice=="2":
#     x=num1+1
#     while x<num2:
#         print(x, end="-")
#         x += 1
#Task5
# num1=int(input("Number 1:"))
# num2=int(input("Number 2:"))
# if num1>num2:
#     num1,num2=num2,num1
#     for x in range(num1,num2):
#         if x%2==0:
#             x+=1
#             print(x,end="-")
# else:
#     for x in range(num1,num2):
#         if x%2==0:
#             x+=1
#             print(x,end="-")
#Task6
# num1=int(input("Number 1:"))
# num2=int(input("Number 2:"))
# if num1>num2:
#     num1,num2=num2,num1
#     for x in range(num1,num2):
#         if x%2==0:
#             print(x,end="-")
#     for y in range(num2 - 1, num1, -1):
#         if y % 2 != 0:
#             print(y, end="-")
#             y -= 1
# else:
#     for x in range(num1, num2):
#         if x % 2 == 0:
#             print(x, end="-")
#     for y in range(num2-1, num1,-1):
#         if y % 2 != 0:
#             print(y, end="-")
#             y -= 1
#Частина 2
#Task1
# num1=int(input("Number 1:"))
# num2=int(input("Number 2:"))
# x=num1+1
# sum=0
# while x<num2:
#     sum+=x
#     x += 1
# print(f"Сума чисел в введеному діапазоні={sum}")
#Task2
# num1=int(input("Number 1:"))
# fact=1
# for x in range(1,num1+1):
#     fact *=x
# print(f"{num1}!={fact}")
#Task3
# num=int(input("Number:"))
# x="*"


