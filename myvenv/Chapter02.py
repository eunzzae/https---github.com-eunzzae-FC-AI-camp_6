# *args
# 인자를 몇 개 명시하더라도 다 더해서 리턴해주는 함수
# def plus(*args) :
#     result=0
#     for i in args:
#         result+=i
#     return result

# result =plus(1,2,3,4,5,6,7) #*args = (1,2,3,4,5,6)
# print(result)

#1. 학생 수에 관계없이 아래와 같은 매개변수가 들어왔을 때 모든 점수의 총합을 리턴하는 함수를 작성하세요. (결과값을 return)


students = [{'id': 1, 'name': 'Kim', 'score': {'math': 50, 'english': 70}},
{'id': 2, 'name': 'Park', 'score': {'math': 80, 'english': 60}},]


def sum_scores(*students):
    result=sum([sum(student['score'].values()) for student in students])
    return result