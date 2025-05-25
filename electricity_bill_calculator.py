from decimal import Decimal
from num2words import num2words

boshi = Decimal(input("Oy boshidagi hisoblagichdagi raqamni kiriting: "))
oxiri = Decimal(input("Oy oxiridagi hisoblagichdagi raqamni kiriting: "))
kWh = Decimal('0.45')

bir_oyda = round((oxiri - boshi)*kWh, 2)

print(f"To'lov: ${bir_oyda} (ENG: {num2words(bir_oyda, lang='eng', to='currency', currency='USD')} RUS: {num2words(bir_oyda, lang='ru', to='currency', currency='USD')})")