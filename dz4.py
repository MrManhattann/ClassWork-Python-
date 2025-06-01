#Task1
# num1=float(input("Введіть перше число:"))
# num2=float(input("Введіть друге число:"))
# num3=float(input("Введіть третьє число:"))
# choice=input("Виберіть дію із списку(sum-сума,dob-добуток):")
# if choice=="sum":
#     res=num1+num2+num3
#     print(f"Сума введених чисел={res}")
# elif choice=="dob":
#     res=num1*num2*num3
#     print(f"Добуток введених чисел={res}")
#Task2
#Varian1-Якщо вводити їх окремо
# num1=float(input("Введіть перше число:"))
# num2=float(input("Введіть друге число:"))
# num3=float(input("Введіть третьє число:"))
#Variant2-Якщо потрібно економити простір і зменшити трохи код
# num1,num2,num3=map(float,input("Введіть три числа через пробіл:").split())
# choice=input("Виберіть дію із списку(max-максимум,min-мынымум,serd-середньоарифметичне):")
# MAX=num1
# MIN=num1
# if choice=="max":
#     if num2>MAX:
#         MAX=num2
#     if num3>MAX:
#         MAX=num3
#     print(f"MAX={MAX}")
# elif choice=="min":
#     if num2<MIN:
#         MIN=num2
#     if num3<MIN:
#         MIN=num3
#     print(f"MIN={MIN}")
# elif choice=="serd":
#     res=(num1+num2+num3)/3
#     print(f"Середньоарифметичне трьох чисел={res}")
#Task3
# grade=int(input("Введіть отриману оцінку від 1 до 5:"))
# if grade==1:
#     print("Дуже погано")
# elif grade==2:
#     print("Погано")
# elif grade==3:
#     print("Задовільно")
# elif grade==4:
#     print("Добре")
# elif grade==5:
#     print("Відмінно")
# else:
#     print("Ви ввели невірну оцінку переконайтесь що введена оцінка є коректною!!!")
#Task4
# distance=float(input("\033[94mВведіть відстань у метрах:"))
# choice=input("\033[96mВиберіть із запропонованого в що перевести метри(mi-милі,in-дюйми,yd-ярди,all-одразу в усі і вивести,kmcm-в кілометри і сантиметри і вивести обидва значення):")
# if choice=="mi":
#     res=distance*0.000621371
#     print(f"\033[92mВведені метри в милях={res}mi")
# elif choice=="yd":
#     res=distance*1.09361
#     print(f"\033[95mВведені метри в ярдах={res}yd")
# elif choice=="in":
#     res=distance*39.3701
#     print(f"\033[91mВведені метри в дюймах={res}in")
# elif choice=="all":
#     res1=distance*0.000621371
#     res2=distance*1.09361
#     res3=distance*39.3701
#     print(f"\033[92mВведені метри в милях={res1}mi")
#     print(f"\033[95mВведені метри в ярдах={res2}yd")
#     print(f"\033[91mВведені метри в дюймах={res3}in")
# elif choice=="kmcm":
#     res1=distance*0.001
#     res2=distance*100
#     print(f"\033[97mВведені метри в кілометрах={res1}km")
#     print(f"\033[97mВведені метри в сантиметрах={res2}cm")
# else:
#     print("\033[91mТи точно обрав функцію якої немає у списку подумай а потім обери вірну!!!!")
#Task5 Я знаю що ми її робили але я подума що для практики можна знову виконати але просто способом який ми проходили по цій темі)Зробив більше для себе шоб закріпити пройдене це ж саме відноситься і до Task6)
# cost=float(input("\033[93mВведіть загальну суму рахунку(грн):"))
# persons=int(input("\033[92mКількість осіб які ділять між собою рахунок:"))
# tips=int(input("\033[94mВведіть процент чайових рестронану в якому знаходяться дані персони:"))
# tip=tips/100
# choice=input("\033[91mОберіть що потрібно порахувати і вивести(tea-сума чайових від загального рахунку,tot-загальна сума з чайовими,onepers-скільки кожна людина повина внести в загальний рахунок):")
# if choice=="tea":
#     res=cost*tip
#     print(f"\033[95mСума чайових від загальної суми={res}грн")
# elif choice=="tot":
#     res=cost+(cost*tip)
#     print(f"\033[95mЗагальна сума рахунку з чайовими={res}грн")
# elif choice=="onepers":
#     res=(cost+(cost*tip))/persons
#     print(f"\033[95mСума яку повинна заплатити кожна персона={res}грн")
#Task6
# rental=float(input("\033[92mВартість оренди автомобіля за день в грн:"))
# days=int(input("\033[92mКількість днів на які береться орендований автомобіль:"))
# deposit=float(input("\033[92mСума застави за орендований автомобіль:"))
# choice=input("\033[93mОберіть варінт із списку\n\033[94mtot-загальну вартість оренди (з урахуванням застави),\n\033[95mmtot-Загальна вартість оренди (без застави),\n\033[94mcost-Сума, яку користувач фактично заплатить після повернення авто (заставу повернуто),\n\033[95mtest-Вартість оренди за один день (перевірка):")
# Загальна вартість оренди (без застави):
# RentalCost=rental*days
# Загальна сума до оплати (з урахуванням застави):
# TotalPayment=RentalCost+deposit
# Сума, яку користувач фактично заплатить після повернення авто (заставу повернуто):
# FinalCost=RentalCost
# Вартість оренди за один день (перевірка):
# DailyCost=RentalCost/days
# if choice=="tot":
#     res=RentalCost+deposit
#     print(f"\033[91mЗагальна сума до оплати (з урахуванням застави)={res}грн")
# elif choice=="mtot":
#     res=rental*days
#     print(f"\033[91mЗагальна вартість оренди (без застави)={res}грн")
# elif choice=="cost":
#     FinalCost=RentalCost
#     print(f"\033[91mСума, яку користувач фактично заплатить після повернення авто (заставу повернуто)={FinalCost}грн")
# elif choice=="test":
#     DailyCost=RentalCost/days
#     print(f"\033[91mВартість оренди за один день (перевірка)={DailyCost}грн")

