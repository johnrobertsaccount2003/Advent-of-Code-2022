import os

directory = os.getcwd()

for i in range(1, 26):
    day_string = "Day " + str(i)
    os.mkdir(day_string)
    f = open(directory + "\\" + day_string + "\\" + day_string + " Program.py", "w")
    f.write("""f = open("%s Input.txt", "r")\n\nfileinput = f.read()\n\nf.close()\n\n\n#Day 1\n\n\n\n\n\n\n#Day 2\n\n\n\n\n\n""" % (day_string))
    f.close()
    f = open(directory + "\\" + day_string + "\\" + day_string + " Input.txt", "w")
    f.close()
