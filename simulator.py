import random as rd

#rushセット数を決める 
#引数   r:乱数
#戻り値 セット数
def set(r):
    if r <= 7:
        return 3
    elif r <= 32:
        return 2
    elif r <= 64:
        return 1
    else:
        return 0

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
            out += rush(set(r)) #ラッシュ中の出玉加算
            break
    res.append([n,out])#結果

#結果表示
print("[回転数, 出玉]")
for i in res:
    print(i)

