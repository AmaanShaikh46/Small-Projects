def encryption():
    return print("This is Encryption function")

def decryption():
    return print("This is Decryption function")

def UserInput():
    return print("This is input taking function")

print("\nWelcome to Vernam Cipher!!")

run = True
while(run):
    print("\nSelect Functions to perform...")
    print("1. Encryption.")
    print("2. Decryption.")
    print("3. Show Initiated Values.")
    print("4. Exit")
    option = int(input("Enter your choice: "))

    match option:
        case 1:
            
            break
        case 2:
            break
        case 3:
            break
        case 4:
            run = False
            print("Exiting the program....!")
            break
        case _:
            print("\n\n!!Invalid input, Select from options...!!")