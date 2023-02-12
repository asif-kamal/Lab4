dnaIn = open("dna1.dat")
contents = dnaIn.read()
dnaIn.close()

input1 = input(("Which pattern?: "))
Count = contents.count(input1)

with open("dna1-baseCount.txt", "a") as f:
    f.write(input1 + ": " + str(Count)+ "\n")
    f.close()

    