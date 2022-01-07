#23강
#할당 연산자 예제를 만들어보시오
a=100
a=a+3
print(a)

b=200
b=b+1
print(b)

#in(멤버십) 연산자 예제를 만들어보시오
lst = [1,2,3,4,5]
a=100 in lst
print(a)

tpl = 1,2,3
print(tpl, type(tpl))

#Boolean 연산자 예제를 만들어보시오
print(bool(1)) #파이썬에서 1은 참(True)을 의미
print(bool(0)) #파이썬에서 0은 거짓(False)을 의미
print(bool(-1)) #True로 나옴 왜지/ 신기하네

#print(bool(none)) err
print(bool(None)) #거짓으로 나옴

# 'None'?
#아무것도 없다는 type 중 하나 -> 타입체크 : NoneType -> 아무것도 없기 때문에 항상 거짓으로 출력
a=None
print(a, type(a))

