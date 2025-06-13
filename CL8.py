#Task 0 Типу д з простими числами
# num=int(input("number --> "))
# k=0
# for i in range(1,num+1,1):
#     if num%i==0:
#         k=k+1
# if k==2:
#     print("prime")
# else:
#     print("not")
#2
# num=int(input("number --> "))
# k=False
# for i in range(2,int(num**0.5)+1,1):
#     if num%i==0:
#         k=True
#         break
# if k==False:
#     print("prime")
# else:
#     print("not")
#While
# num=int(input("number --> "))
# k=False
# i=2
# while i*i<=num:
#     if (num%i==0):
#         k=True
#         break
#     if i!=2:
#         i=i+2
#     else:
#         i=i+2
# if (k==False):
#     print("prime")
# else:
#     print("not")
#Task 5 in home work
# while True:
#     num=int(input("Введіть число --> "))
#     if num<=1:
#         print("Число не може бути менше 1 або дорівнювати йому!!!!")
#         break
#
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             print(f"Число {num} не є простим")
#             break
#     else:
#         print(f"Число {num} є простим")
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
# max_num=None
# for i in range(N):
#     num=int(input(f"Введіть число {i+1}--> "))
#     if max_num is None or num>max_num:
#         max_num=num
# print(f"Максимум із введених чисел --> {max_num}")
#Task 5
# import random
# import time
#
# secret=random.randint(1,500)
# start_time=time.time()
# attempts=0
#
# while True:
#     num=int(input("Спробуйте вгадати число або введіть 0 для завершення --> "))
#
#     if num==0:
#         print(f"Ви здалися! Загадане число --> {secret}")
#         break
#     attempts+=1
#
#     if num<secret:
#         print("Загадане число більше)")
#     elif num>secret:
#         print("Загадане число менше)")
#     else:
#         print("Вітаю ви вгадали загадане число")
#         break
# end_time=time.time()
# duration = end_time - start_time
#
# print(f"Ви зробили {attempts} спроб)")
# print(f"Час {duration:.2f} секунд ")
#Task 6
# while True:
#     print("\nМеню --> ")
#     print("1-Побудувати прямокутник ")
#     print("2-Побудувати квадрат ")
#     print("0-Вихід з програми ")
#
#     choice=input("Ваш вибір --> ")
#
#     if choice=="1":
#         h=int(input("Введіть висоту прямокутника --> "))
#         m=int(input("Введіть штрину прямокутника --> "))
#         symbol=input("Введіть символ для побудови --> ")
#         for i in range(1,h+1):
#             print(symbol*m)
#     elif choice=="2":
#         a=int(input("Введіть сторону квадрату --> "))
#         symbol=input("Введіть символ --> ")
#         for i in range(1,a+1):
#             print(symbol*a)
#     elif choice=="0":
#         print("Вихід з програми!!!")
#         break
#     else:
#         print("Не вірний вибір з меню!!!")
#Частина 4
#Task 1
# h=int(input("Введіть висоту прямокутника --> "))
# m=int(input("Введіть штрину прямокутника --> "))
# symbol=input("Введіть символ для побудови --> ")
# for i in range(1,h+1):
#     print(symbol*m)
#Task 2
#Зроблено в частині 3 завдання 6)
#Task 3
# a=int(input("Введіть сторону квадрата --> "))
# symbol=input("Введіть символ яким будете малювати --> ")
#
# if a<2:
#     print("Квадрат не буде пустотілий")
# else:
#     for i in range(a):
#         if i==0 or i==a-1:
#             print(symbol*a)
#         else:
#             print(symbol+' '*(a-2)+symbol)
#Task 4
# h=int(input("Введіть висоту прямокутника --> "))
# m=int(input("Введіть штрину прямокутника --> "))
# symbol=input("Введіть символ для побудови --> ")
# if h<2 or m<2:
#     print("Не буде пустотілим!!!")
# else:
#     for i in range(h):
#         if i==0 or i==h-1:
#             print(symbol*m)
#         else:
#             print(symbol+' '*(m-2)+symbol)
#Task 5
# h=int(input("Введіть висоту трикутника --> "))
# symbol=input("Введіть символ для побудови --> ")
#
# for i in range(1,h+1):
#     print(symbol*i)
#Task 6
# h=int(input("Введіть висоту трикутника --> "))
# symbol=input("Введіть символ для побудови --> ")
#
# for i in range(h):
#     p=' '*(h-i-1)
#     s=symbol*(2*i+1)
#     print(p+s)