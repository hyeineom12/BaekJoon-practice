num = input("")
text = input("")

numbers = ["1","2","3","4","5","6","7","8","9"]

result = ""

for char in num :
    if not char.isdigit() :
        result += char


if result == text :
    print("1")
else :
    print("0")


