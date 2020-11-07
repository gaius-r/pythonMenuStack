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
    print("\n1. Amazon Linux 2 AMI 64-bit (x86)\t2. RHEL 8 64-bit (x86)\t   3. Custom Image ID\t  4. Exit Instance Creation")
    for i in range(5):
        amiChoice = input("Enter choice (1-4) : ")
        if amiChoice == '1':
            imageID = "ami-0e306788ff2473ccb"
            break
        elif amiChoice == '2':
            imageID = "ami-052c08d70def0ac62"
            break
        elif amiChoice == '3':
            imageID = input("Enter Image ID : ")
            break
        elif amiChoice == '4':
            print("Exiting...")
            return
        else:
            if i == 4:
                exitflag = 1
                break
            print("Invalid choice!!! Choose from 1-4\n")
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
                "aws ec2 create-tags --resources {} --tags Key=Name,Value={} --profile {}".format(instanceID, nametag, profile))
            print("Instance is created and running.\n")
    return


# function to create key-pair and security group for instance
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
            os.system(r"mkdir C:\KeyPairs")
            print(r"{}.pem created in folder C:\KeyPairs\ ".format(keyPair))
            errorKeyPair = os.system(
                r"aws ec2 create-key-pair --key-name {0} --profile {1} --output text > C:\KeyPairs\{0}.pem".format(keyPair, profile))
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


# function to add inbound rules to security group
def inboundRules():
    sgname = input("\nEnter security group name : ")
    print("1. All Traffic (Default)   2. TCP   3. UDP   4. SSH   5. Custom Protocol : ")
    for i in range(5):
        plChoice = input("Choose between 1-5 : ")
        if plChoice == '1' or plChoice == '':
            protocol = 'all'
            port = 'all'
            break
        elif plChoice == '2':
            protocol = 'tcp'
            port = '0-65535'
            break
        elif plChoice == '3':
            protocol = 'udp'
            port = '0-65535'
            break
        elif plChoice == '4':
            protocol = 'tcp'
            port = '22'
            break
        elif plChoice == '5':
            protocol = input("Enter protocol number (Eg. 1 for ICMP, 6 for TCP etc.) : ")
            port = input("Enter port range (leave blank for all by default): ")
            if port == '':
                port = 'all'
            break
        else:
            if i == 4:
                print("Entered wrong option 5 times. Exiting...")
                return
            print("Invalid choice!!! Choose from 1-5\n")
    cidr = input("Enter custom cidr (leave blank for 0.0.0.0/0 by default) : ")
    if cidr == '':
        cidr = '0.0.0.0/0'
    confirm = input("Confirm creation of inbound rule for Security Group : {} => for Protocol : {} \
        Port : {} and CIDR : {} ? (Press Y to confirm) : ".format(sgname, protocol, port, cidr))
    if confirm == 'y' or confirm == 'Y':
        errorcheck = subprocess.call("aws ec2 authorize-security-group-ingress --group-name {} --protocol {} \
            --port {} --cidr {} --profile {}".format(sgname, protocol, port, cidr, profile))
        print("rc : {}".format(errorcheck))


# function to configure AWS user profile
def awsConfigure():
    global loginAWS
    global profile

    print("\nAWS Configure\
           \n-------------")

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
            print("\nAWS MENU\
                   \n--------")
            print("\n1. Launch instance     \t2. Show Key-Pairs       \t3. Delete Key-Pair\
                   \n4. Show Security-Groups\t5. Delete Security-Group\t6. Add Inbound Rules\
                   \n7. Show Instances      \t8. Start Instance       \t9. Stop Instance\
                   \n10.AWS Configure       \t11.List Profiles        \t\
                   \n\nPress Q to exit")
            choice = input("> ")
            if choice == '1':
                launchInstance()
            elif choice == '2':
                os.system(
                    "aws ec2 describe-key-pairs --profile {}".format(profile))
            elif choice == '3':
                keypair = input("\nEnter name of key-pair to delete : ")
                os.system(
                    "aws ec2 delete-key-pair --key-name {} --profile {}".format(keypair, profile))
                print("Key-Pair : {} deleted.".format(keypair))
            elif choice == '4':
                os.system(
                    "aws ec2 describe-security-groups --profile {}".format(profile))
            elif choice == '5':
                sg = input("\nEnter name of security-group to delete : ")
                os.system(
                    "aws ec2 delete-security-group --group-name {} --profile {}".format(sg, profile))
                print("Security-Group : {} deleted.".format(sg))
            elif choice == '6':
                inboundRules()
            elif choice == '7':
                os.system("aws ec2 describe-instances --profile {}".format(profile))
            elif choice == '8':
                instance_id = input("\nEnter instance-id : ")
                error = subprocess.call("aws ec2 start-instances --instance-ids {} \
                    --profile {}".format(instance_id, profile))
                if error == '0':
                    print("Instance started successfully.")
                print("rc : {}".format(error))
            elif choice == '9':
                instance_id = input("\nEnter instance-id : ")
                error = subprocess.call("aws ec2 stop-instances --instance-ids {} \
                    --profile {}".format(instance_id, profile))
                if error == '0':
                    print("Instance stopped successfully.")
                print("rc : {}".format(error))
            elif choice == '10':
                awsConfigure()
            elif choice == '11':
                os.system("aws configure list-profiles")
            elif choice == 'Q' or choice == 'q':
                print("Exiting...\n")
                break
            else:
                print("Invalid choice!!! Choose from 1-11 or Q to exit.\n")
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
    print("\n\t\t\t\t-------------------\
           \n\t\t\t\t| TECH STACK MENU |\
           \n\t\t\t\t-------------------\n")

    # Add menu options based on your requirement or idea. These are just temporary for now.
    # Based on added menu options, create functions too with additional elif statements.
    print("1. AWS CLI\t  2. Configure Hadoop\t3. Configure Docker\n4. Simulate ML Model\n")
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
