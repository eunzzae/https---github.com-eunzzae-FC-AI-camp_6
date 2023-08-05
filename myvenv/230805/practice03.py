# def sum(*numbers):
#    result = 0
#    for i in numbers:
#        result += i
#    return result

#print(sum(1,2,3,4,5))

# def show_user(**user):
#    for i, j in user.items():
#        print(f'{i}는 {j}입니다.')

#show_user(name='koh', age=20)


# def prc1(num):
#     num = 1
#     for i in range(1, 11):
#         num += 1
# print(f'{num} X {i} = num * i')

# def prc2(num):
#     sum = 0
# 	for i in range(1, 11):
# 		sum += num * i
# 	return sum

# def prc3(name, age):
#     if age > 18:
# 		result = '성인'
# 	else:
# 		result = '미성년자'
# 	print(f'{name} 님은 {result} 입니다.')

# 구구단 출력하기
# x = int(input('몇 단을 출력할까요? : '))

# for i in range(1, 10):
#     print(f'{x} X {i} = {x*i}')    

# 게임 메뉴 만들기
# while True:
    
#     print('[메뉴를 입력하세요.]')
#     menu = int(input('1. 게임시작 2. 랭킹보기 3. 게임종료 : '))

#     if menu == 1 : 
#         print("게임을 시작합니다. ")
#     elif menu == 2 :
#         print("실시간 랭킹")
#     elif menu == 3 :
#         print('게임을 종료합니다.')
#         break
#     else:
#         print('다시 입력해주세요.')


kor_list = ['사랑', '스벅', '하늘', '재밌다']

score = 0 

print("Let's Learning Korean")
for word in kor_list:
    print(word)
    data = input()
    if data == word:
        score += 1

print("전체 문제 개수 : ", len(kor_list))
print("맞힌 문제 개수 : ", score)
print("전체 문제 개수 : ", len(kor_list)- score)

# 전체 문제 개수 : 4개
# 맞힌 문제 개수 : 2개
# 틀린 문제 개수 : 2개
