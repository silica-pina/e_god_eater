import random as rd

#rushセット数を決める 
#戻り値 セット数
def set():
    A = 2
    B = 2
    C = 1
    D = 1
    flg = 0
    while(True):
        r = rd.randint(1,100)
        if r <= 16:
            A -= 1
            flg += 1
        elif r <= 32:
            B -= 1
            flg += 1
        elif r <= 48:
            C -= 0
            flg += 1
        elif r <= 64:
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
        r = rd.randint(1,539)
        n += 1
        if r == 1: #当たり
            r = rd.randint(1,100)
            out += rush(set()) #ラッシュ中の出玉加算
            break
    res.append([n,out])#結果

#結果表示
print("[回転数, 出玉]")
for i in res:
    print(i)

