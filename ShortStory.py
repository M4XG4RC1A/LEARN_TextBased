def Final(msg,name):
    print("Good Game, your story ends here "+name+" your error was: "+msg);
    return False


status = True

print("Hi this is a short story of a heroe")

name = input("What is your name heroe?: ")

print("Today the princess tell you to protect her")

res = input("What is your choice? (y/n): ")
while res!='y' and res!='n':
    res = input("What is your choice? (y/n): ")

if res == 'n':
    status = Final("Choose no protect the princess",name)

if status:
    print("The princess go to a party")
    print("There are 2 thiefs that what the princess")
    print("You have the option of stop a thief")
    res = input("What is your choice? (y/n): ")
    while res!='y' and res!='n':
        res = input("What is your choice? (y/n): ")
    if res == 'y':
        status = Final("Stop the thief then the other thief attack the princess",name)
    
    if status:
        print("The thiefs are close to the princess, you are hidden")
        print("Go out?")
        res = input("What is your choice? (y/n): ")
        while res!='y' and res!='n':
            res = input("What is your choice? (y/n): ")
        if res == 'y':
            print("Congratulations you stop the thiefs and protect the princess")
        else:
            status = Final("The thiefs capture the princess",name)
