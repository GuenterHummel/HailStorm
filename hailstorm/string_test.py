import car

message = "Python has several loop variants"
result = message.lower()
print(result)
result = message.upper()
print(result)

for i in range(len(message)):
    print(i, message[i], end=",")

print()

for i, current_char in enumerate(message):
    print(i, current_char, end=",")

print()

for current_char in message:
    print(current_char, end=",")

print()

maintext = "This is a secret message. Please do not distribute"
print(maintext.index("This"))
print(maintext.index("Please"))
print(maintext.index("o"))
print(maintext.rindex("o"))
print(maintext.find("not"))
print("not" in maintext)
print("gue" in maintext)

timestamp = "11:22:33"
print(timestamp.split(':'))

print()


def check_string(input_string, n, test):
    print("""input = {}""".format(input_string))
    print("""input length is {}""".format(len(input_string)))
    print("""the {}. char is '{}'""".format(n, input_string[n]))
    print("""input contains "{}" : {}""".format(test, test in input_string))


check_string("Hallo das ist ein String", 12, "ist")

secret_text = "This is the second secret message. Please do not distribute"
# secret_text[3] = 'e'


def repeat_chars(input_string):
    result_string = ""
    for i, ch in enumerate(input_string):
        result_string += ch * (i + 1)

    return result_string


print(repeat_chars("ABCD"))
print(repeat_chars("ABCDEF"))


def is_vowel(ch):
    return ch in "AaEeIiOoUuÄäÖöÜü"


def remove_vowel(input_string):
    result_string = ""

    for letter in input_string:
        if is_vowel(letter):
            result_string += "_"
        else:
            result_string += letter

    return result_string


print(remove_vowel("Das ist ein lustiger neuer hübscher Text"))

