#Task 1
# numbers=input("Введіть цілі числа через пробіл: ").split()
# nums=[]
# count=0
# count1=0
# for i in numbers:
#     nums.append(int(i))
# for n in nums:
#     if n%2==0:
#         count+=1
#     else:
#         count1+=1
# print(f"Кількість парних чисел=({count})і кількість не парних чисел=({count1})")
#Task 2
# numbers=input("Введіть цілі числа через пробіл: ").split()
# nums=[]
# for i in numbers:
#     nums.append(int(i))
#Якщо робити через скорочений варіант то можна просто використати функцію макс і мін.
# print(f"{min(nums)}and{max(nums)}")
#Другий варіант все вручну
# min_num=nums[0]
# max_num=nums[0]
# for n in nums[1:]:
#     if n<min_num:
#         min_num=n
#     if n>max_num:
#         max_num=n
#
# print(f"Мінімальне число:{min_num}\nМаксимальне число:{max_num}")
#Task 3
# from random import randrange
# numbers=[randrange(-5,20)for _ in range(10)]
# nums=[]
# for i in numbers:
#     nums.append(int(i))
# print(f"Випадковий створений масив в межах -5 до 20      -->{nums}<--")
#
# min_positive=None
# max_negative=None
# positive_count=0
# negative_count=0
# nul_count=0
#
# for i in nums:
#     if i>0:
#         positive_count+=1
#         if min_positive is None or i<min_positive:
#             min_positive=i
#     elif i<0:
#         negative_count+=1
#         if max_negative is None or i>max_negative:
#             max_negative=i
#     else:
#         nul_count+=1
#
# print(f"Мінімальний додатний елемент: {min_positive if min_positive is not None else 'Немає'}")
# print(f"Максимальний від’ємний елемент: {max_negative if max_negative is not None else 'Немає'}")
# print(f"Кількість додатних елементів: {positive_count}")
# print(f"Кількість від’ємних елементів: {negative_count}")
# print(f"Кількість нулів: {nul_count}")
#Task 4
# from random import randrange
# numbers=[randrange(-5,20)for _ in range(10)]
# nums=[]
# for i in numbers:
#     nums.append(int(i))
# print(f"Випадковий створений масив в межах -5 до 20      -->{nums}<--")
# number=int(input("Введіть число для порівняння: "))
# new_lists=[]
# for i in nums:
#     if i>number:
#         new_lists.append(i)
# print(f"Масив після видалення елементів менших за {number} --> {new_lists}")
#Task 5
# expression=input("Введіть арифметичний вираз схожий на (a+b): ")
# for i in "+-/*":
#     if i in expression:
#         task=expression.split(i)
#         if len(task)==2:
#             a=int(task[0])
#             b=int(task[1])
#             if i=="+":
#                 res=a+b
#             elif i=="-":
#                 res=a-b
#             elif i == "*":
#                 res=a*b
#             elif i=="/":
#                 res=a/b if b!=0 else print("Ділення на нуль неможливе!!!")
#             break
# else:
#     print("Введенно не коректно!!!")
# print(f"Результат введеного виразу = {res}")
#Task 6
# from random import randrange
# numbers=[randrange(-5,20)for _ in range(10)]
# nums=[]
# for i in numbers:
#     nums.append(int(i))
# print(f"Випадковий створений масив в межах -5 до 20      -->{nums}<--")
# negativ_nams=[i for i,n in enumerate(nums) if n<0]
# positive_nums=sorted([n for n in nums if n>=0])
# res=[]
# positive_nums_index=0
#
# for i in range(len(nums)):
#     if i in negativ_nams:
#         res.append(nums[i])
#     else:
#         res.append(positive_nums[positive_nums_index])
#         positive_nums_index+=1
# print(f"Відсортований список (від’ємні на місці): --> {res}")