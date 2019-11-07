# Python 함수

'''
1. 기본 형식

def 함수명(인자, default=값):
    실행코드
return 반환값;
'''

def sum1(x, y, default = 1):     # default 값을 먼저 할당
    return x + y + default

x = 1
y = 2
print(sum1(x, y))    # 4
# 함수식에서 먼저 할당된 값은 print 할때 인자를 입력하지 않아도 됨

print(sum1(x, y, 5))
# print 시, 해당 인자에 값을 직접 입력하여, 먼저 할당된 값을 변경할 수 있다.


'''
2. 가변 인자

def 함수명(인자, *인자):
    실행코드
return 반환값;
'''
def list1(x, *y):    # 인자의 값을 특정지을 수 없을 때 사용!
    sum_list = []
    for i in y:
        sum_list.append(i)
    print(sum_list)
list1(1, 1, 2, 3, 4, 5)  # = print(sum2(1, 1, 2, 3, 4, 5))
# sum2 함수 안에 이미 print 함수가 있어 생략 가능
# [1, 2, 3, 4, 5]


'''
3. 별칭 인자

def 함수명(별칭):
    실행코드(별칭사용)
return 반환값;
'''

def sum2(one, two):
    return one + two
print(sum(one = 1, two = 2))    # 인자에 별칭을 부여하여 사용가능


'''
4. 다중 반환 값

def 함수명(별칭):
    실행코드(별칭사용)
return 반환값, 반환값, 반환값...;
'''
# 반환값의 순서에 주의!!