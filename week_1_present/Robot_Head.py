
# def head_act(eyes, mouth):
#     if eyes == 0 and mouth == 1:
#         return "눈을 깜빡이며 입 벌리기!"
#     elif eyes == 0 and mouth == 0:
#         return "눈을 깜빡이며 입을 닫음"
#     elif eyes == 1 and mouth == 1:
#         return "눈을 뜨고 입 벌리기!"
#     else:
#         return "눈을 뜨고 입을 닫음"
    
def head_act(operate_eyes, operate_mouth):
    if operate_eyes == 0 and operate_mouth == 1:
        return "발성기능을 실행 시키겠습니다."
    elif operate_eyes == 0 and operate_mouth == 0:
        return "아무런 기능을 하지 않습니다."
    elif operate_eyes == 1 and operate_mouth == 1:
        return "전방스캔과 발성기능을 실행 시키겠습니다."
    else:
        return "전방스캔기능을 실행 시키겠습니다."


def head_check(engine_start):
    if engine_start.lower() == "on":
        print("머리 기능이 정상 작동 하고 있습니다.")