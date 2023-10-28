f = open("Day 7 Input.txt", "r")

fileinput = f.read()

f.close()


big_total = 0
options = []

class Directory_Tree:
    def __init__(self, parent = None):
        self.items = {}
        self.parent = parent

    def add_file(self, filename, filesize):
        self.items[filename] = filesize

    def add_dir(self, dirname):
        self.items[dirname] = Directory_Tree(self)

    def get_parent(self):
        return self.parent

    def get_dir(self, dir_to_get):
        return self.items[dir_to_get]

    def get_size(self):
        running_total = 0
        total = 0
        for i in self.items:
            if type(self.items[i]) == type(Directory_Tree()):
                temp_total = self.items[i].get_size()
                running_total += temp_total
            else:
                running_total += self.items[i]

        global options
        options.append(running_total)

        if running_total <= 100000:
            global big_total
            
            big_total += running_total
            

        return running_total



    

#Day 1

current = Directory_Tree() #This performs the first instruction
start = current

instructions = fileinput.splitlines()
del instructions[0] #This makes sure the first instruction is not repeated


while len(instructions) > 0:
    ins = instructions[0].split(" ")
    ins_copy = ins
    del instructions[0]
    if ins_copy[1] == "ls":
        while instructions[0][0] != "$":
            if instructions[0].startswith("dir "):
                current.add_dir(instructions[0][4:])
            else:
                file = instructions[0].split(" ")
                current.add_file(file[1], int(file[0]))
            del instructions[0]
            if len(instructions) == 0:
                break
    else:
        if ins_copy[2].endswith(".."):
            current = current.get_parent()
        else:

            current = current.get_dir(ins_copy[2])


            
used_space = start.get_size()


print(big_total)


#Day 2

space_to_remove = used_space - 40000000
best_so_far = 99999999999

for i in options:
    if i > space_to_remove:
        best_so_far = min(best_so_far, i)

print(best_so_far)
    



