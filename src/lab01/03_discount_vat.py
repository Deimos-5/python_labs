price=int(input("Цена: "))
discount=int(input("Скидка: "))
vat=int(input("Налог: "))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"База после скидки: {base} ₽")
print(f"НДС:               {vat_amount} ₽")
print(f"Итого к оплате:    {total} ₽")