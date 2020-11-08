print("\t\t\tWhat do you want to do? \n")
print("\t\t1 : Install docker")
print("\t\t2 : Start docker service")
print("\t\t3 : Stop docker service")
print("\t\t4 : View docker info")
print("\t\t5 : View active containers")
print("\t\t6 : View all containers")
print("\t\t7 : View downloaded images")
print("\t\t8 : Pull an image")
print("\t\t9 : Launch a container")
print("\t\t10 : Stop a container")
print("\t\t11 : Start a container")
print("\t\t12 : Remove an image")
print("\t\t13 : Remove a container")
print("\t\t0 : Previous menu")
print()
while(True):
    option=int(input("\n\tEnter your choice : "))

    if (option==1):
        if not os.system("rpm -q docker-ce"):
            print("\tDocker is already installed. Exiting installation...")
        else:
            print("\tInstalling Docker...")
            file=open("/etc/yum.repos.d/docker-ce_install.repo","a")
            dockrepo = "[docker]\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable/\ngpgcheck=0\n"
            file.write(dockrepo)
            file.close()
            os.system("yum install docker-ce --nobest")
                  
    elif (option==2):
        os.system("systemctl start docker")

    elif (option==3):
        os.system("systemctl stop docker")

    elif (option==4):
        os.system("docker info")

    elif (option==5):
        os.system("docker ps")
        
    elif (option==6):
        os.system("docker ps -a")

    elif (option==7):
        os.system("docker images")

    elif (option==8):
        image=input("\tEnter image name: ")
        version=input("\tEnter image version (optional): ")
        if image:
            if version != "" :
                os.system("docker pull {}:{}".format(image,version))
            else :
                os.system("docker pull {}".format(image))
        else:
            print("\n\tNo image name entered!")

    elif (option==9):
        img = input("\tEnter image name: ")
        ver = input("\tEnter image version (optional): ")
        name = input("\tEnter container name: ")
        if image:
            if version != "" :
                os.system("docker run -it --name {} {}:{}".format(name,image,version))
            else :
                os.system("docker run -it --name {} {}".format(name,image))
        else:
            print("\n\tNo image name entered!")
        
    elif (option==10):
        name_id = input("\tEnter container name or id: ")
        if name_id :
            os.system("docker stop {}".format(name_id))
        else :
            print("\tPlease enter a container name/ID!")

    elif (option==11):
        name_id = input("\tEnter container name or ID: ")
        if name_id :
            os.system("docker start {}".format(name_id))
        else :
            print("\tPlease enter a container name/ID!")

    elif(option==12):
        img = input("\tEnter image name: ")
        ver = input("\tEnter image version (optional): ")
        if img:
            if ver != "" :
                os.system("docker rmi {}:{} --force".format(img,ver))
            else:
                os.system("docker rmi {} --force".format(img))
        else:
            print("\tPlease enter an image name!")

    elif (option==13):
        name_id = input("\tEnter container name or ID: ")
        if name_id :
            os.system("docker rm {}".format(name_id)) 
        else :
            print("\tPlease enter a container name/ID!")

    elif (option==0):
        break
    
    else:
        print("\tInvalid choice!\n")