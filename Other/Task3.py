
x = input("Please, enter a sequence of characters:\n")         # getting a sequence of characters from user

while True:
    # noinspection PyBroadException
    try:
        y = int(input("Please, enter a single digit:\n"))      # getting a number from user and validating it
        break
    except:
        print("Please, enter one integer")

rules = [int(y) > 0,                     # conditions to check
         len(x) % int(y) == 0]

if all(rules):           # if all rules are met
    # print("Success!")
    chunks, chunk_size = len(x), len(x) // int((len(x)/y))
    print([x[i:i+chunk_size] for i in range(0, chunks, chunk_size)])
else:
    print("Not all conditions are met")
