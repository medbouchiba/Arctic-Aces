temp = []
result = []
with open("calibration.txt", "r") as file:
    for line in file:
        for x in line:
            if x.isnumeric():
                temp.append(x)
        Two_Digit_Number = temp[0] + temp[-1]
        result.append(Two_Digit_Number)
        temp = []
    print(result)

Final_Result = 0
for number in result:
    Final_Result += int(number)
print(Final_Result)
