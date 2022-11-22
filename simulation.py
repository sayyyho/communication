import numpy as np
from random import uniform
d = 5
l = 3
A = 0 #바늘이 선에 걸치는 사건횟수
N = 1000000 #시행횟수
for _ in range(N): #몬테카를로 시뮬레이션 시행
    random_angle = uniform(0, np.pi) #0과 파이사이 랜덤 변수(theta)에 대한 난수 생성
    random_length = uniform(0,d/2) #0과 1사이의 랜덤 변수(x)에 대한 난수 생성 
    if((l/2) * np.sin(random_angle)>=random_length):A+=1 #1/2 * l * sin(theta) >= x이면 선과 걸침    
simulation_result = A/N #바늘이 걸치는 확률 계산 
mathematical_result = (2*l)/(d*np.pi) #수학적 결과값
if(simulation_result>mathematical_result):accuracy = mathematical_result/simulation_result # 정확도 비교를 위한 부분
else:accuracy=simulation_result/mathematical_result 
print("뷔퐁의 바늘 시행 횟수: ",N)
print("시뮬레이션 결과 :", simulation_result) 
print("수학적 결과 : ", mathematical_result)
print("정확도 :",accuracy)