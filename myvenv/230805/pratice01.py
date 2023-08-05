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

fruits = ["사과", "바나나", "배"]
fruit = fruits.pop() # 위 리스트에서 마지막 요소인 '배'를 추출해서 fruit 변수에 할당
print(fruit) # 배
print(fruits) # [사과, 바나나]

