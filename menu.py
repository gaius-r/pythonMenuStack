# ARTH TASK - Python scripting for all Technologies learnt
# Try to keep the code as neat as possible for easy understanding of changes and control flow

import os

loginAWS = False
profiles = []

# function to launch AWS instances
def launchInstance():
    print("Press ")

    
    return
    
def awsConfigure():
    global loginAWS

    print("\nAWS Configure\n-----------\n")

    name = input("Enter name of profile : ")
    print("Region name for Mumbai AZ : ap-south-1 | Leave default output format blank for JSON")
    os.system("aws configure --profile {}".format(name))
    profiles.append(name)
    loginAWS = True
    return

def awsMenu():
    print('\n')
    os.system('aws --version')

    while True:
        if not loginAWS:
            awsConfigure()
        else:
            choice = input("\n1. Launch instance\t2. AWS Configure\t3. List Profiles\t4. Exit\n> ")
            if choice == '1':
                launchInstance()
            elif choice == '2':
                awsConfigure()
            elif choice == '3':
                os.system("aws configure list-profiles")
            elif choice == '4':
                break
            else:                
                print("Invalid choice!!! Choose from 1-3\n")
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
    choice = input("> ")

    if choice == '1':
        awsMenu()
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
