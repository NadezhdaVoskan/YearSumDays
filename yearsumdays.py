print("Введите год:")
year = int(input())
monthWith31Day = 31  # янв,март,май,июль,авг,окт,дек = 7
monthWith30Day = 30  # апр,июнь,сент,нояб = 4
leapYear = 29
unleapYear = 28
sumDays = 0
dayInMonth = 1
oneNum = 0
twoNum = 0

for i in range(1, monthWith31Day):
    if i <= 8:
        dayInMonth += i + 1
    elif i <= 9:
        dayInMonth += 1
    elif i >= 10:
        oneNum = (i+1) // 10
        twoNum = (i+1) % 10
        dayInMonth += (oneNum + twoNum)
    print(dayInMonth)

sumDays = 7*dayInMonth
print(f"Кол-во дней: {sumDays}")

dayInMonth = 1
for i in range(1, monthWith30Day):
    if i <= 8:
        dayInMonth += i + 1
    elif i <= 9:
        dayInMonth += 1
    elif i >= 10:
        oneNum = (i+1) // 10
        twoNum = (i+1) % 10
        dayInMonth += (oneNum + twoNum)
    print(dayInMonth)

sumDays += 4*dayInMonth
print(f"Кол-во дней: {sumDays}")

if (year % 4 == 0 and not (year % 100 == 0)) or year % 400 == 0:
    dayInMonth = 1
    for i in range(1, leapYear):
        if i <= 8:
            dayInMonth += i + 1
        elif i <= 9:
            dayInMonth += 1
        elif i >= 10:
            oneNum = (i+1) // 10
            twoNum = (i+1) % 10
            dayInMonth += (oneNum + twoNum)
        print(dayInMonth)

    sumDays += dayInMonth
else:
    dayInMonth = 1
    for i in range(1, unleapYear):
        if i <= 8:
            dayInMonth += i + 1
        elif i <= 9:
            dayInMonth += 1
        elif i >= 10:
            oneNum = (i+1) // 10
            twoNum = (i+1) % 10
            dayInMonth += (oneNum + twoNum)
        print(dayInMonth)

    sumDays += dayInMonth

print(sumDays)
