# Python 함수


# 별칭 함수
def sum(a, b):
    return a + b

s = sum     # sum 함수를 s라는 별칭으로 정의
print(s(10, 11))    # 21 (값을 직접 부여 가능)



# 1급 객체(함수)를 만족하기 위한 조건의 예제
def sum2(c, d):
    return c + d

def multiply(c, d):
    return c * d

func = [sum2, multiply]     # 1. 함수를 변수에 할당 할 수 있다.
print(func[0](3, 3), func[1](4, 4)) # 6, 16

def func1(a, b):
    return multiply(a, b)   # 2. 함수는 반환값으로 사용될 수 있다.

print(func1(2, 4))   # 8



# 기본 값(default 인자)
def sum3(x, y, z = 10):
    return x + y + z

print(sum3(1, 2))   # 디폴트 값으로 지정된 인자는 출력 시, 입력하지 않아도 연산됨
# 13


i = 0
def test(b = i):
    print(b)

i = 10
test()  # = print(test())   >   b = i(0) 디폴트 값으로 설정된 부분 출력
test(i) # = print(test(i))  >   b = i(10) 디폴트 값을 직접 설정한 부분 출력



# 가변 길이 인자
def sum4(*number, f1):
    sum4 = 0
    for i in number:
        sum4 += i
    return sum4 + f1

print(sum4(1, 2, 3, 4, 5, 6, 7, f1 = 1.0))  # 29.0

# '가변 길이 인자'는 개수의 제한 없이 함수에 인자를 넘겨줄 수 있다.

# print(sum4(f1 = 1.0, 1, ,2 ,3 ,4 ,5 ,6 ,7)) # SyntaxError 에러 발생!

# f1 같은 이름 있는 인자는 '가변 길이 인자' 뒤에 선언해야한다.



# 반환 값
def test1(a, b):
    return a, b

print(test1(1, 1))  # (1, 1)

t = test1(1, 1)
print(t, type(t))   # (1, 1) <class 'tuple'>

a, b = test1(1, 1)
print(a, b) # 1 1
