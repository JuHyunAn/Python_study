import sub          # import 모듈명
print(sub.sum(1, 1))    # sub 파일 내 sum 함수를 불러옴

# 2


from sub import sum     # from 모듈명 import 함수
print(sum(1, 3))    # 위에서 가져올 모듈명과 함수를 모두 지정, 모듈명 생략 O

# 4


from sub import sum as s    # sub 모듈 내 sum 함수의 명칭을 s로 지정
print(s(1, 5))      # s = sum

# 6


from package import pck     # from 패키지명 import 모듈명
print(pck.sum(1, 6))

# 7


from package import pck as p
print(p.sum(1, 8))

# 9