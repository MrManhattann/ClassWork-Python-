#Task 0
# def reverse(a):
#     array2=a[::-1]
#     print(array2)
# array=list(map(int,input().split()))
# # print(array)
# reverse(array)
#Task 0.1
# def reverse(a):
#     n=len(a)
#     array2=[0]*n
#     i=n-1
#     j=0
#     while i>=0:
#         array2[i]=a[j]
#         i=i-1
#         j+=1
#     print(array2)
# array=list(map(int,input(":").split()))
# reverse(array)
#Task 0.2
# def reverse(a):
#     n = len(a)
#     array2 = [0] * n
#     j = n - 1
#     for i in range(n):
#         array2[i] = a[j]
#         j-=1
#     print(array2)
#
# array=list(map(int,input(":").split()))
# reverse(array)
#Task 0.3
# def reverse(a):
#     n=len(a)
#     array2=[0]*n
#     i=0
#     while i<n:
#         array2[i]=a[(n-1)-i]
#         i+=1
#     print(array2)
# array=list(map(int,input(":").split()))
# reverse(array)
#Task 0.0.0
#Вивести числа від 1 до n, де - атуральне число, введене з клавіатури (рекурсивний спосіб)
# def rec(num):
#     print(num, end=" ")
#     if num==1:
#         return 1
#     return rec(num-1)
#
# n=int(input("Enter a number: "))
# rec(n)
#Tasl 0.0.1
# def rec(num):
#     if num=="1":
#         return "1"
#     return num+" -> "+rec(str(int(num)-1))
#
# n=input("Enter a number: ")
# print(rec(n))
#Task 0.0.2/ bes minusa
# def stepin(n,p):
#     n*stepin(n,p-1)
#
# num,pow=map(int,input("Enter number and pow -> ").split())
# res=stepin(num,pow)
# print(res)
#Task 0.0.2/ s nulem
# def stepin(n, p):
#     if p==0:
#         return 1
#     return n * stepin(n, p - 1)
#
# num,pow = map(int, input("Enter number and pow -> ").split())
# res=stepin(num,abs( pow))
# if pow>=0:
#     print(res)
# else:
#     print(1/res)
#Task 0.0.3
# def suma(start,end):
#     if start==end:
#         return start
#     return start+suma(start+1, end)
#
# num1,num2 = map(int, input("Enter two number  -> ").split())
# if num1>num2:
#     mum1,num2=num2,num1
# res=suma(num1,num2)
# print(res)
#Part 3
#Task 1
# def power(num,exponent):
#     if exponent==0:
#         return 1
#     if exponent<0:
#         return 1/power(num,-exponent)
#     return num*power(num,exponent-1)
# print(power(2,3))
# print(power(4,3))
# print(power(6,3))
#Task 2
# def suma(a,b):
#     if a>b:
#         return suma(b,a)
#     if a==b:
#         print(f"suma({a},{b})={a}")
#         return a
#     else:
#         print(f"suma({a},{b})={a}+suma({a + 1},{b})")
#         result=a+suma(a+1,b)
#         print(f"Після обчислення: suma({a}, {b}) = {result}")
#         return result
# a = int(input("Введіть a: "))
# b = int(input("Введіть b: "))
#
# result = suma(a, b)
# print(f"Сума чисел від {a} до {b} дорівнює {result}")
# Task 3
# def imge(x):
#     if x<=0:
#         return
#     print("*",end="")
#     imge(x-1)
# imge(6)
#Task 4
# def is_leap_year(year):
#     return (year%4==0 and year%100!=0) or (year%400==0)
# def days_since_start(day, month, year):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     days=(year-1)*365
#     leap_years=(year-1)//4-(year-1)//100+(year-1)//400
#     days+=leap_years
#     for i in range(month-1):
#         days+=month_days[i]
#     if month>2 and is_leap_year(year):
#         days+=1
#     days+=day
#     return days
# def date(x,c,v,b,n,m):
#     days1=days_since_start(x, c, v)
#     days2=days_since_start(b, n, m)
#     return abs(days1-days2)
# print(date(4, 7, 2025, 4, 6, 2026))
#Task 5
# import random
# numbers = [random.randint(-100, 100) for _ in range(100)]
# print(numbers)
# def find_min_sum_index(arr, index=0, min_index=0, min_sum=None):
#     if index > len(arr) - 10:
#         return min_index
#     current_sum = sum(arr[index:index+10])
#     if min_sum is None or current_sum < min_sum:
#         min_sum = current_sum
#         min_index = index
#     return find_min_sum_index(arr, index + 1, min_index, min_sum)
# pos = find_min_sum_index(numbers)
# print("Мінімальна сума починається з індексу:", pos)
# print("Підпослідовність:", numbers[pos:pos+10])
# print("Її сума:", sum(numbers[pos:pos+10]))
#Task 6
#Крестики нолик с помощью інтрернета
# import random
#
# board = [' '] * 9
#
#
# def display_board():
#     print()
#     for i in range(3):
#         row = '|'.join(board[i * 3:(i + 1) * 3])
#         print(row)
#         if i < 2:
#             print("-+-+-")
#     print()
#
#
# def check_win(symbol):
#     win_combinations = [
#         (0, 1, 2), (3, 4, 5), (6, 7, 8),
#         (0, 3, 6), (1, 4, 7), (2, 5, 8),
#         (0, 4, 8), (2, 4, 6)
#     ]
#     return any(board[i] == board[j] == board[k] == symbol for i, j, k in win_combinations)
#
#
# def check_draw():
#     return ' ' not in board
#
#
# def player_move(symbol):
#     while True:
#         try:
#             move = int(input(f"Гравець '{symbol}', введіть номер клітини (1-9): ")) - 1
#             if 0 <= move < 9 and board[move] == ' ':
#                 board[move] = symbol
#                 break
#             else:
#                 print("Невірний хід. Спробуйте ще раз.")
#         except ValueError:
#             print("Введіть число від 1 до 9.")
#
#
# def computer_easy(symbol):
#     move = random.choice([i for i in range(9) if board[i] == ' '])
#     board[move] = symbol
#     print(f"Комп'ютер ({symbol}) вибрав клітину {move + 1}.")
#
#
# def computer_medium(symbol):
#     opponent = 'X' if symbol == 'O' else 'O'
#     for i in range(9):
#         if board[i] == ' ':
#             board[i] = opponent
#             if check_win(opponent):
#                 board[i] = symbol
#                 print(f"Комп'ютер ({symbol}) блокує хід гравця, обрав {i + 1}.")
#                 return
#             board[i] = ' '
#     computer_easy(symbol)
#
#
# def minimax(is_maximizing, symbol, opponent):
#     if check_win(symbol):
#         return 1
#     elif check_win(opponent):
#         return -1
#     elif check_draw():
#         return 0
#
#     best_score = -float('inf') if is_maximizing else float('inf')
#     for i in range(9):
#         if board[i] == ' ':
#             board[i] = symbol if is_maximizing else opponent
#             score = minimax(not is_maximizing, symbol, opponent)
#             board[i] = ' '
#             if is_maximizing:
#                 best_score = max(score, best_score)
#             else:
#                 best_score = min(score, best_score)
#     return best_score
#
#
# def computer_hard(symbol):
#     opponent = 'X' if symbol == 'O' else 'O'
#     best_score = -float('inf')
#     best_move = None
#     for i in range(9):
#         if board[i] == ' ':
#             board[i] = symbol
#             score = minimax(False, symbol, opponent)
#             board[i] = ' '
#             if score > best_score:
#                 best_score = score
#                 best_move = i
#     board[best_move] = symbol
#     print(f"Комп'ютер ({symbol}) зробив оптимальний хід: {best_move + 1}.")
#
#
# def play_game(mode='1', level='easy'):
#     global board
#     board = [' '] * 9
#     current_player = 'X'
#     display_board()
#
#     while True:
#         if mode == '1':
#             player_move(current_player)
#         elif mode == '2':
#             if current_player == 'X':
#                 player_move('X')
#             else:
#                 if level == 'easy':
#                     computer_easy('O')
#                 elif level == 'medium':
#                     computer_medium('O')
#                 elif level == 'hard':
#                     computer_hard('O')
#         display_board()
#
#         if check_win(current_player):
#             print(f"Гравець '{current_player}' переміг!")
#             break
#         if check_draw():
#             print("Нічия!")
#             break
#         current_player = 'O' if current_player == 'X' else 'X'
#
# def main():
#     while True:
#         print("\n--- Хрестики-нулики ---")
#         print("1. Людина — Людина")
#         print("2. Людина — Комп'ютер")
#         choice = input("Оберіть режим (1 або 2): ")
#
#         level = 'easy'
#         if choice == '2':
#             print("Рівні складності: easy / medium / hard")
#             level = input("Оберіть рівень складності: ").strip().lower()
#             if level not in ['easy', 'medium', 'hard']:
#                 print("Невірний рівень. Встановлено 'easy'.")
#                 level = 'easy'
#
#         play_game(mode=choice, level=level)
#
#         again = input("Хочете зіграти ще раз? (y/n): ").lower()
#         if again != 'y':
#             break
#
#
# if __name__ == "__main__":
#     main()
