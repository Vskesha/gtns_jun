greeting = 'Привіт, світ!'

slice3 = greeting[1:4]
print(slice3)

last_word = greeting[-5:-1]
print("Останнє слово --", last_word)

first_word = greeting[:6]
print("Перше слово --", first_word)

empty_slice = greeting[4:2]
print("Порожній зріз -- ", empty_slice)
# print(type(empty_slice))
# print(empty_slice == "")

print()
two_row_str = "Перший рядок\nДругий рядок"
print(two_row_str)
