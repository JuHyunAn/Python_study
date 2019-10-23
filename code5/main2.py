# 내장 함수(sorted, lambda, map, filter)

# built-in functions : 이미 만들어진 함수들 (내장 함수!)

'''
1. sorted 함수 
sorted(iterable, key=None, reverse=False)
 - key, reverse는 작성하지 않으면 기본 값으로 설정됨
 - interable은 반복 가능한 요소
 - key는 정렬 기준을 명시
 - reverse는 오름/내림차순을 지정 (기본 값 = 오름 차순)
'''

numbers = [1, 7, 4, 3, 9]
numbers = sorted(numbers)   # reverse=False(생략)
print(numbers)
# [1, 3, 4, 7, 9]   오름 차순

numbers = sorted(numbers, reverse=True)
print(numbers)
# [9, 7, 4, 3, 1]   내림 차순



'''
2. map 함수
map(function, interable)
 - 자료형 요소들이 함수에 의해 실행된 결과를 묶어서 리턴
 - 별도의 함수를 먼저 정의하고, 
(순서가 있는)자료형을 해당 함수에 반영하여 결과를 모두 반환받고자 할 경우에 사용
'''

def double(x):
    return x * 2    # double 이라는 함수를 먼저 정의한다.

numbers = [1, 2, 3, 4, 5]
numbers = list(map(double, numbers))    # map(함수, 자료형)
print(numbers)
# [2, 4, 6, 8, 10]

def cost(y):
    return y + 1

months = [9, 10, 11, 12]
months = list(map(cost, months))
print(months)
# [10, 11, 12, 13]



'''
3. filter 함수
filter(function, interable)
 - 정의된 함수의 반환 값은 True, False, None 형태의 논리적 반환 값
 - 함수의 연산 결과가 참(True)인 요소만 반환
'''

def grater_than_1(x):   # 조건부 함수 선언
    return x > 2

members = [1, 2, 3, 4, 5]
members = list(map(grater_than_1, members))
print(members)
# [False, False, True, True, True]
# map 함수의 경우, 조건 충족 여부에 따라 True/False로 반환

members2 = [1, 2, 3, 4, 5, 6]
members2 = list(filter(grater_than_1, members2))
print(members2)
# [3, 4, 5, 6]
# filter 함수의 경우, 결과가 참(True)인 값만 반환



'''
4. lambda 함수
lambda parameters : expression
 - parameters 부분에 함수의 인자를 작성
 - 같은 결과를 나타내는 함수를 짧은 코드로 작성할 수 있어 효율적
 - 함수 구문이 작성될 수 없는 부분에도 람다 표현식 사용 가능
'''
# 위 map/filter 함수에서 사용한 함수를 람다식으로 표현

numbers_L = [1, 2, 3, 4, 5]

# numbers_L = list(map(double, numbers_L))    # 기존
double = list(map(lambda x: x * 2, numbers_L))   # 람다식으로 표현

# numbers_L = list(filter(grater_than_1, numbers_L))  # 기존
grater_than_1 = list(filter(lambda x: x > 2, numbers_L)) # 람다식으로 표현

print(double)   # [2, 4, 6, 8, 10]
print(grater_than_1)    # [3, 4, 5]