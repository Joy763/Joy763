items = []
while True:
    print("Enter the value of item no "+ str(len(items)+ 1)+ " Enter to stop")
    name = input()
    if name == "":
        break
    items = items + [name]
print("items= ",items)