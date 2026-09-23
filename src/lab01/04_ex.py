m = int(input("Минуты: "))
m1 = m // 60
m2 = m % 60
print(f"{m1}:{m2:02d}", sep=':')