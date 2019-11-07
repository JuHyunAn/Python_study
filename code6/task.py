# [ 과제 ] formatting, split 문자열 메서드 사용하기


test_string = "My name is Juhyeon An"
print(test_string.split())
# ['My', 'name', 'is', 'Juhyeon', 'An']

test_string2 = "I can see you, I can't see you"
print(test_string2.split(','))
# ['I can see you', " I can't see you"]


for i in test_string.split():
    print(i)

for a in test_string2.split():
    print(a, end=' ')
print(' ')


replace1 = test_string.replace('Juhyeon', 'The great')
print(replace1)
# My name is The great An

replace2 = test_string2.replace("I can't see you", 'you too')
print(replace2)
# I can see you, you too

for b in replace1:
    print(b, end='')

print(' ')

for c in replace2:
    print(c, end=' ')