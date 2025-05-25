from decimal import Decimal
from num2words import num2words

print("Menga haftalik harajatlaringizni yuburing!")

day1 = Decimal(input("Dushanba: "))
day2 = Decimal(input("Seshanba: "))
day3 = Decimal(input("Chorshanba: "))
day4 = Decimal(input("Payshanba: "))
day5 = Decimal(input("Juma: "))
day6 = Decimal(input("Shanba: "))
day7 = Decimal(input("Yakshanba: "))

average = (day1+day2+day3+day4+day5+day6+day7)/7

print(f"O'rtacha harajad: ${average:.2f} (ENG: {num2words(average, lang='en', to='currency', currency='USD')}. RUS: {num2words(average, lang='ru', to='currency', currency='USD')})")