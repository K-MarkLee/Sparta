
class Ai_student:
    def __init__(self,inputname):
        self.name = inputname

    def greet (self):
        print("Hello my name is", self.name)

    def test (a):
        print("This is test")
# 클래스 안의 함수에서 self는 관례이지만 ()안에 어떤 문자가 들어가도 실행은된다(self의 의미를 가짐)
# 하지만 비워 둘 경우 에러가 뜬다.

alice = Ai_student("Alice")
bob = Ai_student("Bob")
alice.greet()
bob.greet()
alice.test()


# pass를 넣는다면, 코드를 적는중 이 함수는 패스하고 다음 코드로 넘어가 테스트 하기 편하게 해준다.

# 매직 메서드란, 미리 정의된 메서드 이다. 예시로는 __init__이 있다.
# 매직 메서드란 내부적인 메서드 이기도 하다.
# 메서드란 클래스 안에 있는 함수이다.
# 매직 메서드는 객체와의 연결성이 좋기 때문에 가장 자주 쓰이고 중복이 될거 같은 것에 설정을 하면 좋을 것 같다.
class human:

# __init__은  객체가 생성이 될때, 자동으로 호출이 되며, 객체의 초기화를 담당한다.
    def __init__(self, name, age):
        self.name = name
        self.age = age

# __repr_은 print와 같이 표시를 해주는 함수이지만, print와는 달리 공식적인 내용을 뽑아와준다.
# 이는 __repr__목적 같은것이고 사실상 표시만 하려고 한다면 print또는 다른 함수를 써도 되지만,
# 내부함수가 있음에도 사용자 함수를 만들어 쓰는 것 처럼 이또한 디폴트 적인 함수 중 하나이다.
    def __repr__(self):
        return f"human ('{self.name}', {self.age})"


# 객체 간의 뎃셈을 연산해준다. 따로 함수를 불러오지 않고 + 연산자로 호출 할 수 있다.
    def __add__(self, other):
        print(self.name+other.name)
        print(self.age+other.age)


# 객체 간의 비교를 해준다. 이또한 따로 함수를 불러오지 않고 연산자 즉 == 로 호출 할 수 있다.
    def __eq__(self, other) :
        if self.name == other.name :
            print("이름이 같습니다")
        else :
            print("이름이 다릅니다")


# 이 메서드 에서는 한번에 하나의 반환값만 도출 하기 때문에, 만약 이름만 불러 온다거나, 나이만 불러온다거나 등 불가능하다.
    def __str__(self):
        return f"{self.name}님은 {self.age}살입니다."


mark = human('이승열',26)
dark = human('어승열', 26)
print(repr(mark))

mark+mark
mark == dark
print(mark.name)


# 클래스 메서드

class MyClass:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        

# 클래스 변수이다. 이는 클래스 내부 뿐만이 아닌, 이 클래스에 생성된 모든 개체에서도 공유를 한다.
    class_variable = 0

# 클래스 메서드 를 정의하는 방법이다.
    @classmethod

    def increment(cls):
        cls.class_variable += 1

# 받는 매게변수를 cls로 변경, 아래의cls.class_variable 의 코드를 실행
    def increments(cls, user):
        user.age += 1


# 원래 메서드를 불러 올때는, 메서드의 이름 을 불러와야 하는것 이지만, 여기에서는 변수를 불러왓다.
MyClass.increment()
print(MyClass.class_variable)
myage = MyClass("mark", 26)

# for i in range(0, 11, 1):
#     MyClass.increments()
#     print(MyClass.class_variable)
