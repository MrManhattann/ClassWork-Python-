#Task 1
# num1=int(input("Number 1 --> "))
# num2=int(input("Number 2 --> "))
#
# even_s=0
# even_c=0
#
# odd_s=0
# odd_c=0
#
# k9_s=0
# k9_c=0
#
# numbers1 = []
# numbers2 = []
# numbers3 = []
#
# for i in range(num1,num2+1):
#     if i%2==0:
#         even_s+=i
#         even_c+=1
#         numbers1.append(i)
#     else:
#         odd_s+=i
#         odd_c+=1
#         numbers2.append(i)
#     if i %9==0:
#         k9_s+=i
#         k9_c+=1
#         numbers3.append(i)
#
# even_a=even_s/even_c if even_c else 0
# odd_a=odd_s/odd_c if even_c else 0
# k9_a=k9_s/k9_c if k9_c else 0
#
# print(f"Сума праних чисел {numbers1} --> {even_s}, і їх середнє арефметичне --> {even_a}")
# print(f"Сума непраних чисел {numbers2} --> {odd_s}, і їх середнє арефметичне --> {odd_a}")
# print(f"Сума кратних 9 {numbers3} --> {k9_s}, і їх середнє арефметичне --> {k9_a}")
#Task 2
# length=int(input("Введіть довжину ліннії --> "))
# symbol=input("Введіть символ яким буде малюватись лінія --> ")
#
# i=0
#
# while i<length:
#     print(symbol)
#     i+=1
#Task 3
# while True:
#     num=int(input("Введіть число --> "))
#     if num==7:
#         print("Good bye!")
#         break
#     elif num>0:
#         print("Number is positive")
#     elif num<0:
#         print("Number is negative")
#     elif num==0:
#         print("Number is equal to zero")
#Task 4
# sum_num=0
# min_num=None
# max_num=None
# count=0
#
# while True:
#     num=int(input("Введіть число --> "))
#     if num==7:
#         print("Good bye!")
#         break
#     sum_num += num
#     count+=1
#     if max_num is None or num>max_num:
#         max_num=num
#     if min_num is None or num<min_num:
#         min_num=num
# if count>0:
#     print(f"Сума чисел --> {sum_num}")
#     print(f"Мінімум --> {min_num}")
#     print(f"Максимум --> {max_num}")
# else:
#     print("Ви одразу ввели 7 тому програма зевершилась!!!!!")
#Task 5
# while True:
#     num=int(input("Введіть число --> "))
#
#     if num<=1:
#         print("Число не може бути менше 1 або дорівнювати йому!!!!")
#         break
#
#     for i in range(2,num):
#         if num%i==0:
#             print(f"Число {num} не є простим")
#             break
#     else:
#         print(f"Число {num} є простим")
#Task 6
# while True:
#     num=int(input("Введіть число --> "))
#     if num<0:
#         print("Число не може бути відємним!!!!")
#         continue
#     if num==2000:
#         print("Напевно ви ввели число 2000, на жаль для вас програма завершуеться;)") #Додав це просто щоб була можливість самому вийти з циклу і завершити роботу,так можна було б і по іншому але мені здалось так будет краще)
    #     break
    # else:
    #     a=0
    #     b=1
    #     while b<num:
    #         next = a + b
    #         a=b
    #         b=next
    #     if b==num or a==num:
    #         print(f"Число {num} належить послідовності Фібоначчі")
    #     else:
    #         print(f"Число {num} не належить послідовності Фібоначчі")




