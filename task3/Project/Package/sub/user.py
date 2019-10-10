# User 클래스를 main.py에서 불러와 사용할 수 있도록 import 구문을 작성

class User():
    specise = "안주현은 프로그래밍 학생입니다."

    def __init__(self, name, gender, city):
        self.name = name
        self.gender = gender
        self.city = city

    def get_user_info(self):
        return "이름은: " + self.name + "\n성별: " + self.gender + "\n사는 곳: " + self.city

    def get_species(self):
        return self.specise