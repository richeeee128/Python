#다중 할당 -> 여러 개의 값을 여러 개의 변수로 각각 저장 -> 한줄로 코드 작성.
a,b,c,d=100,3.14,'k','korea'
print(a,b,c,d)
print(a)

a=100,3.14,'k','korea'
print(a)

#100-6
#쌍따옴표, 홑따옴표가 출력되도록 코드를 작성해보시오.
sample_txt='나는 엄마에게 말했다. "더이상 카레는 먹기 싫어요!"라고...'
print(sample_txt)
#밖과 안이 다른 따옴표로 묶여야 한다.

#그렇지만 따옴표 두 개가 있다면?
sample_txt1='나는 엄마에게 말했다. "더 이상 \'카레\'는 먹기 싫어요!"라고...'
print(sample_txt1)

#' 앞에 백슬래시(\)를 넣어준다.

sample_txt2="나는 엄마에게 말했다. \"더 이상 '카레'는 먹기 싫어요!\"라고..."
print(sample_txt2)

#100-7
#id()함수
a='붕어빵'
print(a,id(a))

b=a
print(b,id(b))
#id=주소값

a='잉어빵'
print(a,id(a))