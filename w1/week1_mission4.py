line = int(input("Diamond 의 길이를 입력하세요(2~30) : "))

for i in range(1, line * 2, 2):
    print(("0" * ((line * 2 - i - 1) // 2)) + ("1" * i) + ("0" * ((line * 2 - i - 1) // 2)))

for i in range(line * 2 -3, 0, -2):
    print(("0" * ((line * 2 - i) // 2) + ("1" * i)) + ("0" * ((line * 2 - i) // 2)))