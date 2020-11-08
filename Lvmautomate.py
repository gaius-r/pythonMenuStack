import os


while True :
	os.system("clear")
	print("\t\tpress 1: to make LVM partition")
	print("\t\tpress 2: to exit")

	ch = input("enter your choice : ")

	if ch == "1":
		pv1 = input("enter name/path of the disk 1 : ")
		pv2 = input("enter name/path of the disk 2 : ")
		os.system("pvcreate /dev/{}".format(pv1))
		os.system("pvcreate /dev/{}".format(pv2))
		vgn = input("enter name for your vg : ")
		os.system("vgcreate {} /dev/{} /dev/{}".format(vgn,pv1,pv2))
		lvsize = input("enter size of your lv : ")
		lvname = input("enter name of your lv : ")
		os.system("lvcreate --size +{} --name {} {}".format(lvsize,lvname,vgn))
		os.system("tput setaf 3")		
		print("successfully createed logical volume..")
		os.system("tput setaf 7")
		os.system("lvdisplay /dev/{}/{}".format(vgn,lvname))
		input("press enter to format your lv {}".format(lvname))
		os.system("mkfs.ext4 /dev/{}/{}".format(vgn,lvname))
		print("succesfully formatted you lv {}".format(lvname))
		input("press enter to make folder where u want to mount your lv")
		folder = input("enter name for your folder : ")
		os.system("mkdir /{}".format(folder))
		print("mounting your lv {} to the /{} folder".format(lvname,folder))
		os.system("mount /dev/{}/{}  /{}".format(vgn,lvname,folder))
		print("successfully mounted ur lv {} to /{} folder".format(lvname,folder))
	
	elif ch == "2":
		exit()

	else :
		print("Invalid choice")
	input()