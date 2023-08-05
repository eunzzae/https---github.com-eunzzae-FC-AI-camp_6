# def multiply(x, y):
#     result = x*y
#     return result
# multiply(10, 20)

# def printSumAvg(x, y, z):
#     sum = x+y+z
#     avg = sum/3
    
#     print(f'합계 : {sum}, 평균 : {avg}')

# printSumAvg(10, 20, 30)

# 로또 번호 추출기 
# import random

# def get_random_number():
#     number = random.randint(1, 45)
#     return number

# lotto_num = [] # 로또 번호를 저장할 리스트

# for i in range(6):
#     random_num = get_random_number()
#     lotto_num.append(random_num)

# lotto_num.sort()
# for num in lotto_num:
#     print(num, end=" ")

# import random

# def get_random_number():
#     number = random.randint(1, 45)
#     return number

# lotto_num = [] # 로또 번호를 저장할 리스트

# count = 0 # 현재 뽑은 숫자

# while True:
#     if count ==6:
#         break
#     random_num = get_random_number()
#     if random_num not in lotto_num:
#         lotto_num.append(random_num)
#         count += 1
        
# lotto_num.sort()
# for num in lotto_num:
#     print(num, end=" ")
