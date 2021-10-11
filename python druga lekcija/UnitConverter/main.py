
print("Hello, I can convert a kilometres into miles.")
while True:
    km = int(input("Can you please enter a number of kilometres? "))
    miles = round((0.621371192 * km), 2)
    print(str(miles) + " miles")
    answer = input("Would you like another conversion? ")
    if answer.lower() != "yes":
        print("Ty for using our service.")
        break
