# Advent of Code day 1 Task

# Part one Solution, only counting mumerals
# l_searcher = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Part two solution
l_searcher = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

l_numbersFound = []
i_sum = 0

# open the file
f_file = open('C:/Users/devang.darode/OneDrive - Accenture/Documents/Projects/Advent of Code 2023/Arctic-Aces/First Day - Trebuchet/Input.txt')

# read the content of first line
s_line = f_file.readline()

# iterate till the input read is not blank
while s_line != "":

    # Handle the line read here
    i_indexFirstDigit = 100
    i_indexSecondDigit = -1
    s_firstDigit = "0"
    s_secondDigit = "0"

    # iterate for each value in the searcher list
    i  = 0
    while i < len(l_searcher):

        # finding the first digit
        i_tempIndexFirstDigit = s_line.find(l_searcher[i])
        if i_tempIndexFirstDigit >= 0:
            # if the detected value is on the left, then take that value
            if i_tempIndexFirstDigit < i_indexFirstDigit:
                i_indexFirstDigit = i_tempIndexFirstDigit
                s_firstDigit = str(i % 10)
 
        # finding the second digit       
        i_tempIndexSecondDigit = s_line.rfind(l_searcher[i])
        if i_tempIndexSecondDigit >= 0:
            if i_tempIndexSecondDigit > i_indexSecondDigit:
                i_indexSecondDigit = i_tempIndexSecondDigit
                s_secondDigit = str(i%10)
        i += 1

    i_number = int(s_firstDigit + s_secondDigit)
    l_numbersFound.append(i_number)

    # read the next line
    s_line = f_file.readline()
f_file.close()

print (l_numbersFound)

for n in range(0, len(l_numbersFound)):
    i_sum += l_numbersFound[n]

print(i_sum)