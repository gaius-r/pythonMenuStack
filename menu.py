# ARTH TASK - Python scripting for all Technologies learnt
# Try to keep the code as neat as possible for easy understanding of changes and control flow

import os
import subprocess

loginAWS = False
profile = ""

# function to launch AWS instances


def launchInstance():
    while True:
        print("\nDefault values for each field taken if left blank => key-pair : MyKeyPair | security-group : my-sg | --description : My Security Group ")
        keyPair = input("1. Enter name for new key-pair : ")
        secGroup = input("2. Enter name for security group : ")
        descSecurity = input(
            "Enter description for security group {} : ".format(secGroup))
        if keyPair == '':
            keyPair = "MyKeyPair"
        if secGroup == '':
            secGroup = "my-sg"
        if descSecurity == '':
            descSecurity = "My Security Group"
        print("Entered fields : \nkey-pair : {}\nsecurity-group : {}\ndescription : {}\n".format(
            keyPair, secGroup, descSecurity))
        confirm = input("Press Y to confirm : ")
        if(confirm == 'Y' or confirm == 'y'):
            # Creating Key-Pair
            errorKeyPair = subprocess.call(
                "aws ec2 create-key-pair --key-name {0} --profile {1}".format(keyPair, profile))
            # Creating Security-Group
            errorSecurityGroup = subprocess.call(
                'aws ec2 create-security-group --group-name {} --description "{}" --profile {}'.format(secGroup, descSecurity, profile))
            if errorKeyPair != 0 or errorSecurityGroup != 0:
                recreate = input(
                    "\nWould you like to delete created key-pair or security-group and try again ? (Press Y for Yes): ")
                if recreate == 'Y' or recreate == 'y':
                    if errorKeyPair != 0 and errorSecurityGroup == 0:
                        subprocess.call(
                            "aws ec2 delete-security-group --group-name {} --profile {}".format(secGroup, profile))
                    elif errorSecurityGroup != 0 and errorKeyPair == 0:
                        subprocess.call(
                            "aws ec2 delete-key-pair --key-name {} --profile {}".format(keyPair, profile))
                    continue
                else:
                    break
            else:
                print("rc : 0")
                break
    return


def awsConfigure():
    global loginAWS
    global profile

    print("\nAWS Configure\n-----------\n")

    name = input("Enter name of profile : ")
    print("Region name for Mumbai AZ : ap-south-1 | Leave default output format blank for JSON")
    errorCheck = os.system("aws configure --profile {}".format(name))
    print("rc : {}".format(errorCheck))

    if errorCheck == 0:
        loginAWS = True
        profile = name
    return


def awsMenu():
    print('\n')
    os.system('aws --version')

    while True:
        if not loginAWS:
            awsConfigure()
        else:
            choice = input(
                "\n1. Launch instance\t2. AWS Configure\t3. List Profiles\t4. Exit\n> ")
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
