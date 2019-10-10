# python 컬렉션(list_dict)

num_list = [1, 2, 3, 4, 5]

# 인덱스 0부터 시작
print(num_list[0])  # 1


# 뒤에서 부터 시작할 경우, 음수(-) 사용
print(num_list[-1]) # 5


for i in num_list:  # in (맴버십 연산자)
    print(i)    # 1, 2, 3, 4, 5 (num_list 내 인덱스를 산출)


# 슬라이싱 (범위) [인덱스 시작:끝-1]
print(num_list[0:3])    # 인덱스 0 ~ 2(3-1)까지 = 1, 2, 3
print(num_list[2:4])    # 인덱스 2 ~ 3(4-1)까지 = 3, 4
print(num_list[1:])     # 인덱스 1 ~ 마지막까지 = 2, 3, 4, 5


# append 메서드를 통해 인덱스 값을 '추가' 할 수 있다.
num_list.append(6)
num_list.append(7)
num_list.append(8)
print(num_list)


# del 키워드를 통해 인덱스 값을 '삭제'할 수 있다.
del num_list[6]     # 6번째 인덱스 값을 삭제
del num_list[0]     # 0번째 인덱스 값을 삭제
print(num_list)


# 여기까지 num_list = [2,3,4,5,6,8]
# len(num_list) = 6
del num_list[len(num_list) - 2]     # = del num_list[4]
print(num_list)


# 특정 인덱스 값을 다른 값으로 '수정(or추가)' 할 수 있다.
num_list[4] = 9
print(num_list)


num_dict = {"a":"An", "j":"Ju"}     # {a:b} a는 곧 b를 나타냄
print(num_dict["a"])    # An


for c, d in num_dict.items():
    print(c, d)


num_dict["h"] = "Hyun"      # 기존에 해당 키가 있으면 수정, 없으면 추가
print(num_dict.get("k"))    # k라는 키워드는 없으므로, None
print(num_dict.get("a"))    # An