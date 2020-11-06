# ARTH TASK - Python scripting for all Technologies learnt
# Try to keep the code as neat as possible for easy understanding of changes and control flow

# function to launch AWS instances
def lcaws():
    return


# function to launch Hadoop cluster
def lchadoop():
    return


# function to launch Docker containers
def lcdocker():
    return


# function to simulate ML models
def simml():
    return


# add more functions if required below -


while True:
    print("\n\t\t\t\t-------------------\n\t\t\t\t| TECH STACK MENU |\n\t\t\t\t-------------------\n")

    # Add menu options based on your requirement or idea. These are just temporary for now.
    # Based on added menu options, create functions too with additional elif statements.
    print("1. Launch AWS Instance\t  2. Launch Hadoop Cluster\t3. Launch Docker Containers\n4. Simulate ML Model\n")
    print("Press Q to quit.\n")
    choice = raw_input("Enter your choice : ")

    if choice == '1':
        lcaws()
    elif choice == '2':
        lchadoop()
    elif choice == '3':
        lcdocker()
    elif choice == '4':
        simml()
    elif choice == 'Q' or choice == 'q':
        break
    else:
        print("Invalid choice!!! Choose from 1-4 or Press Q to exit.\n")
