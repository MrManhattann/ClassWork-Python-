#Частина 2
#Task 1
# numbers=input("Введіть цілі числа через пробіл: ").split()
# nums=[]
#
# for і in numbers:
#     nums.append(int(і))
#
# s=0
# for number in nums:
#     s+=number
#
# avg=s/len(nums)
#
# print(f"Сума чисел: {s}")
# print(f"Середнє арифметичне: {avg}")
# #Task 2
# numbers=input("Введіть цілі числа через пробіл: ").split()
# target=int(input("Яке число шукати?: "))
#
# nums=[]
# for n in numbers:
#     nums.append(int(n))
#
# count=0
# for number in nums:
#     if number == target:
#         count += 1
#
# print(f"Число {target} зустрічається {count} разів.")
#Task 3
# numbers=input("Введіть цілі числа через пробіл: ").split()
# nums=[]
#
# for n in numbers:
#     nums.append(int(n))
#
# positive_sum=0
# for number in nums:
#     if number > 0:
#         positive_sum+=number
#
# print(f"Сума додатних чисел: {positive_sum}")
# #Task 4
# numbers=input("Введіть цілі числа через пробіл: ").split()
# nums=[]
#
# for n in numbers:
#     nums.append(int(n))
#
# print("Індекси парних чисел:")
# for i in range(len(nums)):
#     if nums[i]%2==0:
#         print(i)
#Task 5
# text = input("Введіть текст: ")
# sentences = text.split('.')
# new_text = ""
# for sentence in sentences:
#     sentence = sentence.strip()
#     if sentence:
#         new_text += sentence.capitalize() + '. '
# print("Виправлений текст:")
# print(new_text.strip())
#
# digit_count = 0
# for char in text:
#     if char.isdigit():
#         digit_count += 1
#
# punct_count = 0
# punctuations = ",.:;?!-—()[]{}"
# for char in text:
#     if char in punctuations:
#         punct_count += 1
#
# exclam_count = 0
# for char in text:
#     if char == '!':
#         exclam_count += 1
#
# print(f"Цифр у тексті: {digit_count}")
# print(f"Розділових знаків: {punct_count}")
# print(f"Знаків оклику: {exclam_count}")
#Task 6
# numbers=input("Введіть цілі числа через пробіл: ").split()
# nums=[]
#
# for n in numbers:
#     nums.append(int(n))
#
# unique=[]
# for number in nums:
#     if number not in unique:
#         unique.append(number)
#
# print("Список без повторів:")
# print(unique)