# lambda 매개변수 : 리턴값
# result = (lambda x: [x*1, x*2, x*3])(3) # x에 3이 들어가고, [3, 6, 9]가 리턴됨
#print(result) # [3, 6, 9]

#result = (lambda x: [x * i for i in range(1, 11)])(3) # x에 2가 들어가고,
#print(result) # [2*1, 2*2, ... , 2*9] 가 리턴됨

# map함수
# 함수가 각각 요소마다 적용된 리스트 = map(각각 요소에다가 적용하고자 하는 함수, [1,2,3])
my_list=[1,2,3] #각 숫자 앞에다가 '안녕하세요'라고 붙이고 싶다면?
result=map(lambda x: f'안녕하세요{x}', my_list)
print(list(result))

# filter함수(조건으로 쓸 함수, 리스트)
# 조건으로 쓸 함수는 True 혹은 False 를 리턴해야함
my_list = [1,2,3,4,5,6,7,8,9,10]
result=filter(lambda x: x%2==0, my_list)
print(list(result))