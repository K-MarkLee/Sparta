# 유림님 모듈


def leg_act(right, left):
    if 0 <= right <= 10 and 0 <= left <= 10:
        if right in range(4) and left in range(4):
            return '앞으로 점프합니다!'
        elif right in range(4, 7) and left in range(4, 7):
            return '제자리 점프에요!'
        else:
            return '뒤로 점프했어요!'
    else:
        return '점프를 실패했어요!'


def leg_check(engine_start):
    if engine_start.lower() == "on":
        print("다리 기능이 정상 작동 하고 있습니다.")


# right_leg = int(input('점프를 시도해볼까요? (0부터 10까지 입력)'))
# left_leg = int(input('점프를 시도해볼까요?(0부터 10까지 입력)'))
# action = leg_act(right_leg, left_leg)
# print(action)
