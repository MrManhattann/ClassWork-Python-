#task 2.6
# array=list(map(int,input().split()))
# array_new=[]
# for i in array:
#     if i not in array_new:
#         array_new.append(i)
# print(array_new)
# print(*array_new)
#Частина 3
#Task 1
# from random import randrange
#
# numbers=[randrange(-5,20)for _ in range(10)]
#
# nums=[]
#
# for i in numbers:
#     nums.append(int(i))
# print(nums)
#
# s_m=0
# for n in nums:
#     if n<0:
#         s_m+=n
# print(f"Сума всіх від'ємних чисел ={s_m}")
# s_para=0
# for n in nums:
#     if n%2==0:
#         s_para+=n
# print(f"Сума парних чисел ={s_para}")
# s_neparni=0
# for n in nums:
#     if n%2!=0:
#         s_neparni+=n
# print(f"Сума не парних чисел ={s_neparni}")
# S=1
# for n in range(len(nums)):
#     if n%3==0:
#         S*=nums[n]
# print(f"Добуток елементів масиву де індекс кратний 3 ={S}")
# S_min_max=min(nums)*max(nums)
# print(f"Добуток мінімального і максимального числа ={S_min_max}")
# s_start_end=0
# for n in nums:
#     if n in nums[0:9+1]:
#         s_start_end+=n
# print(f"Cума елементів в діапазоні від 1 до останього елементу ={s_start_end}")
#Task 2
# from random import randrange
#
# numbers=[randrange(-5,20)for _ in range(10)]
#
# nums=[]
#
# for i in numbers:
#     nums.append(i)
# print(f"Початковий випадковий спимок ={nums}")
# nums2=[]
# for n in nums:
#     if n%2==0:
#         nums2.append(n)
# print(f"Новий список парних чисел ={nums2}")
# nums3=[n for n in nums if n%2!=0]
# print(f"Новий список не парних чисел ={nums3}")
# nums4=[n for n in nums if n<0]
# print(f"Новий список відємних чисел чисел ={nums4}")
# nums5=[n for n in nums if n>0]
# print(f"Новий список додатніх чисел ={nums5}")
#Task 3
# line=input("Введіть рядки через кому: ")
# lines=line.split(",")
# min_len=lines[0]
# for i in range(len(lines)):
#     if len(lines[i])<len(min_len):
#         min_len=lines[i]
# print(f"Мінімальний рядок по довжені це({min_len})")
#Task 4
# line=input("Введіть рядки через кому: ")
# lit=input("Введіть букву для пошуку і створення нового списку: ")
# lines=line.split(",")
# new_lines=[]
# for i in lines:
#     if i.lower().startswith(lit):
#         new_lines.append(i)
# print(f"Новий список рядків які містять вказану букву:\n(-->{",".join(new_lines)}<--)")
#Task 5
# line=input("Введіть рядки через кому: ").lower()
# lines= line.split(",")
# palindrom=[]
# print(lines)
# for n in lines:
#     j=n.replace(" ","")
#     if j==j[::-1]:
#         palindrom.append(n)
# palindrom=sorted(palindrom, key=len, reverse=True)
#
# print(f"Поліндрови в порядку зменшення довжини\n(-->{",".join(palindrom)}<--)")
#Task 6
numbers=input("Введіть цілі числа через пробіл: ").split()
number=int(input("Введіть число для підрахунків: "))
nums=[]
new_list=[]
for i in numbers:
    nums.append(int(i))
n=len(nums)
for i in range(1,2**n):
    lists=[]
    for j in range(n):
        if (i>>j)&1:
            lists.append(nums[j])
    total=0
    for l in lists:
        total+=l

    if total==number:
        new_list.append(lists)
print(new_list)







