a = float(input("a: ").replace(',', '.'))
b = float(input("b: ").replace(',', '.'))
sum = f"{a + b: .2f}"
avg = f"{(a + b)/2: .2f}"

print('sum=',sum,'; avg=', avg, sep = '')
