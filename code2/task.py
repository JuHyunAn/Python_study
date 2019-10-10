class User():
    old = "29살"

    def __init__(self, name, gender, city):
        self.name = name
        self.gender = gender
        self.city = city


    def get_user_info(self):     # 변수 정보를 self 변수에서 가져옴
        return "이름:" + self.name + "\n성별:" + self.gender + "\n사는 곳:" + self.city

    def get_old(self):   # 그냥 self로 처리...어차피 old는 전역변수(고정 값)
        return "열심히 공부하는 " + self.old + " 학생입니다!"


user = User("안주현", "남성", "안양")
print(user.get_user_info())
print(user.get_old())



# 아래와 같은 결과가 나오도록 return 값을 채우기

# 이름: 안주현
# 성별: 남성
# 사는 곳: 안양
# 열심히 공부하는 29살 학생입니다!