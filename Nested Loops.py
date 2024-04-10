List = [1, 2, 3, 3, 3, 4, 5, 7, 8, 6, 6]
List2 = []
for number in List:
    if number not in List2:
        List2.append(number)
print(List2)
