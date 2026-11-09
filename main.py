queue = []
def option1():
    a = int(input("Enter a number: "))
    queue.append(a)
def option2():
    queue.pop()
    print(queue)
while True:
    print("Please select the operation:1.add 2.remove 3.display 4.exit ")
    select = int(input("Enter your choice: "))
    if select == 1:
        option1()
        print("Queue is added!")
    elif select == 2:
        option2()
    elif select == 3:
        print(queue)
    elif select == 4:
        print("Thanks for using this program🤗")
    else:
        print("Enter a valid option")

