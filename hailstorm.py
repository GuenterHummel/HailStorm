# calculate collatz sequence for a user supplied number

# print the sequence nicely, print the sequence size. 

start_str = input("Working with what number : ")
start_int = int(start_str)

count = 1
seq_int = start_int
print("Here is the Collatz sequence starting at : ", start_str)

print('{0:7d}, '.format(seq_int), end='')
while seq_int > 1:

    # collatz calculation
    if seq_int % 2 == 0:

        seq_int = int(seq_int / 2)
    elif seq_int % 2:

        seq_int = seq_int * 3 + 1
    else:

        print("something wrong if we get here")

    # avoid trailing comma when we hit 1
    if seq_int == 1:

        print('{0:7d} '.format(seq_int))
    else:

        print('{0:7d}, '.format(seq_int), end='')

    count += 1
    if count % 10 == 0:
        print()

else:

    print(count, "elements in sequence starting at", start_int)

print('The end')
