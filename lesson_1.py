# задание 1: Заменить все буквы "x" на "y"

sourceString = "jidxncndxxscedj djcj ddcoysnxks"
newString = ""

for x in sourceString:
    if x == "x":
        newString += "y"
    else:
        newString += x

print(sourceString)
print(newString)

# задание 2: Сосчитать произведение чисел кратных 3 и 5

nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 4, 5, 6, 7]
comp = 1

for x in nums:
    if x % 3 == 0 or x % 5 == 0:
        comp *= x

print(comp)

# задание 3: Заменить все буквы "x" на "y" в исходной строке без использования дополнительной

sourceString = sourceString.replace("x", "y")

print(sourceString)
