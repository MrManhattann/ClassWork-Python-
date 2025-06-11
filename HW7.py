# A=int(input("A --> "))
# N=int(input("N --> "))
#
# res=1
# count=0
#
# while count<N:
#     res*=A
#     count+=1
# print(f"A в ступені N --> {res}")
# for _ in range(N):
#     res*=A
# print(f"A в ступені N --> {res}")
#Lesson 7
#Частина 2
#Task3
# num1=int(input("length --> "))
# i=0
# while i<num1:
#     print("*",end="")
#     i+=1
#Task4
# num1=int(input("length --> "))
# simbol=input("Choice simbol --> ")
# i=0
# while i<num1:
#     print(simbol,end="")
#     i+=1
#Task5
# num1=int(input("Number 1:"))
# num2=int(input("Number 2:"))
#
# while True:
#
#     choice = input("Виберіть що програма буде робити з введеними числами(1-минимум,2-максимум,3-вихід із програми -->)")
#
#     if choice=="1":
#         res=min(num1,num2)
#         print(f"min--> {res}")
#     elif choice=="2":
#         res=max(num1,num2)
#         print(f"max--> {res}")
#     elif choice=="3":
#         print("Завершення роботи!!!")
#         break
#     else:
#         print("Повернення до вибору!!")
#Task6
# while True:
#     choice=int(input("Оберіть функцію \n1-Додавання двох чисел \n2-Віднімання двох чисел \n3-Ділення двох чисел \n4-Вихід із програми)--> "))
#     if choice==1 or choice==2 or choice==3:
#         num1=int(input("Number 1 --> "))
#         num2=int(input("Number 2 --> "))
#         if choice==1:
#             res=num1+num2
#             print(f"Результат додавання двох чисел --> {res}")
#         elif choice==2:
#             res=num1-num2
#             print(f"Результат віднімання двох чисел --> {res}")
#         elif choice==3:
#             if num2==0:
#                 print("Нануль ділити не можна і нуль не ділиться!!!Введи коректо числа!!!")
#             else:
#                 res=num1/num2
#                 print(f"езультат ділення двох чисел --> {res}")
#     elif choice==4:
#         print("Завершення роботи програми!!!")
#         break
#     else:
#         print("Помилка вибору повернення до вибору!!!")
#Частина 3
#Task1
# num=int(input("Number-->"))
# i=1
# while i<=10:
#     res=num*i
#     print(f"{num}*{i}-->{res}")
#     i += 1
#Task2
# while True:
#     print("Конвертор валюти гривень у обрану валюту:)")
#     choice=int(input("Оберіть в яку валюту будуть конвертуватись ваші гривні \n1-в Долари \n2-в Евро \n3-в Фунти \n0-вихід з програми \n-->"))
#     if choice==1 or choice==2 or choice==3:
#         amount_of_money=float(input("Введіть сум в грн яку потрібно перевести у вибрану валюту --> "))
#         if choice==1:
#             res=amount_of_money*0.0241
#             print(f"{amount_of_money}UAH --> {res:.2f} USD")
#         elif choice==2:
#             res=amount_of_money*0.0211
#             print(f"{amount_of_money}UAH --> {res:.2f} EUR")
#         elif choice==3:
#             res=amount_of_money*0.0186
#             print(f"{amount_of_money}UAH --> {res:.2f} GBP")
#     elif choice==0:
#         print("Вихід із програми")
#         break
#     else:
#         print("Ви обралу опцію якої немає тому оберіть вірну!!!")
#Task3
# start=int(input("Start--> "))
# end=int(input("End--> "))
# while True:
#     num=int(input("Number--> "))
#     if num<start or num>end:
#         print("Число не входить в діапазон!!!")
#     elif start <= num <= end:
#         for i in range(start,end+1):
#             if i==num:
#                 print(f"!{i}!",end=" ")
#
#             else:
#                 print(f"{i}",end=" ")
#         break
#Task4
# N=int(input("Введіть кількість чисел які будете вводити--> "))
# num1=int(input("Введіть число №1 --> "))
# max=num1
# for i in range(N):
#     num=int(input(f"Введіть число №{i+1}--> "))
#     max=num
#     i+=1
#     if num>max:
#         num=max
#     elif num<max:
#         num!=max
# print(num)


