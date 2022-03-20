import math

# 素数を求めるジェネレータ
def get_prime():
    num = 2
    # 2から順に素数判定し、素数の場合だけyield(無限ループ)
    while True:
        if is_prime(num):
            yield num
        num += 1


# 引数valueが素数かどうかを判定
def is_prime(value):
    # 素数かどうかを表すフラグ
    result = True
    # 2～sqrt(value)で、valueを割り切れるものがあるか
    for i in range(2, math.floor(math.sqrt(value)) + 1):
        if value % i == 0:
            result = False
            break
    return result


# 素数を順に出力
for prime in get_prime():
    print(prime)
    # 素数が100を超えたところで終了
    if prime > 100:
        break
