#Task 0
# string=input("Enter a string: ")
# word_search=input("Enter a word for search: ")
# word_change=input("Enter the woed to replace: ")
# array_words=string.split()
# for i in range(len(array_words)):
#     if array_words[i]==word_search:
#         array_words[i]=word_change
# print(array_words)
#Task 2.1
#Спосіб 1
# array=[1,1,2,4,6,8,3]
# s=0
# for i in range(len(array)):
#     s+=array[i]
# print(s)
# print(s/len(array))
#Спосіб 2
# array=[1,1,2,4,6,8,3]
# s=0
# n=len(array)
# for i in range(n):
#     s += array[i]
# print(s)
# avg=s/n
# print(avg)
#Частина 2
#Task 1
# numbers=input("Введіть цілі числа через пробіл: ").split()
# nums=[]
# for i in numbers:
#     nums.append(int(i))
# s=0
# for j in nums:
#     s+=j
# avg=s/len(nums)
# print(f"Сума чисел дорівнює={s}")
# print(f"Середнє арефметичне={avg}")
#Task 2
# numbers=input("Введіть цілі числа через пробіл: ").split()
# search=input("Введіть число для пошуку в масиві: ")
# nums=[]
# for i in numbers:
#     nums.append(i)
# count=0
# for n in nums:
#     if n==search:
#         count+=1
# print(f"Число--> ({search}) зустрічається ({count})рази")
#Task 3
# numbers=input("Введіть цілі числа через пробіл: ").split()
# nums=[]
# for i in numbers:
#     nums.append(int(i))
# p_sum=0
# for n in nums:
#     if n>0:
#         p_sum+=n
# print(f"Сума додатніх чисел={p_sum}")
#Task 4
# numbers=input("Введіть цілі числа через пробіл: ").split()
# nums=[]
# for i in numbers:
#     nums.append(int(i))
# for n in range(len(nums)):
#     if nums[n]%2==0:
#         print(n,end=" ")
#Task 5
# text="today is a sunny day 1 the (perfect!!!) weather, for 2 a walk - in the 3 park!. {people} are smiling children 4 are! playing and 5 birds are singing in the treetops!!!."
# text1=text.split('.')
# new_text=""
# for i in text1:
#     i=i.strip()
#     if i:
#         new_text+=i.capitalize()+'. '
# print(new_text.strip())
# count_nums=0
# for n in text:
#     if n.isdigit():
#         count_nums+=1
# print(f"Цифри в тексті зустрічаються {count_nums} разів")
# punctuation_count=0
# punctuation=",.:;?!-—()[]{}"
# for n in text:
#     if n in punctuation:
#         punctuation_count+=1
# print(f"Знаки пунктуації в тексті зустрічаються {punctuation_count} разів")
# Exclamation_count=0
# Exclamation="!" #або ми не створюємо цю зміну і в умові просто зрівнюємо елемент масиву з знаком оклику.
# for n in text:
#     if n in Exclamation:
#         Exclamation_count+=1
# print(f"Кількість знаків оклика в тексті =({Exclamation_count})")
#Task 6
# numbers=input("Введіть цілі числа через пробіл: ").split()
# nums=[]
# for i in numbers:
#     nums.append(int(i))
# unq=[]
# for n in nums:
#     if n not in unq:
#         unq.append(n)
# print(f"Стартові значення з повторенями --> {nums}")
# print(f"Тільки унікальні значення без повторень --> {unq}")
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










