import numpy as np
from random import uniform
import pandas as pd
# import matplotlib.pyplot as plt
d = 10 #바늘 사이의 거리
l = 5 #바늘의 길이
A = 0 #바늘이 선에 걸치는 사건횟수
N = 10000000 #뷔퐁의 바늘 시행횟수
rad_data = []
length_data = []
for _ in range(N): #몬테카를로 시뮬레이션 시행
    random_rad = uniform(0, np.pi) #0 ~ PI사이 랜덤 변수(theta)에 대한 N개의 무작위 샘플링
    random_length = uniform(0,d/2) #0과 1사이의 랜덤 변수(x)에 대한 N개의 무작위 샘플링
    rad_data .append(random_rad)
    length_data.append(random_length)
    if((l/2) * np.sin(random_rad)>=random_length):A+=1 #1/2 * l * sin(theta) >= x이면 선과 걸침, 모델    
simulation_result = A/N #바늘이 걸치는 확률 계산 
mathematical_result = (2*l)/(d*np.pi) #뷔퐁의 바늘 수학적 결과값
if(simulation_result>mathematical_result):accuracy = mathematical_result/simulation_result # 정확도 비교를 위한 부분
else:accuracy=simulation_result/mathematical_result 
print("set length(l):", l, "set distance(d):", d)
print("시뮬레이션 시행 횟수: ", N, "번", sep='')
# print("result of A :", A)
print("시뮬레이션 결과 :", format(simulation_result, '.15f')) 
print("수학적 분석 결과 : ", format(mathematical_result, '.15f'))
print("정확도 : ",accuracy*100, "%", sep='')
# print("radian(x) min :", format(min(rad_data), '.15f'), "\nradian(x) max :" , format(max(rad_data), '.15f'))
# print("length(l) min : ", format(min(length_data), '.15f'), "\nlength(l) max : ", format(max(length_data), '.15f'))
pd.set_option('float_format', '{:.10f}'.format)
rad_data = pd.Series(rad_data)
length_data = pd.Series(length_data)
print("radian(x) data set\n--------------------------\n",rad_data.describe(), "\n", sep='')
print("length(l) data set\n--------------------------\n" , length_data.describe(), sep='')