# Python 컬렉션(딕셔너리)

num_dic = {"a":"apple", "s":"samsung"}
# a = apple / s = samsung

print(num_dic["s"])     # samsung
print(num_dic["a"])     # apple

num_dic["l"] = "lg"     # l(lg) 새로운 키 추가
print(num_dic["l"])     # lg


for k in num_dic.keys():    # keys 메서드 = 딕셔너리 안의 모든 '키'를 나열
    print(k, end=" ")
# a s l

print("")

for v in num_dic.values():  # valuse 메서드 = 딕셔너리 안의 모든 '값'을 나열
    print(v, end=" ")
# apple samsung lg

print("")


# items 메서드 = 딕셔너리 안의 모든 '키/값'을 나열
for k, v in num_dic.items():
    print(k, v, end=" ")
# apple samsung lg a apple s samsung l lg

print("")

for k in num_dic.items():
    print(k, end=" ")
# ('a', 'apple') ('s', 'samsung') ('l', 'lg')