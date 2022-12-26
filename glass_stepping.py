from random import *

def path_update(num):
    select = random()
    if(select<=0.5):path[num] = 1
    else:path[num]=0
    num+=1
    if(num==glass_num):return
    path_update(num)

def bridge_generator(num): 
    i = randint(0,1)
    glass_bridge[num][0] = i #왼쪽 유리
    glass_bridge[num][1] = abs(i-1) #오른쪽 유리
    num+=1
    if(num == glass_num):return
    bridge_generator(num)

def simulation():
    bridge_generator(0)
    path_update(0)
    check = 0
    member_index = 0
    survival_index = -1 # not find
    while(member_index+1 != member):
        for j in range(check, glass_num):
            check+=1
            select = path[j]
            if(glass_bridge[j][select]== 0):
                member_index+=1
                path[j]=abs(select-1)
                break
        if(check==glass_num):
            survival_index = member_index
            break
        else: path_update(check) 
    if (survival_index!=-1):
        for i in range(survival_index, member):result[i] += 1
    return


glass_num, member = map(int, input().split())
result = [0 for _ in range(member)]
attempt = 1000000
for _ in range(attempt):
    glass_bridge = [[0,0]for _ in range(glass_num)]
    path = [0 for _ in range(glass_num)]
    simulation()
    # print(glass_bridge)
    # print(path)
print("시행 횟수 : ", attempt)
for i in range(member):
    val = result[i] / attempt *100
    print(i+1,f"번째의 생존 확률 :  {val:.3f} %")
print(result)