
import random

# ver 1

# ver 2
# 숫자를 받아 오는것 또한 메서드로 대체해보기

#관례에 따라 클래스의 이름은 대문자로 변경

# class num_game:
class Num_game:
    def __init__(self, num1=None, num2=None):
        if num1 is None or num2 is None:
            num1, num2 = self.get_num()
        self.minnum = num1
        self.maxnum = num2

        #randint는 최대값의 숫자를 포함하지 않기 때문에, +1을 해줘야 한다.
        self.random_number = random.randint(num1, num2+1)
        print(f"{num1}과 {num2}사이의 숫자를 하나 정했습니다.")

    def get_num(self):
        print("랜덤 숫자 맞추기 게임의 범위를 지정해주세요.")
        minnum = int(input("최소 숫자를 입력해 주세요: "))
        maxnum = int(input("최대 숫자를 입력해 주세요: "))
        return minnum, maxnum

    def playgame(self):
        print("이 숫자는 무엇일까요?")
        while True:
            user_num = int(input("예상 숫자: "))
            if user_num == self.random_number:
                print("축하합니다! 정답입니다")
                while True:
                    again = str(input("새 게임을 진행 하시겠습니까? (yes or no) : "))
                    if again.lower() == "yes":
                        # print("랜덤 숫자 맞추기 게임의 범위를 지정해주세요.")
                        # num_range1 = int(input("최소 숫자를 입력해 주세요: "))
                        # num_range2 = int(input("최대 숫자를 입력해 주세요: "))
                        # new_game = num_game(num_range1, num_range2)
                        # new_game.playgame()
                        # return

                        minnum, maxnum = self.get_num()
                        new_game = Num_game(minnum, maxnum)
                        new_game.playgame()
                        return

                    elif again.lower() == "no":
                        print("게임을 종료합니다.")
                        return
                    else:
                        print("다시 입력해 주세요.")
            elif user_num < self.random_number and user_num < self.maxnum:
                print("너무 작습니다. 다시 입력해주세요.")
            elif user_num > self.random_number and user_num < self.maxnum:
                print("너무 큽니다. 다시 입력해주세요.")
            else:
                print("범위 안의 숫자를 제대로 입력해주세요.")

# print("랜덤 숫자 맞추기 게임의 범위를 지정해주세요.")
# num_range1=int(input("최소 숫자를 입력해 주세요: "))
# num_range2=int(input("최대 숫자를 입력해 주세요: "))
# new_game=num_game(num_range1, num_range2)
# new_game.playgame()


new_game = Num_game()
new_game.playgame()
