import os

print()
print("\t\t\t\t\tWelcome to the World of Automation ")
print("\t\t\t\t\t------------------------------------")
print()

print("\t\t\t1.Creating key pair ")
print("\t\t\t2.Checking available key pair ")
print("\t\t\t3.Deleting key pair ")
print("\t\t\t4.Creating security group ")
print("\t\t\t5.Checking available security groups ")
print("\t\t\t6.Deleting security group ")
print("\t\t\t7.Adding Inbound rules to security group ")
print("\t\t\t8.Checking available instances")
print("\t\t\t9.Creating Instances ")
print("\t\t\t10.Starting Instance ")
print("\t\t\t11.Stopping Instance ")
print("\t\t\t12.Terminating Instance ")
print("\t\t\t13.Creating an EBS volume ")
print("\t\t\t14.Attaching an EBS volume with an instance")
print("\t\t\t15.Showing the available storage in an instance")
print("\t\t\t16.Creating a partition in an instance")
print("\t\t\t17.Formatting a partition in an instance")
print("\t\t\t18.Mounting the partition on a directory in instance")
print("\t\t\t19.Showing the filesystem of instance")
print("\t\t\t20.Installing webserver")
print("\t\t\t21.Starting webserver service")
print("\t\t\t22.Checking status of webserver service")
print("\t\t\t23.Stopping webserver service")
print("\t\t\t24.Creating a S3 Bucket")
print("\t\t\t25.Uploading a file to S3 bucket")
print("\t\t\t26.Setting up CloudFront")
print("\t\t\tPress 0 to exit")

print()

