x = {1:"R", 22:"A"}  #사전자료형
print(x[1])
print(x.get(1))

print(1 in x)  #True   안에 들어 있는지 확인
print(5 in x)   #False

x[3] = "L"   #사전에 값 추가
x[22] = "M"   #사전 값 변경
print(x)

del x[3]  #값 삭제
print(x)


print(x.keys())  #키 출력


print(x.values())   #값 출력


print(x.items())  #다 출력


x.clear()    #다 삭제

