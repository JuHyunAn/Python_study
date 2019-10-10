# Python 컬렉션(리스트)

num_list = [1, 2, 3, 4, 5]
double_list = [num_list, num_list]
print(type(num_list))   # list 타입


for a in num_list:
    print(a, end='')    # end='' 를 통해 출력 값을 공백으로 구분하여, 한 줄에 출력 가능
# 1, 2, 3, 4, 5 (정수)

print('')

for j in double_list:
    for h in j:
        print(h, end='')
# 1, 2, 3, 4, 5, 1, 2, 3, 4, 5

print('')

num_list[len(num_list) - 2] = 6     # len 인덱스 길이 x (값의 길이 o)
print(str(num_list))
print(type(str(num_list)))  # str로 감싸주었기 때문에 문자열 타입
# [1, 2, 3, 6, 5]


num_list = num_list + num_list
print(num_list)
print(type(num_list))
# [1, 2, 3, 6, 5, 1, 2, 3, 6, 5]


num_list = num_list * 2
print(num_list)
# [1, 2, 3, 6, 5, 1, 2, 3, 6, 5, 1, 2, 3, 6, 5, 1, 2, 3, 6, 5]


double_list[1] = []
print(double_list)
# double_list = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
# [[1, 2, 3, 4, 5], []]


num_list.append(7)
num_list.append(8)
print(num_list)
# [1, 2, 3, 6, 5, 1, 2, 3, 6, 5, 1, 2, 3, 6, 5, 1, 2, 3, 6, 5, 7, 8]

double_list.append(6)
double_list.append(7)
print(double_list)
# [[1, 2, 3, 4, 5], [], 6, 7]


del num_list[3]
del num_list[7]     # 위에서 3번 인덱스 삭제, 8번 > 7번 인덱스로 변경 (-1)
del num_list[11]    # 13번 > 11번 (-2)
del num_list[15]    # 18번 > 15번 (-3)
print(num_list)    # 6을 전부 지우자!
# [1, 2, 3, 5, 1, 2, 3, 5, 1, 2, 3, 5, 1, 2, 3, 5, 7, 8]

del double_list[1]  # 앞서 바꾼 index 1 = []를 지우자!
print(double_list)
# [[1, 2, 3, 4, 5], 6, 7]


# 리스트 슬라이싱
print(num_list[2:5])    # 인덱스 2 ~ 4(5-1)까지
# [3, 5, 1]

print(num_list[5:-5])   # 인덱스 5 ~ 12(17-5)까지
# [2, 3, 5, 1, 2, 3, 5, 1]

print(num_list.pop(len(num_list) - 2))  # 16번 인덱스를 삭제 & 산출
# 7