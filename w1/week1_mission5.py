def gugudan_check():
    try:
        num = int(input("구구단 중 몇 단을 입력하겠습니까?: "))
        for i in range(1, 10):
            print("{} * {} = {}".format(num, i, num * i))
    except ValueError:
        print("숫자를 입력해야지.. ")
        gugudan_check()

gugudan_check()





