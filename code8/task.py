# [ 과제 ] 예외 발생 시켜보기

# 'name' 인자를 인자로 입력하지 않으면 "이름이 필요합니다!"라는 예외가 발생하도록 작성

class Cat():
    
    def __init__(self, name):
        if not name:
            print("이름이 필요합니다!")
        self.name = name



cat = Cat("냥") # 에러 발생하지 않음

try:
    cat = Cat()   # 객체 생성에 필요한 인자인 "name"이 없기 때문에 TypeError 발생
except:
    print("Type Error 발생합니다!")

cat = Cat("")   # 에러 발생