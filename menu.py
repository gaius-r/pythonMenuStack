# ARTH TASK - Python scripting for all Technologies learnt
# Try to keep the code as neat as possible for easy understanding of changes and control flow

import os
import ec2
import docker
import Lvmautomate
import ml

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

    key = input("\nEnter key name with .pem extension: ")
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
        else:
            print("Invalid choice!!! Choose from 1-4 or Press Q to exit.\n")
        print("rc : {}:{}:{}:{}".format(error1,error2,error3,error4))
    return


def s3():
    while True:
        error1, error2 = 0,0
        print("\n 1. Create S3 Bucket\
               \n 2. Upload to S3 Bucket\
             \n\n Press Q to quit")
        choice = input("> ")
        if choice == '1':
            bucket = input("Enter bucket name : ")
            error1 = os.system("aws s3api create-bucket --bucket {} --region ap-south-1 \
                --create-bucket-configuration LocationConstraint=ap-south-1 --no-verify-ssl".format(bucket))
            if error1 == 0:
                print("Bucket '{}' created successfully.".format(bucket))
        elif choice == '2':
            file = input("Enter absolute path of file you wish to upload : ")
            bucket = input("Enter bucket name : ")
            error2 = os.system("aws s3 cp {} s3://{}/ --acl public-read-write".format(file, bucket))
            if error2 == 0:
                print("File '{}' added to Bucket '{}' successfully.".format(file, bucket))
        elif choice == 'q' or choice == 'Q':
            break
        else:
            print("Invalid choice!!! Choose 1 or 2 or Press Q to exit.\n")
    return


def cloudfront():
    bucket = input("\nEnter bucket name : ")
    print("Setting up CloudFront ...")
    error = os.system(
        "aws cloudfront create-distribution --origin-domain-name {}.s3.amazon.com".format(bucket))
    if error == 0:
        print("CloudFront distribution created successfully.")
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
                s3()
            elif choice == '4':
                cloudfront()
            elif choice == 'Q' or choice =='q':
                return
            else:
                print("Invalid choice!!! Choose from 1-4 or Press Q to exit.\n")
    return


while True:
    print("\n\t\t\t\t-------------------\
           \n\t\t\t\t| TECH STACK MENU |\
           \n\t\t\t\t-------------------\n")

    # Add menu options based on your requirement or idea. These are just temporary for now.
    # Based on added menu options, create functions too with additional elif statements.
    print("1. AWS CLI          \t2. Configure Hadoop    \t3. Configure Docker\
         \n4. Simulate ML Model\t5. Create LVM Partition\
         \nOptions 3 and 4 executable only in a UNIX Machine...")
    print("\nPress Q to quit.\n")
    choice = input("> ")

    if choice == '1':
        awsMenu()
    elif choice == '2':
        continue
    elif choice == '3':
        docker.dockerMenu()
    elif choice == '4':
        ml.mlModel()
    elif choice == '5':
        Lvmautomate.lvmAuto()
    elif choice == 'Q' or choice == 'q':
        break
    else:
        print("Invalid choice!!! Choose from 1-4 or Press Q to exit.\n")