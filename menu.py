# ARTH TASK - Python scripting for all Technologies learnt
# Try to keep the code as neat as possible for easy understanding of changes and control flow

import os
import ec2
from subprocess import PIPE, run, check_output,call

import ec2

loginAWS = False
profile = ""

# wrapper to get ouput of system command
def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout


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



def webserver():

    key = input("Enter key name with .pem extension: ")
    address = out("echo %USERPROFILE%").rstrip("\n")
    key = r"{}\KeyPairs\{}".format(address, key)
    instance = input("Enter instance-id : ")
    publicDns = out("aws ec2 describe-instances --instance-ids {}\
            --query Reservations[*].Instances[*].[PublicDnsName] --output text".format(instance)).rstrip("\n")
    
    while True:
        error1, error2, error3, error4 = 0,0,0,0
        print("\n 1. Install Apache WebServer\
               \n 2. Start WebServer\
               \n 3. Stop WebServer\
               \n 4. Check Status\
               \n\n Press Q to quit")
        choice = input("> ")
        if choice == '1':
            error1 = os.system("ssh -i {} ec2-user@{} sudo yum install httpd".format(key, publicDns))
        elif choice == '2':
            error2 = os.system("ssh -i {} ec2-user@{} sudo systemctl start httpd".format(key, publicDns))
            if error2 == 0:
                print("WebServer Started...")
        elif choice == '3':
            error3 = os.system("ssh -i {} ec2-user@{} sudo systemctl stop httpd".format(key, publicDns))
            if error3 == 0:
                print("WebServer Stopped...")
        elif choice == '4':
            error4 = os.system("ssh -i {} ec2-user@{} sudo systemctl status httpd".format(key, publicDns))
        elif choice == 'q' or choice == 'Q':
            break
        print("rc : {}:{}:{}:{}".format(error1,error2,error3,error4))
    return


def awsMenu():
    print('\n')
    error = os.system('aws --version')
    print(error)
    if error != 0:
        print("No version of AWS CLI found. Would you like to install AWS CLIv2 ? (Press Y to confirm)")
        install = input("> ")
        if install == 'y' or install == 'Y':
            call("msiexec /i https://awscli.amazonaws.com/AWSCLIV2.msi")
            return
        else:
            return
    while True:
        if not loginAWS:
            awsConfigure()
        else:
            print("\nAWS MENU\
                   \n--------")
            print("\n1. EC2    2. Run Webserver    3. S3    4. CloudFront\
                 \n\nPress Q to exit\n")
            choice = input("> ")
            if choice == '1':
                ec2.ec2menu(profile)
            elif choice == '2':
                webserver()
            elif choice == '3':
                break
            elif choice == '4':
                break
            elif choice == 'Q' or choice =='q':
                return
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