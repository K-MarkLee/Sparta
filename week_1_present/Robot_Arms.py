# 하림님 모듈

def arm_act(arm_grab):
    if arm_grab.lower() == "1" :
        left_hand = "주먹을 쥠"
        right_hand = "경례 하고 내림"
        print("왼손: " + left_hand + ", 오른손: " + right_hand)
        # 추가 동작: 내린 오른손도 주먹을 쥔다
        right_hand = "주먹을 쥠"
        print("오른손이 내려진 후: " + right_hand)
    else :
        left_hand = "주먹을 풂"
        right_hand = "주먹을 풂"
        print("왼손: " + left_hand + ", 오른손: " + right_hand)
        

def arm_check(engine_start):
    if engine_start.lower() == "on":
        print("팔 기능이 정상 작동 하고 있습니다.")


# # 사용자로부터 엔진 상태 입력 받기
# engine_start = input("로봇의 엔진 상태를 입력하세요 (켜짐/꺼짐): ")
# # 함수 호출
# arm_act(engine_start)

