#reduce 함수

from functools import reduce

my_list=[1,2,3,4,5]
result=reduce(lambda x, y: x+y, my_list)
# x=1, y=2, 리턴값=3
# x=3, y=전의 리턴값=3, 리턴값=6
# x=4, y=전의 리턴값=6, 리턴값=10
# x=5, y=전의 리턴값=10, 리턴값=15
print(result)