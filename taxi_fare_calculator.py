from decimal import Decimal
from num2words import num2words

start_price = Decimal("3.00")
rate_per_km = Decimal("1.20")

distance = Decimal(input("Masofani kiriting = "))
total_price = round((distance * rate_per_km + start_price), 2)

print(f"Yetkazib berish narxi: ${total_price} (ENG: {num2words(total_price, lang='en', to='currency', currency='USD' )}. RUS: {num2words(total_price, lang='ru', to='currency', currency='USD')})")
