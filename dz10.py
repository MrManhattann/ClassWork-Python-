#Task 1
# text="Эти английские тексты для начинающих предоставляют возможность бесплатно попрактиковаться в чтении и понимании онлайн. Занятия по пониманию письменного английского языка расширят ваш словарный запас и улучшат понимание грамматики и порядка слов. Тексты ниже призваны помочь вам развиваться и предоставляют вам мгновенную оценку вашего прогресса."
#
# j=text.split('.')
#
# for i in j:
#     if i.strip():
#         print(i.strip())
#Task 2
# text=input("Введіть рядок для перевірки на поліндром --> ").lower()
# dell=[]
# for i in text:
#     if i.isalnum():
#         dell.append(i)
# if dell==dell[::-1]:
#     print(f"{text} <--це паліндром!!!")
# else:
#     print(f"{text} <--це не паліндром!!!")
#Task 3
# text=input("Введіть текст --> ")
# reserv=["мама","папа","син"]
#
# words=text.split()
# res=[]
#
# for i in words:
#     if i.lower() in reserv:
#         res.append(i.upper())
#     else:
#         res.append(i)
# text2=" ".join(res)
# print(f"Оновлений текст з зарезервованими словами у верхньому регістрі --> {text2}")
#Task 4
# text=input("Введіть рядок: ")
# symbol1,symbol2=input("Введіть символ перший і через пробіл другий: ").split()
#
# index1=text.find(symbol1)
# index2=text.find(symbol2)
#
# if index1==-1 or index2==-1:
#     print("Одного з символів не було знайденно!!!")
# else:
#     start=min(index1,index2)
#     end=max(index1,index2)
#
#     text2=text[:start]+text[end+1:]
#     print(f"Текст або рядок з видаленими символами і діапазоном між ними: {text2}")
#Task 5
# text=input("Введіть рядок: ")
# symbol=input("Введіть символи для видалення: ")
#
# words=text.split()
# res=[]
# found=False
# for i in words:
#     found = False
#     for j in symbol:
#         if j in i:
#             found=True
#             break
#     if not found:
#         res.append(i)
# print(f"Результат з видаленими словами де був символ: {' '.join(res)}")
#Task 6
# text=input("Введіть рядок: ")
# words=text.split()
# text2=words[::-1]
# res=' '.join(text2)
# print(f"Результат зворотнього виводу тексту: {res}")

