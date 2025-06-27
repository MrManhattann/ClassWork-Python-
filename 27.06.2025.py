#Task 0
# def mat_diya(a, b, c):
#    if c=="*":
#       res=a*b
#    elif c=="/":
#       res=a/b
#    elif c=="+":
#       res=a+b
#    elif c=="-":
#       res=a-b
#    print(f"{a}{c}{b}={res}")
# num1,num2=map(int,input("Enter a numbers: ").split())
# symbol=input("Enter a mat symbol: ")
# mat_diya(num1,num2,symbol)
#Task 0.1
# def suma(a, b):
#    res=a+b
#    print(res)
# def dell(a, b):
#    res=a/b
#    print(res)
# def minus(a, b):
#    res=a-b
#    print(res)
# def dobytok(a, b):
#    res=a*b
#    print(res)
# num1,num2=map(int,input("Enter a numbers: ").split())
# suma(num1,num2)
# dell(num1,num2)
# minus(num1,num2)
# dobytok(num1,num2)
#Part 1
#Task 1
# def text():
#    print(f"\033[90m\"Don't let the noise of others' opinions ")
#    print(f"\tdrown out your own inner voice.\"\033[0m")
#    print("\t\t\033[33mSteve Jobs\033[0m")
#
# text()
#Task 2
# def number(start, end):
#    if start>end:
#       start,end=end,start
#    for i in range(start,end):
#       if i%2!=0:
#          print(i,end=",")
# num1,num2=map(int,input("Enter a numbers: ").split())
# number(num1,num2)
#Task 3
#Task 3.1
# def line(l,d,s):
#    if d=="vertical":
#       for _ in range(l):
#          print(s)
#    elif d=="horizontal":
#       print((s+" ")*l)
#    else:
#       print("Incorrect direction")
# length=int(input("Enter a length: "))
# direction=input("vertical or horizontal: ")
# symbol=input("Enter a symbol: ")
# line(length, direction, symbol)
# def line_vertical(length,symbol):
#    i=0
#    while i<length:
#       print(f"{symbol}")
#       i+=1
# def line_gorisont(length,symbol):
#    i=0
#    while i<length:
#       print(f"{symbol}",end="")
#       i+=1
#
# leng=int(input("Length: "))
# sym=input("Symbol: ")
# line_gorisont(leng,sym)
# line_vertical(leng,sym)
#Task 4
# def maximal(l):
#    max_num=l[0]
#    for i in l:
#       if i>max_num:
#          max_num=i
#    print(f"Maximal nuber in seved list: {max_num}")
#
# def get_numbers():
#    nums = []
#    while True:
#       user_input = input("Введи число (або Enter для завершення): ")
#       if not user_input:
#          break
#       nums.append(int(user_input))
#    print(nums)
#    return nums
# nums=get_numbers()
# if nums:
#    maximal(nums)
# else:
#    print("Not list")
#Task 5
# def simple(l):
#    if l<2:
#       return False
#    for i in range(2,int(l**0.5)+1):
#       if l%i==0:
#          return False
#    return True
#
# number=int(input("Enter a number: "))
# if simple(number):
#    print("simple number")
# else:
#    print("not simple number")
#Task 6
# def lucky(l):
#    if len(l)!=6 or not l.isdigit():
#       return False
#    first=int(l[0])
#    second=int(l[1])
#    third=int(l[2])
#    fourth=int(l[3])
#    fifth=int(l[4])
#    six=int(l[5])
#    sum_left=first+second+third
#    sum_right=fourth+fifth+six
#    if sum_left==sum_right:
#       return True
#    else:
#       return False
#
# number=input("Enter a mb lucky numbers: ")
# if lucky(number):
#    print("Its lucky number")
# else:
#    print("Not lucky")
