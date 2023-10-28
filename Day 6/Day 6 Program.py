f = open("Day 6 Input.txt", "r")

fileinput = f.read()

f.close()


#Day 1


for i in range(len(fileinput)):
    if len(set(fileinput[i:i+14])) == 14:
        break

print(i+14)






#Day 2





