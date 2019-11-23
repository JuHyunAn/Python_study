# Python 예외 처리

# try ~ catch 구문

# 각 코드를 상황에 따라 3가지 구문에 묶어서 적용시킴

'''
try:
    실행코드    <- 에러 가능성 존재

except:
    예외 발생시 실행코드 <- 1번

finally:
    무조건 실행되는 코드 <- 2번
'''

test = [1, 2, 3]
try:
    print(test[2])  # 3
except:
    print("인덱스 에러 발생!")  # 예외 사항 없으므로, 코드 실행되지 않음
finally:
    print("무조건 실행되는 코드!")


test1 = [1, 2, 3, 4]
try:
    print(test1[4])  # 없는 4번 인덱스를 호출 -> 예외 사항 발생!
except:
    print("인덱스 에러 발생!")  # 예외 사항 발생으로, 코드 실행됨
finally:
    print("무조건 실행되는 코드!")


test3 = 20
if test3 == 20:
    raise Exception("test3 is 30.")
'''
Traceback (most recent call last):
  File "main.py", line 38, in <module>
    raise Exception("test3 is 30.")
Exception: test3 is 30.
'''
# raise Exception 코드는 인위적으로 예외를 발생시킴