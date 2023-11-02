f = open("Day 25 Input.txt", "r")

fileinput = f.read()

f.close()


#Day 1

base5 = fileinput.splitlines()

final_total = 0

changes = {"=": 0, "-": 1, "0": 2, "1": 3, "2": 4}
reverse = {i: j for j, i in changes.items()}

def letters_to_number(letters):
    total = 0
    multi = 1
    for j in range(len(letters) - 1, -1, -1):
        total += (changes[letters[j]] - 2) * multi
        multi *= 5
    return total

def number_to_letters(number):
    final_answer = []
    multi = 1
    while number != 0:
        multi *= 5
        
        for i in range(-2, 3):
            total_copy = number
            total_copy += i * (multi // 5)
            if total_copy % multi == 0:
                final_answer.insert(0,reverse[2-i])
                number = total_copy
                break

    final_answer = "".join(final_answer)

    return final_answer


for i in base5:
    final_total += letters_to_number(i)
    

print(final_total)

final_answer = number_to_letters(final_total)

print(final_answer)




#Day 2





