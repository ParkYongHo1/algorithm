a=int(input())
for _ in range(a):
    n,m=input().split()
    for i in m:
        print(i*int(n),end='') #end= 출력결과 이어붙이는 용도
    print()


