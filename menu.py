# ARTH TASK - Python scripting for all Technologies learnt
# Try to keep the code as neat as possible for easy understanding of changes and control flow

import os
import subprocess

loginAWS = False
profile = ""

# function to launch AWS instances


def launchInstance():

    keyname, securityGroup, rc = keyAndSecurity()

    if rc != 0:
        return

    exitflag = 0
    imageID = "ami-0e306788ff2473ccb"
    print("\n1. Amazon Linux 2 AMI 64-bit (x86)\t2. RHEL 8 64-bit (x86)\t3. Custom Image ID (Default : Amazon Linux 2 AMI)")
    for i in range(5):
        amiChoice = input("Enter choice (1-3) : ")
        if amiChoice == '2':
            imageID = "ami-052c08d70def0ac62"
            break
        elif amiChoice == '3':
            imageID = input("Enter Image ID : ")
            break
        else:
            if i == 4:
                exitflag = 1
                break
            print("Invalid choice!!! Choose from 1-3\n")
    if exitflag == 1:
        print("Entered wrong option 5 times. Exiting...")
        return

    print("Create Instance with instanceID : {}, type : t2.micro, key-name : {}, security-group : {} ?".format(imageID, keyname, securityGroup))
    create = input("Enter Y to confirm : ")
    if create == 'Y':
        errorInstance = subprocess.call(
            "aws ec2 run-instances --image-id {} --count 1 --instance-type t2.micro --key-name {} --security-groups {} --profile {}".format(imageID, keyname, securityGroup, profile))
        if errorInstance == 0:
            instanceID = input("Enter the instance ID : ")
            nametag = input("Enter name tag for instance (Eg. MyInstance): ")
            subprocess.call(
                "aws ec2 create-tags --resources {} --tags Key=Name,Value={}".format(instanceID, nametag))
            print("Instance is created and running.\n")
    return


def keyAndSecurity():
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
            errorKeyPair = os.system(
                "aws ec2 create-key-pair --key-name {0} --profile {1} --output text > {0}.pem".format(keyPair, profile))
            # Creating Security-Group
            errorSecurityGroup = subprocess.call(
                'aws ec2 create-security-group --group-name {} --description "{}" --profile {}'.format(secGroup, descSecurity, profile))
            if errorKeyPair != 0 or errorSecurityGroup != 0:
                recreate = input(
                    "\nWould you like to delete created key-pair or security-group and try again ? (Press Y for Yes): ")
                if recreate == 'Y' or recreate == 'y':
                    if errorKeyPair != 0 and errorSecurityGroup == 0:
                        rc = 11
                        subprocess.call(
                            "aws ec2 delete-security-group --group-name {} --profile {}".format(secGroup, profile))
                    elif errorSecurityGroup != 0 and errorKeyPair == 0:
                        rc = 12
                        subprocess.call(
                            "aws ec2 delete-key-pair --key-name {} --profile {}".format(keyPair, profile))
                    continue
                else:
                    rc = 1
                    break
            else:
                rc = 0
                print("rc : {}".format(rc))
                break
    return (keyPair, secGroup, rc)


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
