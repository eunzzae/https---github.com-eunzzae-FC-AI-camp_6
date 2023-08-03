#1. 아래 딕셔너리에서, 모든 학생들의 영어 점수 총합을 출력하는 코드를 작성하세요.
# scores = {
#   'Kim': {'math': 50, 'english': 70},
#   'Park': {'math': 70, 'english': 60},
#   'Lee': {'math': 80, 'english': 50}
# }

# total=0
# for score in scores.values():
#     total += score['english']
# print(total)

# total=sum([score['english'] for score in scores.values()])
# print(total)

#2. 아래 리스트에서, 수학 점수가 60점 이상인 사람들만 남기는 코드를 작성하세요.
# students = [
#   {'id': 1, 'name': 'Kim', 'score': {'math': 50, 'english': 70}},
#   {'id': 2, 'name': 'Park', 'score': {'math': 80, 'english': 60}},
#   {'id': 3, 'name': 'Lee', 'score': {'math': 70, 'english': 50}},
# ]

# filtered_students=[]
# for student in students:
#     if student['score']['math'] >=60:
#         filtered_students
        
        
# filtered_students = [student for student in students if student['score']['math'] >=60]
# print(filtered_students)

#3. 아래 리스트에서, 학생 별로 total: (점수 총합) 을 추가하는 코드를 작성하세요. (리스트 컴프리헨션 사용 X)
students = [
  {id: 1, name: 'Kim', score: {math: 50, english: 70}},
  {id: 2, name: 'Park', score: {math: 80, english: 60}},
  {id: 3, name: 'Lee', score: {math: 70, english: 50}},
]

for student in students:
    student['score']['total'] = sum(student['score'].values())
print(students)