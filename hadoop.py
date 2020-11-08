import os


# script of  hadoop with python
print('\t\t\t\t\t\t\tWelcome to world of hadoop')
print('\t\t\t\t\t\t\t--------------------------')


def core_site():
    print('Enter NameNode IP Address :-   ', end='')
    NN_ip = input()

    os.system('echo \<configuration\> >> core-site.xml')
    os.system('echo \<property\> >> core-site.xml')
    os.system('echo \<name\>fs.default.name\<\/name\> >> core-site.xml')

    if cmd == '1':
        os.system(
            'echo \<value\>hdfs://{}:9001\<\/value\> >> core-site.xml'.format(NN_ip))
    else:
        os.system(
            'echo \<value\>hdfs://{}:9001\<\/value\> >> core-site.xml'.format(NN_ip))

    os.system('echo \</property\> >> core-site.xml')
    os.system('echo \<\/configuration\> >> core-site.xml')

    if cmd == '2':
        os.system(
            'scp core-site.xml {}:/etc/hadoop/core-site.xml'.format(remote_ip))
    else:
        os.system('cp core-site.xml /etc/hadoop/core-site.xml')
    os.system('rm -rf core-site.xml')
    os.system('cp temp.xml core-site.xml')


def hdfs_site():

    if cmd2 == '4':
        print('Enter DataNode Directory name you want to provide to NN :-   ', end='')

    elif cmd2 == '3':
        print('Enter NameNode Directory name you want to create :-   ', end='')

    dir_name = input()

    if cmd == '3':
        os.system('ssh {} mkdir {}'.format(remote_ip, dir_name))
    # else:
        # os.system('mkdir {}'.format(dir_name))
    os.system('echo \<configuration\> >> hdfs-site.xml')
    os.system('echo \<property\> >> hdfs-site.xml')

    if cmd2 == '4':
        os.system('echo \<name\>dfs.data.dir\<\/name\> >> hdfs-site.xml')
    elif cmd2 == '3':
        os.system('echo \<name\>dfs.name.dir\<\/name\> >> hdfs-site.xml')
    os.system('echo \<value\>{}\<\/value\> >> hdfs-site.xml'.format(dir_name))
    os.system('echo \</property\> >> hdfs-site.xml')
    os.system('echo \<\/configuration\> >> hdfs-site.xml')
    if cmd == '2':
        os.system(
            'scp hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml'.format(remote_ip))
    else:
        os.system('cp hdfs-site.xml /etc/hadoop/hdfs-site.xml')
    os.system('rm -rf hdfs-site.xml')
    os.system('cp temp2.xml hdfs-site.xml')

# step1
	# 1download hadoop software and install
	# 2download jdk softwareand install
    print('\t\t\t\t\t\t\press 1 to install hadoop')
    print('\t\t\t\t\t\t\press 2 to install jdk software')
# step2
	# option 3 to be masternode(namenode)

    elif cmd2 == '3':
            os.system('rpm -ivh /root/jdk-8u171-linux-x64.rpm')
            os.system('rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force')
            hdfs_site()
            core_site()
            os.system('hadoop namenode -format')
            os.system('hadoop-daemon.sh start namenode')
            os.system('jps')

	# option 4 to be datanode (slavenode)

	 elif cmd2=='4':
            os.system('rpm -ivh /root/jdk-8u171-linux-x64.rpm')
            os.system('rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force')
            hdfs_site()
            core_site()
            os.system('sudo hadoop-daemon.sh start datanode')
            os.system('sudo jps')

    
# step3
    # substep 3 if you choose masternode 
        # configure it with ip address 
            # configure 1.hdfs.site.xml 2.core.site.xml
               
            
        
    # substep3 if you choose datanode
        # give ip address 
            # configure core.site.xml
