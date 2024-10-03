# 지호님 모듈

def weapon_check(engine_start):
    if engine_start.lower() == "on":
        print("장비 기능이 정상 작동 하고 있습니다.")


def weapon_act():
    tools_list = ["날개", "무기"]
    weapon_list = ["총", "칼", "폭탄"]

    print("필요하신 도구는 무엇입니까?")

    tools = input(f'{tools_list}에서 골라주세요 : ')

    if tools == "날개":
        print("날개를 호출했습니다.")
    elif tools == "무기":
        print("무기를 호출했습니다. 무기 목록 업로드 중...")
        weapon_info = input(f'{weapon_list}중 필요하신 무기를 호출해주세요 : ')
        if weapon_info == "총":
            print("총을 호출했습니다.")
        elif weapon_info == "칼":
            print("칼을 호출했습니다.")
        elif weapon_info == "폭탄":
            print("폭탄을 호출했습니다.")
        else:
            print("요청하신 무기는 현재 가지고 있지 않습니다. 죄송합니다")
    else:
        print("요청하신 도구는 현재 가지고 있지 않습니다.")
    return print("도구 불러오기를 종료합니다.")


# weapon_act()
