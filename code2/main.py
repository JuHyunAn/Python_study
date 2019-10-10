class Cat():
    species = "russian blue"    # 공용적으로 사용될 변수(클래스 변수)

    def __init__(self, name):   # 개별적으로 사용될 변수(인스턴스 변수)
        self.name = name    # self.name은 하나의 객체, name은 단순 인자

cat1 = Cat("냥1")
cat2 = Cat("냥2")

print(cat1.species)     # print(객체.변수) = 해당 객체의 변수 값을 호출
print(cat2.species)

print(cat1.name)
print(cat2.name)