#Task 1
#Цикл for
# num1=int(input("Number 1:"))
# num2=int(input("Number 2:"))
# for i in range(num1, num2+1):
#     if i%7==0:
#         print(i, end="-")
#Цикл while
# num1=int(input("Number 1:"))
# num2=int(input("Number 2:"))
#
# i=num1
#
# while i<num2+1:
#     if i%7==0:
#         print(i,end="-")
#     i+=1

#Task 2
# num1=int(input("Number 1:"))
# num2=int(input("Number 2:"))
# quantity = 0
# print("\nЧисла за зростанням:")
# for i in range(num1, num2+1):
#     print(i,end=".")
# print("\nЧисла за спаданням:")
# for i in range(num2, num1-1, -1):
#     print(i,end=".")
# print("\nЧисла кратні 7:")
# for i in range(num1, num2+1):
#     if i % 7 == 0:
#         print(i, end="-")
# print("\nКількість чисел, кратних 5:")
# for i in range(num1, num2+1):
#     if i%5==0:
#         quantity += 1
# print(quantity)
#Task 3
# num1=int(input("Number 1:"))
# num2=int(input("Number 2:"))
#
# print("\nАналіз чисел у діапазоні:")
# print("_" * 30)
#
# for i in range(num1,num2+1):
#     if i%3==0 and i%5==0:
#         print(f"{i:>5} -> Fizz Buzz")
#     elif i%3==0:
#         print(f"{i:>5} -> Fizz")
#     elif i%5==0:
#         print(f"{i:>5} -> Buzz")
#     else:
#         print(f"{i:>5} -> {i}")
# print("_" * 30)
#Task 4
# num1=int(input("Start:"))
# num2=int(input("End:"))
# num3=int(input("Step:"))
# choice=input("Choice 1 or 2:")
# if choice=="1":
#     for i in range(num1,num2+1,num3):
#         print(i,end="_")
# elif choice=="2":
#     for i in range(num2,num1-1,-num3):
#         print(i,end="-")
# else:
#     print("Bad choice!!")
#Task 5
# num1=int(input("Start:"))
# num2=int(input("End:"))
#
# dobutok=1
# found=False
# numbers = []
#
# if num1>num2:
#     num1,num2=num2,num1
#     for i in range(num1,num2+1):
#         if i%4==0 and i%6!=0:
#             dobutok *= i
#             found=True
#             numbers.append(i)
#
#     if found:
#         print(f"Добуток чисел, що діляться на 4, но не дільться на 6:Числа які підходять під умову {numbers} --> Добуток цих чисел {dobutok}")
#
#     else:
#         print("У вказаному діапазоні немає чисел, які б ділилися на 4, але не ділилися на 6!!!!")
#
# else:
#     for i in range(num1,num2+1):
#         if i%4==0 and i%6!=0:
#             dobutok *= i
#             found=True
#             numbers.append(i)
#
#     if found:
#         print(f"Добуток чисел, що діляться на 4, но не дільться на 6:Числа які підходять під умову {numbers} --> Добуток цих чисел ({dobutok})")
#
#     else:
#         print("У вказаному діапазоні немає чисел, які б ділилися на 4, але не ділилися на 6!!!!")
#Task 6
# A=int(input("Число А:"))
# N=int(input("Введіть ступінь N для числа А:"))
#Варіант через цикл while
# res=1
# count=0
#
# while count<N:
#     res*=A
#     count+=1
# print(f"Результати числа піднесеного до ступеню буде --> {res}")
#Варіант через цикл for
# res=1
#
# for _ in range(N):
#     res*=A
# print(f"Результати числа піднесеного до ступеню буде --> {res}")