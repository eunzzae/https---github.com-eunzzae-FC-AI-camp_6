import random

class Game:
    def __init__(self, turn):
        self.turn=turn
        self.min_num=1
        self.max_num=3
        self.curr_num=0
        self.is_finished=0
        
    def input_num(self):
        while True:
            try:
                user=int(input(f'부르고 싶은 숫자의 개수 ({self.min_num}~{self.max_num})를 입력해주세요. : '))
                if self.min_num <= user <= self.max_num:
                    return user
                else:
                    print(f'({self.min_num}~{self.max_num}) 사이의 숫자를 입력해주세요. : ')
            except ValueError:
                print('숫자를 입력해주세요.')
    
    def check_count(self, length):
        caller = '플레이어' if self.turn else '컴퓨터'
        print(f'{caller}가 입력한 숫자는', list(range(self.curr_num+1, self.curr_num+length+1)))
        self.curr_num += length
        if self.curr_num >= 31:
            print(f'{caller}는 패배')
            self.is_finished = 1
    
    def start_game(self):
        while not self.is_finished:
            call = self.input_num() if self.turn else random.randrange(self.min_num, self.max_num+1)
            self.check_count(call)
            self.turn = not self.turn
            
instance = Game(1) # 1이면 플레이어 먼저 시작, 0이면 컴퓨터 먼저 시작
instance.start_game()
            
        
                