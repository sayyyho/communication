from random import *
success = 0
trial = 100000
member = 20

for _ in range(trial): #몬테카를로 시뮬레이션 시행
    check = [0 for i in range (366)]
    for _ in range(member):
        random_number = randint(1,365)
        if(check[random_number]==0):check[random_number] = 1
        else:
            success +=1
            break
print(success/trial * 100)