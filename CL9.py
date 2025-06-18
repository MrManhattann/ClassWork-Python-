#Task 0
# x="I'm super Hero!"
# print(x[0],x[1],x[6])
#Task 0.1* for
# x="I'm super Hero!"
# n=len(x)
# for i in range(n):
#     print(x[i], end="")
# for i in x:
#     print(i,end="")
#Task 0.2* while
# x="I'm super Hero!"
# i=0
# while i<n:
#     print(x[i], end="")
#     i+=1
#Частина 1 --> Масиви
#Task 1
#Простий варінт с виведеням кількістю цифр і букв.
# n=input("Введіть рядок цифри,букви--> ")
#
# lit=[]
# nums=[]
#
# for i in n:
#     if 'а' <= i <= 'я' or 'А' <= i <= 'Я' or 'A' <= i <= 'Z' or 'a' <= i <= 'z':
#         lit.append(i)
#     elif '0' <= i <= '9':
#         nums.append(i)
#
# print(len(lit))
# print(len(nums))
#Той самий варінат але через isalpha і isdigit
# n=input("Введіть рядок цифри,букви--> ")
#
# lit=[]
# nums=[]
#
# for i in n:
#     if i.isalpha():
#         lit.append(i)
#     elif i.isdigit():
#         nums.append(i)
# print(f"Кількість літер -->{len(lit)}")
# print(f"Кількість цифр -->{len(nums)}")
#Task 2
# n=input("Введіть рядок--> ")
# symbol=input("Введіть символ який хочете порахувати в рядку--> ")
#
# count=0
#
# for i in n:
#     if i==symbol:
#         count+=1
# print(f"Символ {symbol} зустрічається у рядку {count} разів")
#Task 3
# n=input("Введіть рядок--> ")
# for i in n:
#     print(i)
#Варінт 2
# n=input("Введіть рядок--> ")
# n2=n[::-1]
# print(n2)
#Task 4
# n=input("Введіть рядок--> ")
# word=input("Введіть слово для пошуку --> ")
#
# count=n.count(word)
#
# print(f"Слово --> {word} зустрісчається --> {count} разів")
# n=input("Введіть рядок--> ")
# word=input("Введіть слово для пошуку --> ")
#
# count=0
# words=n.split()
#
# for i in words:
#     if i==word:
#         count+=1
# print(f"Слово --> {word} зустрісчається --> {count} разів")

# word=input("Введіть слово для пошуку --> ")
#Task 5
#Якщо вводиться рядок через пробіл
# n=input("Введіть рядок--> ")
# word=input("Введіть слово для видалення --> ")
# word1=input("Введіть слово для заміни видаленого--> ")
#
# x=n.split()
#
# newlist=[]
#
# for i in x:
#     if i==word:
#         newlist.append(word1)
#     else:
#         newlist.append(i)
# newlist1=' '.join(newlist)
# print(newlist1)
#Якщо вводиться без проьілів
# n=input("Введіть рядок--> ")
# word=input("Введіть слово для видалення --> ")
# word1=input("Введіть слово для заміни видаленого--> ")
#
# newlist=n.replace(word,word1)
# print(newlist)
#Task 6
# n=input("Введіть рядок--> ")
#
# x=n.split()
#
# m=x[0]
#
# for i in x:
#     if len(i)>len(m):
#         m=i
# print(m)