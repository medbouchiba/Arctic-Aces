i_redMax = 12
i_greenMax = 13 
i_blueMax = 14  

b_gameTest = True
i_result = 0

# open the file
f_file = open('C:/Users/devang.darode/OneDrive - Accenture/Documents/Projects/Advent of Code 2023/Arctic-Aces/SecondDay_CubeConundrum/Input.txt')

# read the content of first line
s_line = f_file.readline()
i_gameID = 1

# iterate till the input read is not blank
while s_line != "":

    # Handle the line read here
    b_gameTest = True
    l_gameId = s_line.split(":")    # split- Game 1: 12 blue; 2 green format
    print(l_gameId[0])
    l_gameSet = l_gameId[1].split(";")      # split- 12 blue: 2 green, 12 blue
    # l_gameSet = ["12 blue", "2 green, 13 blue, 19 red", "13 red, 3 green, 14 blue"]
    i_gameSetlength = len(l_gameSet)

    for i in range(i_gameSetlength):
        l_ballsShown = l_gameSet[i].split(',')
        # l_ballsShown = ["2 green", "13 blue", "19 red"]

        for n in range(len(l_ballsShown)):
            l_eachPick = l_ballsShown[n].strip().split(" ")
            print(l_eachPick[0])
            if l_eachPick[1] == "red" and int(l_eachPick[0]) > i_redMax:
                b_gameTest = False
            elif l_eachPick[1] == "blue" and int(l_eachPick[0]) > i_blueMax:
                b_gameTest = False
            elif l_eachPick[1] == "green" and int(l_eachPick[0]) > i_greenMax:
                b_gameTest = False
    print(b_gameTest)

    if b_gameTest:
        i_result += i_gameID

    """
    1. go through each game
    2. split each game to sets in list
    3. split each set to the color
    4. read the number of balls for each color
    5. check these numbers with max balls available
    6. if the number of balls satify, add the game ID
    """


    # read the next line
    s_line = f_file.readline()
    i_gameID += 1
print(i_result)
f_file.close()