# hello="hello world"
# print(hello.split(" "))

# bye=hello.replace('hello','bye')
# print(bye)

# fruits = ['사과', '바나나', '배']
# fruits[2] = '복숭아'
# print(fruits) # 복숭아 바나나 배

# fruits = ['사과', '바나나', '배', ['복숭아', '딸기']]
# print(fruits[3][0]) 
# print(fruits) 

# fruits=['사과','바나나','배',{'name':'Koh'}]
# print(fruits[3]['name'])

# fruits = ["사과", "바나나", "배"]
# fruit = fruits.pop() # 위 리스트에서 마지막 요소인 '배'를 추출해서 fruit 변수에 할당
# print(fruit) # 배
# print(fruits) # [사과, 바나나]

# numbers = [2, 3, 1, 5, 4]
# numbers.sort()
# print(numbers) # [1, 2, 3, 4, 5] (역순 정렬을 하고 싶다면 sort 후 reserve 해주면 되겠죠?)
# numbers.reverse()
# print(numbers)

# user = {
# 	'name': 'Kim',
# 	'age': 20,
# 	'hobby': ['Basketball', 'Tennis'],
# 	'address': {'City': 'Seoul', 'Street': 'Dongdaemun'}
# }
# print(user['hobby'][1]) # Tennis
# print(user['address']['City']) # Seoul

# score = int(input('점수를 입력하세요. : '))

# if score >=int(95):
#     print("A")
# elif score >=int(90):
#     print("B")
# elif score >=int(85):
#     print("C")
# elif score <int(85):
#     print("F")

num1 = int(input('첫번째 숫자를 입력하세요. : '))
num2 = int(input('두번째 숫자를 입력하세요. : '))

if num1%2==1 & num2%2==1:
    print("홀수")
else:
    print("짝수")