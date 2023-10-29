f = open("Day 13 Input.txt", "r")

fileinput = f.read()

f.close()


#Part 1 and Part 2

count = 0
number = 0

class InputString:
    def __init__(self, value):
        self.value = eval(value)

    def __lt__(self, other):
        result, final = compare(self.value, other.value)
        return result

def compare(a, b):
    current = -1
    success = True
    while True:
        current += 1
        
        if current >= len(a) and not (current >= len(b)):
            return True, True
            
        elif not (current >= len(a)) and  (current >= len(b)):
            return False, True
        
        elif current >= len(a) and current >= len(b):
            return True, False

        else:
            if isinstance(a[current], int) and isinstance(b[current], int):
                if a[current] < b[current]:
                    return True, True
                elif b[current] < a[current]:
                    return False, True
            elif isinstance(a[current], list) and isinstance(b[current], list):
                success, final = compare(a[current], b[current])
                if final:
                    return success, True
            elif isinstance(a[current], int) and isinstance(b[current], list):
                success, final = compare([a[current]], b[current])
                if final:
                    return success, True                  
            elif isinstance(a[current], list) and isinstance(b[current], int):
                success, final = compare(a[current], [b[current]])
                if final:
                    return success, True
            else:
                print(type(a[current]), type(b[current]), "error")



values = fileinput.split("\n\n")

for case in values:
    number += 1
    a = eval(case.split("\n")[0])
    b = eval(case.split("\n")[1])


    success, final = compare(a, b)
    if success:
        count += number


print(count)

    

    

#Day 2


to_be_sorted = []
for i in fileinput.split():
    to_be_sorted.append(InputString(i))




to_be_sorted.append(InputString("[[2]]"))
to_be_sorted.append(InputString("[[6]]"))

k=0
for i in to_be_sorted:
    print(k, i.value)
    k += 1

to_be_sorted.sort()

k=0
for i in to_be_sorted:
    print(k, i.value)
    k += 1

result = 1



number = 0
for i in to_be_sorted:
    number += 1


    if i.value == [[6]] or i.value == [[2]]:
        print(number, i.value)
        result *= number

print(result)