while(True):
    choice=int(input("Enter your choice : "))
    
    if(choice==1):
        key_name=input("Enter key-name : ")
        print("Creating key pair in AWS..")
        os.system("aws ec2 create-key-pair --key-name {} --output text > {}.pem".format(key_name,key_name))
        print("key pair created successfully.")
        print("Press enter to continue...")
        
    elif(choice==2):
        print("Checking key pair in AWS..")
        os.system("aws ec2 describe-key-pairs")
        print("Press enter to continue...")
        
    elif(choice==3):
        key_name=input("Enter key-name : ")
        print("Deleting key pair in AWS..")
        os.system("aws ec2 delete-key-pair --key-name {}".format(key_name))
        print("key pair deleted successfully")
        print("Press enter to continue...")
        
    elif(choice==4):
        sg_name=input("Enter sg-name : ")
        desc=input("Enter sg description : ")
        print("Creating security group in AWS..")
        os.system("aws ec2 create-security-group --group-name {} --description {}".format(sg_name,desc))
        print("security group created successfully")
        print("Press enter to continue...")
        
    elif(choice==5):
        print("Checking Security group in AWS..")
        os.system("aws ec2 describe-security-groups")
        print("Press enter to continue...")
        
    
    elif(choice==6):
        sg_name=input("Enter sg-name : ")
        print("Deleting Security group in AWS..")
        os.system("aws ec2 delete-security-group --group-name {}".format(sg_name))   
        print("Security group deleted successfully")
        print("Press enter to continue...")
        
    elif(choice==7):
        name=input("Enter sg-name : ")
        Id=input("Enter sg-id : ")
        port=input("Enter port number : ")
        cidr=input("Enter cidr : ")
        print("Adding inbound rules..")
        os.system("aws ec2 authorize-security-group-ingress --group-name {} --group-id {} --protocol tcp --port {} --cidr {}".format(name,Id,port,cidr))
        print("Added inbound rules successfully")
        print("Press enter to continue...")

    elif(choice==8):
        print("Checking instances in AWS..")
        os.system("aws ec2 describe-instances")
        print("Press enter to continue...")

    elif(choice==9):
        image=input("Enter image-id : ") #ami-052c08d70def0ac62
        inst_type=input("Enter instance-type : ") #t2.micro 
        subnet=input("Enter subnet id : ") #subnet-710f0619
        sg_id=input("Enter sg-id : ")
        key=input("Enter key-name : ")
        print("Launching new instance in AWS..")
        os.system("aws ec2 run-instances --image-id {} --instance-type {} --count 1 --subnet-id {} --security-group-ids {} --key-name {}".format(image,inst_type,subnet,sg_id,key))
        print("new instance launched suucessfully")
        print("Press enter to continue...")

    elif(choice==10):
        instance_id=input("Enter instance-id : ")
        print("starting instance..")
        os.system("aws ec2 start-instances --instance-ids {} ".format(instance_id))
        print("Instance started successfully")
        print("Press enter to continue...")
        
    elif(choice==11):
        instance_id=input("Enter instance-id : ")
        print("stopping instance..")
        os.system("aws ec2 stop-instances --instance-ids {} ".format(instance_id))
        print("Instance stopped successfully")
        print("Press enter to continue...")    

    elif(choice==12):
        inst_id=input("Enter instance id : ")
        print("terminating instance..")
        os.system("aws ec2 terminate-instances --instance-ids {}".format(inst_id))
        print("instance terminated successfully")
        print("Press enter to continue...")
 
    elif(choice==13):
        size=input("Enter volume size : ")
        print("Creating an ebs volume in AWS..")
        os.system("aws ec2 create-volume --availability-zone ap-south-1a --size {}".format(size))
        print("volume created successfully")
        print("Press enter to continue...")
        
    elif(choice==14):
        volume=input("Enter your volume-id : ")
        instance=input("Enter instance-id : ")
        print("attaching your ebs volume to instance..")
        os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdh".format(volume,instance))
        print("volume attached successfully")
        print("Press enter to continue...")
        
    elif(choice==15):
        key=input("Enter key name with .pem extension: ")
        ip=input("Enter ip of instaance seperated with hypen : ")
        os.system("ssh -i {""} ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo fdisk -l".format(key,ip))
        print("Press enter to continue...")
        
    elif(choice==16):
        key=input("Enter key name with .pem extension: ")
        ip=input("Enter ip of instaance seperated with hypen : ")
        name=input("Enter name of volume you want to create partition in : ")
        os.system("ssh -i {""} ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo fdisk {}".format(key,ip,name))
        print("Press enter to continue...")
        
    elif(choice==17):
        key=input("Enter key name with .pem extension: ")
        ip=input("Enter ip of instaance seperated with hypen : ")
        name=input("Enter name of partition you want to format : ")
        os.system("ssh -i {""} ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo mkfs.ext4 {}".format(key,ip,name))
        print("Press enter to continue...")
        
    elif(choice==18):
        key=input("Enter key name with .pem extension: ")
        ip=input("Enter ip of instaance seperated with hypen : ")
        name=input("Enter name of partition you want to mount : ")
        folder=input("Enter name of folder you want to mount this partition : ")
        os.system("ssh -i {""} ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo mount {} {}".format(key,ip,name,folder))
        print("Press enter to continue...")
        
    elif(choice==19):
        key=input("Enter key name with .pem extension: ")
        ip=input("Enter ip of instaance seperated with hypen : ")
        os.system("ssh -i {""} ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo df -h".format(key,ip))
        print("Press enter to continue...")
        
    elif(choice==20):
        key=input("Enter key name with .pem extension: ")
        ip=input("Enter ip of instaance seperated with hypen : ")
        os.system("ssh -i {""} ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo yum install httpd".format(key,ip))
        print("Press enter to continue...")
        
    elif(choice==21):
        key=input("Enter key name with .pem extension: ")
        ip=input("Enter ip of instaance seperated with hypen : ")
        os.system("ssh -i {""} ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo systemctl start httpd".format(key,ip))
        print("Press enter to continue...")
        
    elif(choice==22):
        key=input("Enter key name with .pem extension: ")
        ip=input("Enter ip of instaance seperated with hypen : ")
        os.system("ssh -i {""} ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo systemctl status httpd".format(key,ip))
        print("Press enter to continue...")
        
    elif(choice==23):
        key=input("Enter key name with .pem extension: ")
        ip=input("Enter ip of instaance seperated with hypen : ")
        os.system("ssh -i {""} ec2-user@ec2-{}.ap-south-1.compute.amazonaws.com sudo systemctl stop httpd".format(key,ip))
        print("Press enter to continue...")   

    elif(choice==24):
        bucket=input("Enter bucket name : ")
        print("Creating s3 bucket..")
        os.system("aws s3api create-bucket --bucket {} --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1 --no-verify-ssl".format(bucket))
        print("S3 bucket created successfully")
        print("Press enter to continue...")     
        
    elif(choice==25):
        file=input("Enter filename with format you want to upload : ")
        bucket=input("Enter bucket name : ")
        print("uploading file..")
        os.system("aws s3 cp {} s3://{}/ --acl public-read-write".format(file,bucket))
        print("File uploaded successfully")
        print("Press enter to continue...")
        
    elif(choice==26):
        bucket=input("Enter bucket name : ")
        print("Setting up cloudfront..")
        os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazon.com".format(bucket))
        print("Cloudfront distribution created successfully.")
        print("Press enter to continue...")
    
    elif(choice==0):
        print("Thank you! Have a nice day ahead.")
        break
        
    else:
        print("Invalid !!")
 
