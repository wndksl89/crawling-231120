import random

class RandomNumber:
    def __init__(self):
        self.random_number = random.randint(1, 100)

    def play_game(self):
        game_count = 0

        while True:
            my_number = int(input("1~100 사이의 숫자를 입력하세요:"))
            game_count += 1
            print("다운" if my_number > self.random_number else "업" if my_number < self.random_number else f"축하합니다.{game_count}회 만에 맞췄습니다")
            if my_number == self.random_number:
                break

        return game_count

if __name__ == '__main__':
    r = RandomNumber()
    game_count = r.play_game()

    print(f'랜덤넘버: {r.random_number}')
    print(f'맞추는데 걸린 횟수: {game_count}')
