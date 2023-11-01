f = open("Day 20 Input.txt", "r")

fileinput = f.read()

f.close()



class Link:
    def __init__(self, num):
        self.num = num


    def __str__(self):
        return str((self.num, self.ind))

    def __int__(self):
        return self.num

def task(fileinput, rounds, key):

    #Part 2

    numbers = fileinput.splitlines()

    numbers = list(map(int, numbers))


    order = numbers.copy()

    zero = None

    for i in range(len(order)):
        numbers[i] = Link(numbers[i] * key)
        if order[i] == 0:
            zero = numbers[i]
        numbers[i].ind = i
        order[i] = numbers[i]

    for _ in range(rounds):
        for i in order:
            ind = numbers.index(i)

            new_ind = (ind + i.num) % (len(order) - 1)

            if new_ind == 0:
                new_ind = len(order) - 1

            if ind != new_ind:

                del numbers[ind]


                numbers.insert(new_ind, i)

    zero_ind = numbers.index(zero)

    total = 0

    for i in range(3):

        zero_ind += 1000
        zero_ind %= len(numbers)
        total += int(numbers[zero_ind])

    return total


print(task(fileinput, 1, 1))
print(task(fileinput, 10, 811589153))
