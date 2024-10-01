

# class Ai_student:
#     def __init__(self,inputname):
#         self.name = inputname

#     def greet (self):
#         print("Hello my name is", self)

# alice = Ai_student("Alice")
# #

class character:
    def __init__(self, name, character_class, level):
        self.name = name
        self.character_class = character_class
        self.level = level
        self.skill_upgrade = False

    def new_skill(self) :
        if not self.skill_upgrade:
            if self.level > 50:
                self.skill_upgrade = True
                print("Now you can use new skill")
            else:
                print("level is low for new skill")
        else:
            print("no more new skill exist")

    def class_detail(self) :
        print(f"Name: {self.name}")
        print(f"Class: {self.character_class}")
        print(f"level: {self.level}")


# 객체 생성 및 메서드 호출하기

my_character = character("Mark", "Warrior", 100)
# character 클래스에 인스턴스 생성

my_character.new_skill()
# 출력 : Now you can use new skill

my_character.class_detail()


