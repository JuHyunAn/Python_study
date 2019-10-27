# //////////////// 포멧팅 지시어 //////////////// 

test1 = "Life is too short, %s"     
# [%s]를 설정하여 해당 위치에 문자열이 추가될 수 있음을 나타냄
result1 = test1 % "You need Python."
# "You need Python." 이라는 문자열이 [%s]위치에 적용됨
print(result1)
# Life is too short, You need Python.


test2 = "Life is too short, %s %s %s"   # 쪼개서 사용...
result2 = test2 % ("You", "need", "Python.")
print(result2)
# Life is too short, You need Python.

'''
test3 = "Life is too short, %d"
result3 = test3 % "10"
print(result3)
# [%d]의 경우 정수를 받기 때문에, str 타입인 "10"을 받으면, 타입 에러 발생
# TypeError: %d format: a number is required, not str
'''

test4 = "Life is too short, %d"
result4 = test4 % 10
print(result4)
# Life is too short, 10


test5 = "Life is too short, %.2f"   # .2 소수점 둘째 자리까지 표현 (반올림)
result5 = test5 % 100.1654
print(result5)
# Life is tooo short, 100.17


test6 = "Life is too short, {} {} {}"
result6 = test6.format("You", "need", "Python.")    # format 함수를 통해 직접 지시어를 입력
print(result6)
# Life is too short, You need Python.



# //////////////// 이스케이프 문자(\) //////////////// 

test7 = "\"Life is too short\", \n\'You need Python.\'"
print(test7)
# \n(줄바꿈), \"(큰 따옴표), \'(작은 따옴표)
#   "Life is too short",
#   'You need Python.'

test8 = "Life is too short, You need Pythond\bd\bd\b." 
print(test8)
# \b(백스페이스)를 통해 글을 지우거나, 띄어쓰기 제거 등 가능
# Life is too short, You need Python.