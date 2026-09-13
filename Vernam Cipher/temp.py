def UserInput(choice):
    match choice:
        case 1:
            plain_text = input("Enter plain text: ")
            return plain_text
        case 2:
            print("")
        case _:
            print("")


plain_text = ""
runEncryption = True
while(runEncryption):
    print("\nSelect Encryption Options below...")
    print("1. Plaintext.")
    print("2. Keyword.")
    print("3. Encrypt Plaintext using Vernam Cipher.")
    print("4. Exit")
    encryption_option = int(input("Enter your Choice: "))
    match encryption_option:
        case 1:
            runPlaintext = True
            while(runPlaintext):
                print("\nSelect Plaintext Options below...")
                print("1. Show Plaintext.")
                print("2. Set/Change Plaintext.")
                print("3. Exit...")
                plaintext_options = int(input("Enter your Choice: "))
                match plaintext_options:
                    case 1:
                        print("Current Plaintext: ", plain_text)
 
                    case 2:
                        plain_text = UserInput(1)
                    case 3:
                        print("Exiting Plaintext Options...!")
                        runPlaintext = False
                    case _:
                        print("\n\n!!Invalid Input, Select between 1-3...!!")

        case 2:
            print("")

        case 3:
            print("")

        case 4:
            runEncryption = False

        case _:
            print("\n\n!!Invalid Input, Select between 1-4....!!")