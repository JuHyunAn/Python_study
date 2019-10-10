from Package.sub.user import User   # from [user.py 경로명] import [클래스(함수)명]

student = User("안주현", "남성", "대한민국")

print(student.get_user_info())
print(student.get_species())