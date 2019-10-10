# Python 컬렉션 set, tuple

# Tuple(튜플)
num_tuple = (1, 2, 3)       # tuple 은 소괄호()로 선언
# num_tuple[0] = 0      # TypeError : tuple 객체는 값의 추가를 지원 X
# del num_tuple[0]      # TypeError : tuple 객체는 값의 삭제를 지원 X
print(num_tuple)



# Set(셋)
num_set = {1, 1, 2, 2, 3, 3}         # set 은 중괄호{}로 선언
print(num_set)          # {1, 2, 3} -> 중복을 제거하고 산출!

num_set.add(4)              # add 메서드를 통해 값을 추가
print(num_set)          # {1, 2, 3, 4}


set1 = {1, 2, 3, 4}
set2 = {1, 2, 3}
# 교집합(&)
print(set1 & set2)      # {1, 2, 3}
# 합집합(|)
print(set1 | set2)      # {1, 2, 3, 4}
# 차집합(-)
print(set1 - set2)      # {4}


# 객체의 타입을 변환시킬 수 있다.
test_list = [1, 2, 3, 1, 2, 3]
print(set(test_list))   # {1, 2, 3} -> list 타입에서 set 타입으로 변환됨