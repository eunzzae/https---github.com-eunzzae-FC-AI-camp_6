# for i in {'name': 'Kim', 'age': 20}:
# 	print(i) # name / age
# 	print('입니다')

# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)
    
# for i in range(1, 10):
#     if i == 5:
#         continue
#     print(i)    
    
# for i in range(1,10):
#     if i != 5:
#         print(i)

# for i in range(1,101):
#     if i%2 ==0 :
#         print(i)

# flag = 0
# while not flag:
# 	user = input('그만할까요?')
# 	if user == '그만':
# 		flag = 1    

# while True:
#     user = str(input('그만할까요?'))
# 	if user == '그만' :
# 		break

# numbers=[i for i in range(1,11)]
# print(numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filtered_numbers = [number for number in numbers if number >=4]
# print(filtered_numbers)

# filtered_numbers = []

# for i in numbers:
#     if i >=4:
#         filtered_numbers.append(i)
# print(filtered_numbers)

# scores = {
#   'Kim': {'math': 50, 'english': 70},
#   'Park': {'math': 70, 'english': 60},
#   'Lee': {'math': 80, 'english': 50}
# }

# sum = 0 
# for score in scores.values():
#     sum +=score['english']
# print(sum)

# scores_sum = sum(score['english'] for score in scores.values())
# print(scores_sum)

# students = [
#   {'id': 1, 'name': 'Kim', 'score': {'math': 50, 'english': 70}},
#   {'id': 2, 'name': 'Park', 'score': {'math': 80, 'english': 60}},
#   {'id': 3, 'name': 'Lee', 'score': {'math': 70, 'english': 50}},
# ]

# filtered_students = []
# for student in students:
#     if student['score']['math'] >= 60:
#         filtered_students.append(student)
# print(filtered_students)

# filtered_students = [student for student in students if student['score']['math'] >=60]
# print(filtered_students)

students = [
  {'id': 1, 'name': 'Kim', 'score': {'math': 50, 'english': 70}},
  {'id': 2, 'name': 'Park', 'score': {'math': 80, 'english': 60}},
  {'id': 3, 'name': 'Lee', 'score': {'math': 70, 'english': 50}},
]

for student in students:
    student['score']['total'] = sum(student['score'].values())
print(students)
    