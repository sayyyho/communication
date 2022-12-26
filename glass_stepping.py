from random import *

# path에서 0 : left, 1 : right | bridge에서 0 : 탈락 1 : 통과

def path_generator(num):
    select = random()
    if(select<=0.5):path[num] = 1
    else:path[num]=0
    num+=1
    if(num==glass_num):
        print("path : ", num)
        return
    path_generator(num)

def bridge_generator(num): 
    i = random()
    if (i > 0.5): 
        i = 0 #탈락
        j = 1 #성공
    else: 
        i = 1
        j = 0
    glass_bridge[num][0] = i #왼쪽 유리
    glass_bridge[num][1] = j #오른쪽 유리
    num+=1
    if(num == glass_num):
        print("bridge :" ,num)
        return
    bridge_generator(num)

def simulation():
    bridge_generator(0)
    path_generator(0)
    check = 0
    survival_index = 0
    for i in range(member):
        for j in range(glass_num):
            check+=1
            select = path[j]
            if(glass_bridge[j][select]== 0):
                print(glass_bridge)
                print("now j :", j)
                print(path)
                path[j]=abs(select-1) #0이면 1, 1이면 0
                print(path[j])
                break
        if(check>=glass_num):
            survival_index = i
            print("starting surviving member  :", survival_index)
            break
        path_generator(check) #이후 경로 재설정
    for i in range(survival_index, member):result[i] += 1
    return


# 성공 case


member, glass_num = map(int, input().split())
glass_bridge = [[0,0]for _ in range(glass_num)]
path = [0 for _ in range(glass_num)]
result = [0 for _ in range(member)]
simulation()
print(glass_bridge)
print(path)
print(result)