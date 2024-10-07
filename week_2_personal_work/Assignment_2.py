
class person:
    def __init__(self, name, gender, age):
        self.name = str(name)
        self.gender = str(gender)
        self.age = int(age)

# 클래스 의 하위 메서드들은 self로 객체의 속성에 대해 받아올 수 있는데, 그것을 알면서도 display(name, gender, age)를 했다.
    # def display(name, gender, age):
    def display(self):
        print(f"이름 : {self.name}, 설병 : {self.gender}")
        print(f"나이 : {self.age}")


while True:
    try:
        p_age = int(input("나이 : "))
        p_name = str(input("이름 : "))
        p_gender = str(input("성별 : "))
        if p_gender.lower() == "male" or p_gender.lower() == "femele":
            newperson = person(p_name,p_gender,p_age)
            newperson.display()
            break
        else:
            print("성별은 male 또는 female로 입력 해주시기 바랍니다.")
    except ValueError:
        print("나이는 숫자로 입력해주시기 바랍니다.")
