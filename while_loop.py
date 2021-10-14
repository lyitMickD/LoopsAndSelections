max = 5
counter = 0
total = 0
while counter <= max:
    total += 9.99
    counter += 1
print("The final amount is:{0:5.2f}".format(total))
print("\n")

text = ""
while 1:
    print("Enter name")
    uname=input()
    if(uname == "joe"):
        break
    print("\nSorry, try again!")
print("Finished")
print("\n")

