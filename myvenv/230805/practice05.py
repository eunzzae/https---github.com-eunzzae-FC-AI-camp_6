# 업, 다운 게임 만들기
# import random

# com = random.randrange(1, 101)
# is_matched = 0

# while not is_matched:
#     user = int(input('1 부터 100 사이의 수 중에서 하나를 선택해주세요. : '))
#     if user<com:
#         print('업')
#     elif user>com:
#         print('다운')
#     else:
#         print("정답")
#         is_matched=1

# BR31 게임 만들기 

import random

class Game:
    def __init__(self, turn):
        self.turn = turn
        self.min_num = 1 # 부를 수 있는 숫자의 최소, 최대 개수도 게임 생성 시 변경할 수 있게 수정 가능
        self.max_num = 3
        self.curr_num = 0
        self.is_finished = 0

    def input_with_validation(self):
        while True:
            try:
                user = int(input(f'부르고 싶은 숫자의 개수 ({self.min_num}~{self.max_num}) 를 입력해주세요.'))
                if self.min_num <= user <= self.max_num: # 최대 최소 조건을 만족했을때만 리턴
                    return user
                else:
                    print(f'{self.min_num}~{self.max_num} 사이의 숫자를 입력해주세요.')
            except ValueError: # 숫자를 입력한게 아니라면
                print('숫자를 입력해주세요.')

    def check_count(self, length):
        caller = '플레이어' if self.turn else '컴퓨터'
        print(f'{caller}가 입력한 숫자는 : ', list(range(self.curr_num+1, self.curr_num+length+1)))
        self.curr_num += length
        if self.curr_num >= 31:
            print(f'{caller} 패배')
            self.is_finished = 1

    def start_game(self):
        while not self.is_finished:
            call = self.input_with_validation() if self.turn else random.randrange(self.min_num, self.max_num+1)
            self.check_count(call)
            self.turn = not self.turn

instance = Game(1) # 1이면 플레이어 먼저 시작, 0이면 컴퓨터 먼저 시작
instance.start_game()