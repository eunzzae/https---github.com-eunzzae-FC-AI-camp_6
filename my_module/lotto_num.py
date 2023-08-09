import random

lotto = []
def random_lotto():
    random_num = random.randint(1, 45)

    for i in range(6):
        while random_num in lotto:
            random_num = random.randint(1, 45)
        lotto.append(random_num)
        
    lotto.sort()
    print(f'오늘의 로또번호는 {lotto}입니다.')

if __name__== "__main__" :
    random_lotto()