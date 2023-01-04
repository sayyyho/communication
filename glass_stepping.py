import random
import math
import matplotlib.pyplot as plt

def update_path(now):
    path[now] = random.randint(0,1)
    now+=1
    if(now==glass_num):return
    update_path(now)

def generate_bridge(num): 
    random_glass = random.randint(0,1)
    glass_bridge[num][0] = random_glass 
    glass_bridge[num][1] = abs(random_glass-1) 
    num+=1
    if(num == glass_num):return
    generate_bridge(num)

def simulation():
    check = 0
    generate_bridge(0)
    update_path(0)
    current_member = 0
    survival_index = -1 # not find
    while(current_member + 1 != member):
        for j in range(check, glass_num):
            check+=1
            select = path[j]
            if(glass_bridge[j][select] == 0):
                current_member+=1
                path[j]=abs(select-1)
                break
        if(check==glass_num):
            survival_index = current_member
            break
        else: update_path(check) 
    if (survival_index!=-1):
        for i in range(survival_index, member):result[i] += 1
    return member - survival_index

def calculate_mathematical_probability():
    total = 0
    case = []
    mathematical_result = []
    for i in range(glass_num):
        total += math.comb(glass_num, i)
        if(i<member):
            case.append(total)
    
    for i in range(member):
        mathematical_result.append(case[i]/total *100)
        print(i+1, "번째 선택자의 수학적 생존 확률 : " , format(case[i]/total *100, ".5f"), "%", sep="")
    # print(mathematical_result)
       
    plt.bar(mark_number, mathematical_result)
    plt.show()



glass_num, member = map(int, input("please input glass data and people data : ").split())
result = [0 for _ in range(member)]
mark_number = [i for i in range(1, member+1)]
total_survival = 0
attempt = 10000
for _ in range(attempt):
    glass_bridge = [[0,0]for _ in range(glass_num)]
    path = [0 for _ in range(glass_num)]
    total_survival += simulation()
avg_survival = total_survival/attempt
simulation_result = []
print("시뮬레이션 횟수 :", attempt, "|" " 유리판 수 :", glass_num, "|" " 인원 수 :", member)
for i in range(member):
    print(i+1,"번이 생존 확률 : ", format(result[i] / attempt *100, ".4f"), "%", sep="")
    simulation_result.append(result[i] / attempt *100)
plt.bar(mark_number, simulation_result)
plt.show()
print("번호 별 살아남은 횟수", result, sep="")
print("평균 생존 인원 : ", format(avg_survival, ".4f"), "명", sep="")
calculate_mathematical_probability()
