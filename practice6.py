#문자열의 순서는 0부터 시작
x = "123456789"
 
print("번호:" + x[2])
print("번호2자리:" + x[0:2])
print("번호 거꾸로3자리:" + x[-4:-1])


G = "Game is Amazing"
print(G.lower())
print(G.upper())
print(len(G))
print(G.replace("Game", "VR"))

x = G.index("a")
print(x)

print(G.count("m"))
