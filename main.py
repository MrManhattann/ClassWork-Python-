#Task0
# num1=float(input("Введіть перше число:"))
# num2=float(input("Введіть друге число:"))
# num3=float(input("Введіть третьє число:"))
# num4=float(input("Введіть четверте число:"))
# num5=float(input("Введіть пяте число:"))
# num1,num2,num3,num4,num5=map(float,input("Введіть пять чисел:").split())
# MIN=num1
# if num2<MIN:
#     MIN = num2
# if num3<MIN:
#     MIN = num3
# if num4<MIN:
#     MIN = num4
# if num5<MIN:
#     MIN = num5
# print(f"MIN={MIN}")
# a=float(input("Fist number:"))
# s=input("Simbol:")
# b=int(input("Secon number:"))
# res=float(a)+float(b)
# a=float(a)
# b=float(b)
# res=a+b
# if s == "+" :
#     res=a+b
# elif s=="-":
#     res=a-b
# elif s == "*":
#     res=a*b
# elif s == "/":
#     res=a/b
# elif s == "//":
#     res=a//b
# elif s == "%":
#     res=a%b
# else: res="EROR"
# print(res)
#Task1
# number=float(input("Введіть число:"))
# if number%2==0:
#     number="Even number"
# elif number%2:
#     number="Odd number"
# print(number)
#Task2
# number=float(input("Введіть число:"))
# if number%7==0:
#     number="Number is multiple 7"
# elif number%7:
#     number="Number is not multiple 7"
# print(number)
#Task3
# num1=float(input("First number:"))
# num2=float(input("Second number:"))
# if (num1>num2):
#     print("Max1",num1)
# else:
#     print("Max2", num2)
#Task4
# num1=float(input("First number:"))
# num2=float(input("Second number:"))
# if (num1<num2):
#     print("Min1",num1)
# else:
#     print("Min2", num2)
#Task5
# num1=float(input("Fist number:"))
# articl=input("Виберіть дію +,-,* або ser:")
# num2=float(input("Secon number:"))
# if articl == "+" :
#     res=num1+num2
# elif articl=="-":
#     res=num1-num2
# elif articl == "*":
#     res=num1*num2
# else: res=(num1+num2)/2
# print(res)
#Task6
# num1=float(input("Введіть суму в доларах:"))
# articl=input("Виберіть валюту на вибір із(EUR(евро),GBP(фунти),JPY(єни)):")
# num2=float(input("Ведіть поточний курс вибраної валюти:"))
# if articl=="EUR":
#     res=num1*num2
#     print(f"EUR={res}")
# elif articl=="GBP":
#     res=num1*num2
#     print(f"GBP={res}")
# elif articl=="JPY":
#     res=num1*num2
#     print(f"JPY={res}")
#Part2
#Task1
# time=float(input("Час який пройшов починаючи з 00:00|"))
# timelist=input("Виберіть у чому показати скільки лишилось до 24:00,на вибір(s-секунди,m-хвилини,g-години):")
# if timelist=="s":
#     res=86400-time
#     print(f"Кількість секунд які залишились до 24:00={res}")
# elif timelist=="m":
#     res=(86400-time)/60
#     print(f"Кількість хвилин які залишились до 24:00={res}")
# elif timelist=="g":
#     res=((86400-time)/60)/60
#     print(f"Кількість годин які залишились до 24:00={res}")
#Task2
# D=float(input("Введіть діаметр кола:"))
# formula=input("Виберіть що порахувати-(S-площа,P-периметр):")
# p=3.14
# r=D/2
# if formula=="S":
#     res=p*r**2
#     print(f"Площа кола={res}")
# elif formula=="P":
#     res=p*D
#     print(f"Периметр кола={res}")
#Task3
# cost=float(input("Ведіть вартість однієї ігрової приставки:"))
# quantity=float(input("Введіть кількість взятих приставок:"))
# discount=float(input("Введіть знижку на приставку:"))
# choice=input("Виберіть що порахувати(S-Загальна сума замовленя з знижкою,V-вартість однієї приставки зі знижкою):")
# d=(1-20/100)
# if choice=="S":
#     res=(cost*quantity)*d
#     print(f"Загальна вартість приставок зі знижкою={res}")
# elif choice=="V":
#     res=cost*d
#     print(f"Вартість однієї приставки зі знижкою={res}")
#Task4
# SGB=float(input("Введіть розмір файлу в гігабайтах:"))
# VBPS=float(input("Введіть швидкість інтернету в бітах за секунду:"))
# timelist=input("Виберіть у яких часових одиницях порахувати скільки буде завантажуватись(s-секунди,m-хвилини,g-години):")
# SBITS=SGB*1073741824*8
# timesec=SBITS/VBPS
# if timelist=="s":
#     res=timesec
#     print(f"Час завантаження в секундах={res}sec")
# elif timelist=="m":
#     res=timesec/60
#     print(f"Час завантаження в хвилинах={res}minute")
# elif timelist=="g":
#     res=timesec/3600
#     print(f"Час завантаження в годинах={res}hours")
#Task5
# hours=int(input("Ведіть яка зараз година:"))
# if 0<=hours<6:
#     print("Good Night")
# elif 6<=hours<13:
#     print("Good Morning")
# elif 13<=hours<17:
#     print("Good Day")
# elif 17<=hours<24:
#     print("Good Evening")
# else:
#     print("ERROR")
#Task6
# не доробив

