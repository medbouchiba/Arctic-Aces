xcn = 0
ycn = 0
xcs = 0
ycs = 0
cnt = 0
a_cnt = 0
n_coordinates = []
s_coordinates = []
sub = []
final = []

with open("input.txt", 'r') as file:
    for line in file:
        line = list(line.strip("\n"))
        for i in line:
            if i.isnumeric():
                xcn = line.index(i)
                ycn = cnt
                sub.append({i: (xcn, ycn)})
                index = line.index(i)
                line[index] = "."
            elif not i.isalpha() and i != "." and not i.isnumeric():
                if sub:
                    n_coordinates.append(sub)
                    sub = []
                xcs = line.index(i)
                ycs = cnt
                s_coordinates.append({i: (xcs, ycs)})
                index = line.index(i)
                line[index] = "."
            else:
                if sub:
                    n_coordinates.append(sub)
                    sub = []
        cnt += 1

for j in s_coordinates:
    for s_key, s_value in j.items():
        for bloc in n_coordinates:
            if a_cnt != 0:
                a_cnt = 0
            for unit in bloc:
                if a_cnt == 1:
                    break
                else:
                    for n_key, n_value in unit.items():
                        if a_cnt == 1:
                            break
                        else:
                            if s_value[1] == n_value[1] or \
                                    s_value[1] == (n_value[1] - 1) or \
                                    s_value[1] == (n_value[1] + 1):
                                if s_value[0] == n_value[0] or \
                                        s_value[0] == (n_value[0] - 1) or \
                                        s_value[0] == (n_value[0] + 1):
                                    number = ""
                                    for m in bloc:
                                        for key, value in m.items():
                                            number += key
                                    final.append(number)
                                    a_cnt = 1
                                    break

sum_final = 0
for s in final:
    sum_final += int(s)
print(sum_final)
