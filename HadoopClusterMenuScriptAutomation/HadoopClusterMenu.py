import os

print("\t\t\tWelcome to the Hadoop Cluster Set-Up Menu")
print("\t\t\t------------------------------------")


print(''' \t\t\tFor setting hadoop cluster you have to follow certain steps:
          \t\tStep:1 Give details about namenode.
          \t\tStep:2 Give details about datanode.
          \t\tStep:3 give details about client.
''')



Namenode_IP = input("\t\t\tGive IP at which you want to configure namenode:")
#copy namenode.py into instance

os.system("scp namenode.py root@{}:/root/".format(Namenode_IP))
#install python3 on the instance

os.system("ssh root@{} yum install python3 -y".format(Namenode_IP))
#setup namenode core-site.xml and hdfs-site.xml

os.system("ssh root@{} python3 namenode.py".format(Namenode_IP))
#format the namenode

os.system("ssh root@{} hadoop namenode -format".format(Namenode_IP))
#start namenode

os.system("ssh root@{} hadoop-daemon.sh start namenode".format(Namenode_IP))



Datanode_IP = []
count_datanode = int(input("\t\t\tHow many datanode you want to configure: "))
for i in range(0,count_datanode):
	d_ip = input("\t\t\tGive IP at which you want to configure datanode{}:".format(i+1))
	Datanode_IP.append(d_ip)
	os.system("scp datanode.py root@{}:/root/".format(Datanode_IP[i]))
	os.system("ssh root@{} yum install python3 -y".format(Datanode_IP[i]))
	#setup datanode core-site.xml and hdfs-site.xml
	os.system("ssh root@{} python3 datanode.py".format(Datanode_IP[i]))
	#start datanode
	os.system("ssh root@{} hadoop-daemon.sh start datanode".format(Datanode_IP[i]))


Client_IP = []
count_client = int(input("\t\t\tHow many client you want to configure: "))
for i in range(0,count_client):
	c_ip = input("\t\t\tGive IP at which you want to configure client:")
	Client_IP.append(c_ip)
	os.system("scp client.py root@{}:/root/".format(Client_IP[i]))
	os.system("ssh root@{} yum install python3 -y".format(Client_IP[i]))
	#setup datanode core-site.xml and hdfs-site.xml
	os.system("ssh root@{} python3 client.py".format(Client_IP[i]))
	