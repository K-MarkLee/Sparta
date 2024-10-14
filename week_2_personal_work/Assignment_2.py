
#관례를 따라 class이름을 대문자로 변경
# class person:
class Person:
    def __init__(self, name, gender, age):
        self.name = str(name)
        self.gender = str(gender)
        self.age = int(age)

# 클래스 의 하위 메서드들은 self로 객체의 속성에 대해 받아올 수 있는데, 그것을 알면서도 display(name, gender, age)를 했다.
    # def display(name, gender, age):
    def display(self):
        if self.age > 19:
            adult = "성인"
        else:
            adult = "미성년자"
        print(f"이름 : {self.name}, 성별 : {self.gender}")
        print(f"나이 : {self.age}")
        print(f"안녕하세요, {self.name}님! {adult}이시군요!")
        return



while True:
    try:
        p_age = int(input("나이 : "))
        break
    except ValueError:
        print("나이는 숫자로 입력해주시기 바랍니다.")

p_name = str(input("이름 : "))

while True:
    p_gender = str(input("성별 : "))
    if p_gender.lower() == "male" or p_gender.lower() == "female":
        newperson = Person(p_name, p_gender, p_age)
        newperson.display()
        break
    else:
        print("성별은 male 또는 female로 입력 해주시기 바랍니다.")
