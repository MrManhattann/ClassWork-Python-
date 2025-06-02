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
# temp=float(input("Введіть поточну температур Цельсіях:"))
# if temp<-10:
#     print("Дуже холодно")
# elif -10=<temp<0:
#     print("Холодно")
# elif 0<temp=<15:
#     print("Прохолодно")
# elif 15>temp=<25:
#     print("Тепло")
# elif temp>25:
#     print("Спекотно")
#Частина 4
#Task1
# figur=int(input("Введіть кількість сторін вашої фігури(min-3,max-8):"))
# if figur==3:
#     print("Трикутник")
# elif figur==4:
#     print("Чотирикутник")
# elif figur==5:
#     print("Пятикутник")
# elif figur==6:
#     print("Шестикутник")
# elif figur==7:
#     print("Семикутник")
# elif figur==8:
#     print("Восьмикутник")
#Task2
# age=int(input("Введіть ваш вік що направити вас в потрібну категорію змаганнь:"))
# if age<=10:
#     print("Ваша категорія змаганнь дитяча)")
# elif 10<age<18:
#     print("Ваша категорія змаганнь юніорська)")
# elif 18<=age<50:
#     print("Ваша категорія змаганнь доросла)")
# elif 50<=age:
#     print("Ваша категорія змаганнь ветеранська)")
#Task3
# clock,minute=map(int,input("Введіть через пробіл яка година і яка хвилина на годинику:").split())
# if 0<=clock<=5 and 0<=minute<60:
#     print("На дворі ніч:(")
# elif 6<=clock<11 and 0<=minute<60:
#     print("На дворі ранок:/")
# elif 12<=clock<17 and 0<=minute<60:
#     print("На дворі день:)")
# elif 18<=clock<23 and 0<=minute<60:
#     print("На дворі вечір:(")
#Task4
# weight=int(input("Введіть вашу вагу:"))
# if weight<=40:
#     print("Ваша категорія ваги легка)")
# elif 40<weight<75:
#     print("Ваша категорія ваги середня)")
# elif 76<=weight<110:
#     print("Ваша категорія ваги важка)")
# elif 110<=weight:
#     print("Ваша категорія ваги суперважка)")
#Task5
# score=int(input("Введіть ваш бал від 0 до 100:"))
# if 0<=score<=59:
#     print("Ваша оцінка F")
# elif 60<=score<=69:
#     print("Ваша оцінка D")
# elif 70<=score<=79:
#     print("Ваша оцінка C")
# elif 80<=score<=89:
#     print("Ваша оцінка B")
# elif 90<=score<=100:
#     print("Ваша оцінка A")
#Task6
# days=int(input("Введіть кількість днів в місяці 30 або 31 або 28/29 якщо це лютий:"))
# if days==30:
#     print("За введеною кількостю днів в 2025 році це може бути один з цих місяців:Січень,Березень,Травень,Липень,Серпень,Жовтень,Грудень")
# elif days==31:
#     print("За введеною кількостю днів в 2025 році це може бути один з цих місяців:Квітень,Червень,Вересень,Листопад")
# elif days==28 or days==29:
#     print("Це Лютий")
# elif days<=28 or days<=29:
#     print("Дана кількість днів є у всіх місяцях!!!!")
#Частина3
#Task1
# number=int(input("\033[92mВведіть номер місяця від 1 до 12:"))
# if number==1 or number==2 or number==12: #number in [1,2,12]
#     print("\033[34mWinter")
# elif 3<=number<=5:
#     print("\033[35mSpring")
# elif 6<=number<=8:
#     print("\033[32mSummer")
# elif 9<=number<=11:
#     print("\033[33mAutumn")
# else:
#     print("\033[30m\033[41mERORR!!!!!!!\033[0m")
#Task2
# score=int(input("Введіть ваш бал від 0 до 100:"))
# if 90<=score<=100:
#     print("Ваша оцінка Відмінно")
# elif 70<=score<=89:
#     print("Ваша оцінка Добре")
# elif 50<=score<=69:
#     print("Ваша оцінка Задовільно")
# elif score<50:
#     print("Ваша оцінка Незадовільно")
#Task3
# age=float(input("\033[101m\033[30mКористувач будь-ласка введи свій стаж в роках:"))
# wage=float(input("\033[102m\033[30mКористувач будь-ласка введіть вашу заробітнью плату:"))
# if 1<=age<3:
#     res=wage-(wage*(1-5/100))
#     print(f"\033[104m\033[30mВаша премія в залежності від вашого стажу={res}грн\033[0m")
# elif 3<=age<5:
#     res=wage-(wage*(1-10/100))
#     print(f"\033[104m\033[30mВаша премія в залежності від вашого стажу={res}грн\033[0m")
# elif age>=5:
#     res=wage-(wage*(1-15/100))
#     print(f"\033[104m\033[30mВаша премія в залежності від вашого стажу={res}грн\033[0m")
# elif age<1:
#     print("Премія не передбачена\033[0m")
#Task4
# number=input("Введіть будь яке число:")
# sum=0
# for digit in number:
#     sum+=int(digit)
# if sum%10==0:
#     print(f"even={sum}")
# else:
#     print(f"odd={sum}")





