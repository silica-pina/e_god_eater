import random as rd
import matplotlib.pyplot as plt

#rushセット数を決める 
#戻り値 セット数
def set():
    A = 2
    B = 2
    C = 1
    D = 1
    flg = 0
    while(True):
        r = rd.randint(1,1000)
        if r <= 228:
            A -= 1
            flg += 1
        elif r <= 456:
            B -= 1
            flg += 1
        elif r <= 548:
            C -= 0
            flg += 1
        elif r <= 640:
            D -= 1
            flg += 1
        else:#通常
            flg += 0
            break
        
        if A == 0 or B == 0 or C == 0 or D == 0:
            break
    return flg

#rush
#引数   k:セット数
#戻り値 out:出玉
def rush(k):
    out = 0
    for i in range(k):
        while(True):
            r = rd.randint(1,1000)
            if r <= 802:
                out += 1500
            else:
                out += 150
                break
    return out


res = [] #結果格納

for i in range(10):
    n = 0   #回転数
    out = 1500 #出玉
    while(True):
        r = rd.randint(1,5392)
        n += 1
        if r <= 10: #当たり
            out += rush(set()) #ラッシュ中の出玉加算
            break
    res.append([n,out])#結果

#結果表示
data = []
p = 15 #１回転あたりの消費量
now = 0 #差玉
print("[回転数, 出玉]")
for i in res:
    now -= i[0]*p
    data.append(now)

    now += i[1]
    data.append(now)

    print(i)

plt.plot(data)
plt.show()

