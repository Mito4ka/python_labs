price = float(input("price="))
disc = float(input("discount="))
vat = float(input("vat="))
base = price * (1 - disc/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print('База после скидки:', f"{base: .2f}", '₽' )
print('НДС:              ', f"{vat_amount: .2f}", '₽')
print('Итог к оплате:    ', f"{total: .2f}", '₽')