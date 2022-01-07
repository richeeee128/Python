#9강
# == 연산자
a= [1,2,3,4,5]
b=a
c=[1,2,3,4,5]

print(a==b)
print(a==c)
print(b==c)
#모두 True
# == 연산자는 오브젝트의 데이터 값이 같은지를 확인하고자 할 때 사용한다.


#10강
#is, == 연산자 복습

#[1]숫자
a=101
b=100+1
 #101이라는 새로운 방을 만드는 것은 비효율적이라 기존에 있는걸 가리킴
print(a is b) #같은 곳을 가리키고 있는가? T
print(a==b) #같은 값인가? T

#[2]문자열
c='korea'
d='korea'

print(c is d) #T
print(c==d) #T

#[3]리스트
e=[1,2,3,4,5]
f=[1,2,3,4,5]

print(e is f) #F
print(e==f) #T


