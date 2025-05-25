from num2words import num2words
total = int(input("Pul miqdorini kiriting ($): "))
amount = total

k_50 = amount // 50
amount = amount % 50
print("$50 kupyuradan:", k_50, "ta")

k_10 = amount // 10
amount = amount % 10
print("$10 kupyuradan:", k_10, "ta")

k_5 = amount // 5
amount = amount % 5
print("$5 kupyuradan:", k_5, "ta")

k_1 = amount // 1
amount = amount % 1
print("$1 kupyuradan:", k_1, "ta")

print(f"Umumiy summa: ${total} ({num2words(total, lang='en')}, {num2words(total, lang='ru')})")