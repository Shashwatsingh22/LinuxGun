import os
import getpass
from pyfiglet import Figlet

def render(text,style,num):
	f=Figlet(font=style)
	print('\n')
	print(f.renderText(text))

os.system("tput setaf 1")
render('LinuxGun','big',0)
render('by Shashwat Singh','digital',5)
os.system("tput setaf 7")

os.system("tput setaf 2")

print("\t\t\t    SHORCUTS FOR EVERY CMD ")

print("\t\t\t---------------------------------")

password=getpass.getpass("Enter Password: ")
correctpass="redhat"

if password != correctpass:
	print("Incorrect Password")
	exit()

print("Where You Wants to Deploy this (local/remote) : ",end=" ")
location= input()

if location=="remote":
	remote_IP=input("Enter the IP of remote location: ")


while True:

		print("""\t\t\t 
			Press 1: For The Some basic commands(Pings/Retriving Tha Data From The Clipboard.....) !
			Press 2: For some Directory & File Related Commands ! \n
			Press 3: For the Package Management/Software Manegement/conf yum/Install softwares !  
			Press 4: For Networking Purpose (tranfer file to other system/ running the program(GUI Base or CLI based)) !
			Press 5: For The User Settings (Add user/Delete user/change password/....)!
			Press 6: Configure Webserver !
			Press 7: Gaing information about (IP/Port Scanning/to run script for get the that system is vulnerabel or not) 
			                BY THE HELP OF TOOL(NMAP) !
			Press 8: Configure Router Gateway !
			Press 9: Partition ! 
			Press 10: Docker (setup/conf/pull/lunch) 
			Press 12:Exit
			  """)

		print("Enter Your Choice: ",  end=" ") #here if we use the end=" " becoz when we give the input it is automatically go to new line For taking the input but I use this as to not terminate this in new line 
		ch=input()
		if location == "local":
			if int(ch)==1:
				while True:
					print("""Press 1:Date
						     Press 2:Callender
						     Press 3:To check the connectivity !
						     Press 4:To Retrive The data from the clipboard !
						     Press 5: To Shutdown the OS !
						     Press 6:Back"""
						  )
					print("Enter Your Choice: ", end=" ")
					ch1=input()
					if int(ch1)==1:
						os.system("date")
					elif int(ch1)==2:
					    os.system("cal")
					elif int(ch1)==3:
						os.system("ping 8.8.8.8")
					elif int(ch1)==4:
						os.system("dnf install xclip")
						os.system("xclip")
					elif int(ch1)==5:
						os.system("init 0")
					elif int(ch1)==6:
						break

			elif int(ch)==2:
			    while True:
			        print("""Press 1:Change Directory/Location
			        	     Press 2:Move Just Back location
			        	     Press 3:Make New Folder
			        	     Press 4:Remove Directory
			        	     Press 5:Make The new file
			        	     Press 6:Remove the File
			        	     Press 7:To see the All information About the files/floder about there read write
			        	     Press 8:To see the whole informate about the specific file only
			        	     Press 9:Back"""
			        	  )
			        print("Enter Your Choice: ", end=" ")
			        ch1=input()
			        if (int(ch1)==1):  	
			        	print("Enter the Address Of Your Destination (like Downloads or Desktop/Project/xyz): ", end=" ")
			        	chage_dir=input()
			        	os.system("cd {}".format(chage_dir))
			        elif int(ch1)==2:
			        	os.system("cd ..")
			        elif int(ch1)==3:
			        	print("Give the name to your floder: ",end=" ")
			        	name=input()
			        	os.system("mkdir {}".format(name))
			        elif int(ch1)==4:
			        	print("Name of that Directory: ",end=" ")
			        	name=input()
			        	os.system("rm {}".format(name))
			        elif int(ch1)==5:
			        	print("Give the name to your file: ",end=" ")
			        	name=input()
			        	print("Extension for your file: ",end=" ")
			        	exe=input()
			        	os.system("touch {}.{}".format(name,exe))
			        elif int(ch1)==6:
			        	print("Give the file name with Extension : ",end=" ")
			        	name=input()
			        	exe=input()
			        	os.system("rm {}.{}",format(name,exe))
			        elif int(ch1)==7:
			        	os.system("ls -la")
			        elif int(ch1)==8:
			        	print("Enter the name of the file/folder: ",end=" ")
			        	name=input()
			        	os.system("ls -la | grep {}",format(name))
			        elif int(ch1)==9:
			        	break
			elif int(ch)==3:
				while True:
					print("""
			    		Welcome TO Package Manegment!!!
			    		Some technical work you Have to do first follow the steps :
			    		IN REDHAT FOR THE PACKAGEMENT (rpm)==> It is used to managed the software..
			    		We have to Mount that .iso file to our vmware/virtual box
			    		-----------     VM Ware   --------------------
			    		Player >> Removal Devices >> Settings >> Give the Address of your iso file
			    		--------------------------------------------------------------------------
			    		--------------Virtual Box ----------------------------
			    		>>Device Optical >> Go there and attache the .iso file
			    		-------------------------------------------------------
			    		Press 1:Wants to check that Software is available or not ?
			    		Press 2: Configure Your Yum !
			    		Press 3: To Check Repolist !
			    		Press 4: To install the Software !
			    		Press 5: To Remove any Software !
			    		Press 5: Back
			    		""")
					print("Enter Your Choice: ", end=" ")
					ch1=input()
					if int(ch1)==1:
						print("Enter the name of the Software: ", end=" ")
						name_soft=input()
						os.system("rpm q -a | grep {}".format(name_soft))
					elif int(ch1)==2:
						print("""
							-----FOR Configure Your Yum Need To follow these steps: ------
							Step 1: Go To the loction of the Yum Repo(run cmd)===>>> cd /etc/yum.repos.d/
							Step 2: Now make your own repo file of any name but extension should be (.repo)
							===>>> gedit xyz.repo
							Step 3: Inside the xyz.repo file copy and paste the given data below:
							===>>>
							----------------------------------------------------------------------------
							[dvd1]
							baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream
							gpgcheck=0
							[dvd2]
							baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS
							gpgcheck=0
							---------------------------------------------------------------------------      
							Step 4: Save That file...
							<<<<Now You have completed the Repo work>>>>
							Now you may need some more which are not present in these Repolist::::
							So, You have SetUp two more repolist... You need not do anything I will do
							it for you.....
							PRO TIP: Use Inspite the Use of yum.. you use only dnf...
						""")
						os.system("yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")
						os.system("yum install https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm")
						print("Now YOUR YUM IS CONFIGURED !!")
					elif int(ch1)==3:
						os.system("dnf repolist")
					elif int(ch1)==4:
						print("Enter the name of the valid software: ", end=" ")
						name_soft=input()
						os.system("dnf install {}".format(name_soft))
					elif int(ch1)==5:
						print("Enter the name of the valid Software: ", end=" ")
						name_soft=input()
						os.system("rpm -e {}".format(name_soft))
					elif int(ch1)==6:
						break
			elif int(ch)==4:
				while True:
					print("""
						---------------Welcome To Networking World------------------------
						First we need to stup our lab perfectly.....Follow the steps which are given below:::
						>>>> Network Setting>> Change From NAT to Bridge >>>>
						Now your Lab is ready to use -----> Stop the wifi and then start....
						NOTE: You should have to know the IP of the System B , username ,password and your system
						should be in same network......
						You also need one Software i.e. openssh so press 0
						Press 0:To install ssh !  
						Press 1:For finding Your the IP  !
						Press 2:Ping to the System B !
						Press 3: You Want The Output Of  program From the System B (For the CLI)!
						Press 4: You Wants to transfer the file from System A to B(:/root/) (WE will use scp protocal)!
						Press 5: You Wants to run any programable file (Like written in python) !
						Press 6: You Wants to copy the file from the system  B !
						Press 7: You Wants to copy the folder from the System B !
						Press 8: You Want The Output Of  program From the System B (For the GUI)!
						Press 9: Back !
					""")
					print("Enter Your Choice: ", end=" ")
					ch1=input()
					if int(ch1)==0:
						os.system("dnf install openssh")
					elif int(ch1)==1:
						os.system("ifconfig")
					elif int(ch1)==2:
						print("Enter the IP of the System B: ", end=" ")
						ip_b=input()
						os.system("ping {}".format(ip_b))
					elif int(ch1)==3:
						print("Enter the ip of the system B  and also tell for which program that you wants output: ",end=" ")
						ip_b=input()
						name_soft=input()
						os.system("ssh {} {}".format(ip_b,name_soft))
					elif int(ch1)==4:
						print("Enter the Name of the File: ",end=" ")
						file_name=input()
						print("Enter the IP of the System B: ", end=" ")
						ip_b=input()
						os.system("scp {} {} :/root".format(file_name,ip_b))
					elif int(ch1)==5:
						print("Enter the IP of the System B: ",end=" ")
						ip_b=input()
						print("ENter complete location of that File (like: /root/my.py): ",end=" ")
						location=input()
						os.system("ssh {} python3 {}".format(ip_b,location))
					elif int(ch1)==6:
						print("Enter the IP of the System B: ",end=" ")
						ip_b=input()
						print("Enter the of the file which you wants to copy (like /root/sha.txt): ",end=" ")
						location_b=input()
						print("Enter the location of your that where you wants to copy that file(like /root/): ",end=" ")
						location_a=input()
						os.system("scp {}:{} {}".format(ip_b,location_b,location_a))
					elif int(ch1)==7:
						print("Enter the IP of the system B: ",end=" ")
						ip_b=input()
						print("Enter the location of the folder of the System B(like /root/fold1): ",end=" ")
						location_b=input()
						print("Enter the location of the system A (like /root/): ",end=" ")
						location_a=input()
						os.system("scp -r {}:{} {}".format(ip_b,location_b,location_a))
					elif int(ch1)==8:
						print("Enter the IP of the system B: ",end=" ")
						ip_b=input()
						print("Enter the valid program name: ",end=" ")
						name_soft=input()
						os.system("ssh -X {} {}".format(ip_b,name_soft))
					elif int(ch1)==9:
						break
			elif int(ch)==5:
				while True:
					print("""
						Press 1:To add user !
						Press 2: Delete The User !
						Press 3: Change The password !
						Press 4: Back !
						""")
					print("Enter Your Choice : ")
			elif int(ch)==6:
				while True:
					print("""
						Press 1: Install the HTTPD !
						Press 2: Now the MOve to that Folder where You have keep your Complete Website Folder(WE CAN ALSO CHANGE THIS BY DEFAULT FOLDER) !
						Press 3: Before starting we need to first Disable firewall by which client can access to our server(For Permanently) !
						Press 4: Stop the Firewall (For temprory) !
						Press 5: You Wants to start your Server for temprory !
						Press 6: You wants to start your Server for Permanently !
						Press 7: To see the which ports are working !
						Press 8: Back
						""" )
					print("Enter your Choice: ",end=" ")
					ch1=input()
					if int(ch1)==1:
						os.system("dnf install httpd")
					elif int(ch1)==2:
						print("Go on the loction /var/www/html by >>> cd /var/www/html")
					elif int(ch1)==3:
						os.system("systemctl disable firwalld")
					elif int(ch1)==4:
						os.sytem("systemctl stop firewalld")
					elif int(ch1)==5:
						os.system("systemctl start httpd")
						print("Now your client can access to your Webserver by using >>>> https://your_RHEL_IP:80/webpage_name")
					elif int(ch1)==6:
						os.system("systemctl enable httpd")
						print("Now your client can access to your Webserver by using >>>> https://your_RHEL_IP:80/webpage_name")
					elif int(ch1)==7:
						os.system("netsat -tnlp")
					elif int(ch1)==8:
						break
			elif int(ch)==7:
				while True:
					print("""
						Press 1:To Install NMAP !
						Press 2:Collect the IP which are connected to same Network !
						Press 3:Show the  information about port(Work With the Particular IP)!
						Press 4:Now Just Remove those ports which are inactive !
						Press 5:Now Deploy the Default Script !
						Press 6:Also scan with all the scripts(With High Speed By the use of the -T5) !
						Press 7:Back ! 
						""")
					print("Enter Your Choice: ",end=" ")
					ch1=input()
					if int(ch1)==1:
						os.system("dnf install nmap")
					elif int(ch1)==2:
						print("Enter the starting 3 decimal number(like if your IP=192.163.43.240 then only give input 192.163.43: ",end=" ")
						ip_a=input()
						os.system("nmap -sL {0}.0-255".format(ip_a))
					elif int(ch1)==3:
						print("Enter the starting 3 decimal number(like if your IP=192.163.43.240 then only give input 192.163.43: ",end=" ")
						ip_vic=input()
						os.system("nmap -sn -sL {0}.0-255".format(ip_vic))
					elif int(ch1)==4:
						print("Choose the victim IP from the upper output and put it here: ",end=" ")
						ip_vic=input()
						os.system("nmap -Pn {0}".format(ip_vic))
					elif int(ch1)==5:
						print("Choose the victim IP from the upper output and put it here: ",end=" ")
						ip_vic=input()
						os.system("nmap -Pn --script default {0}".format(ip_vic))
					elif int(ch1)==6:
						print("Choose the victim IP from the upper output and put it here: ",end=" ")
						ip_vic=input()
						os.system("nmap -Pn -T5 --script all {0}".format(ip_vic))
					elif int(ch1)==7:
						break
			elif int(ch)==8:
				while True:
					print("""
						Press 1: To See The IP and the Gateway Of your Router !
						Press 2: To Remove The Enteries !
						Press 3: To add Gateway !
						Press 4: Back !
						""")
					print("Enter Your Choice : ",end=" ")
					ch1=input()
					if int(ch1)==1:
						os.system("route -n")
					elif int(ch1)==2:
						os.system("route del -net 0.0.0.0")
					elif int(ch1)==3:
						os.system("route add -net 0.0.0.0 gw 10.0.2.2")
					elif int(ch1)==4:
						break
			elif int(ch)==9:
				while True:
					print("""
						<<<<----------------- PARTITION -------------------------->>>>>
						Imp NOTE : SIze Of 1 Sector == 512 bytes == Half Of KiB 
						Press 1: To Display Information About Partition Data Space !
						Press 2: To see that How many HDD are attach with this OS !
						Press 3: For Creating New Virtual HDD (in VM)
						Press 4: List to The Particular HDD !
						Press 5: Create Partition !
						Press 6: Back !
						""")
					print("Enter Your Choice : ",end=" ")
					ch1=input()
					if int(ch1)==1:
						os.system("lvdisplay")
					elif int(ch1)==2:
						os.system("fdisk -l")
					elif int(ch1)==3:
						print("""
							For Creating New Virtual HDD need to follow these steps:
							>>>1.   ShutDown the OS!
							>>> Setting >> Storage >> Controller SATA >> Last ICON (Add New HDD) >>> 
							Create New HDD >>> VOI FORMATE >>> Dynamic Allocated >>> Put Size
							""")
					elif int(ch1)==4:
						print(" Enter information about the Particular Information(like /dev/sda): ", end=" ")
						hdd_info=input()
						os.system("fdisk -l {0}".format(hdd_info))
					elif int(ch1)==5:
						print(" Enter information about the Particular HDD(like /dev/sda): ", end=" ")
						hdd_info=input()
						print("Follow the Steps : ")
						os.system("fdisk {0}".format(hdd_info))
					elif int(ch1)==6:
						break
#--------------------------------------from here its the code for the remote system --------------------------------- 

		if location == "remote":
			if int(ch)==1:
				while True:
					print("""Press 1:Date
						     Press 2:Callender
						     Press 3:To check the connectivity !
						     Press 4:To Retrive The data from the clipboard !
						     Press 5: To Shutdown the OS !
						     Press 6:Back"""
						  )
					print("Enter Your Choice: ", end=" ")
					ch1=input()
					if int(ch1)==1:
						os.system("ssh {0} date".format(remote_IP))
					elif int(ch1)==2:
					    os.system("ssh {0} cal".format(remote_IP))
					elif int(ch1)==3:
						os.system("ssh {0} ping 8.8.8.8".format(remote_IP))
					elif int(ch1)==4:
						os.system("ssh {0} dnf install Xclip".format(remote_IP))
						os.system("Xclip".format(remote_IP))
					elif int(ch1)==5:
						os.system("ssh {0} init 0".format(remote_IP))
					elif int(ch1)==6:
						break

			elif int(ch)==2:
			    while True:
			        print("""Press 1:Change Directory/Location
			        	     Press 2:Move Just Back location
			        	     Press 3:Make New Folder
			        	     Press 4:Remove Directory
			        	     Press 5:Make The new file
			        	     Press 6:Remove the File
			        	     Press 7:To see the All information About the files/floder about there read write
			        	     Press 8:To see the whole informate about the specific file only
			        	     Press 9:Back"""
			        	  )
			        print("Enter Your Choice: ", end=" ")
			        ch1=input()
			        if (int(ch1)==1):  	
			        	print("Enter the Address Of Your Destination (like Downloads or Desktop/Project/xyz): ", end=" ")
			        	chage_dir=input()
			        	os.system("ssh {0} cd {1}".format(remote_IP,chage_dir))
			        elif int(ch1)==2:
			        	os.system("cd ..")
			        elif int(ch1)==3:
			        	print("Give the name to your floder: ",end=" ")
			        	name=input()
			        	os.system("ssh {0} mkdir {1}".format(remote_IP,name))
			        elif int(ch1)==4:
			        	print("Name of that Directory: ",end=" ")
			        	name=input()
			        	os.system("ssh {0} rm {1}".format(remote_IP,name))
			        elif int(ch1)==5:
			        	print("Give the name to your file: ",end=" ")
			        	name=input()
			        	print("Extension for your file: ",end=" ")
			        	exe=input()
			        	os.system("ssh {0} touch {1}.{2}".format(remote_IP,name,exe))
			        elif int(ch1)==6:
			        	print("Give the file name with Extension : ",end=" ")
			        	name=input()
			        	exe=input()
			        	os.system("ssh {0} rm {1}.{2}",format(remote_IP,name,exe))
			        elif int(ch1)==7:
			        	os.system("ls -la")
			        elif int(ch1)==8:
			        	print("Enter the name of the file/folder: ",end=" ")
			        	name=input()
			        	os.system("ls -la | grep {}",format(name))
			        elif int(ch1)==9:
			        	break
			elif int(ch)==3:
				while True:
					print("""
			    		Welcome TO Package Manegment!!!
			    		Some technical work you Have to do first follow the steps :
			    		IN REDHAT FOR THE PACKAGEMENT (rpm)==> It is used to managed the software..
			    		We have to Mount that .iso file to our vmware/virtual box
			    		-----------     VM Ware   --------------------
			    		Player >> Removal Devices >> Settings >> Give the Address of your iso file
			    		--------------------------------------------------------------------------
			    		--------------Virtual Box ----------------------------
			    		>>Device Optical >> Go there and attache the .iso file
			    		-------------------------------------------------------
			    		Press 1:Wants to check that Software is available or not ?
			    		Press 2: Configure Your Yum !
			    		Press 3: To Check Repolist !
			    		Press 4: To install the Software !
			    		Press 5: To Remove any Software !
			    		Press 5: Back
			    		""")
					print("Enter Your Choice: ", end=" ")
					ch1=input()
					if int(ch1)==1:
						print("Enter the name of the Software: ", end=" ")
						name_soft=input()
						os.system("rpm q -a | grep {}".format(name_soft))
					elif int(ch1)==2:
						print("""
							-----FOR Configure Your Yum Need To follow these steps: ------
							Step 1: Go To the loction of the Yum Repo(run cmd)===>>> cd /etc/yum.repos.d/
							Step 2: Now make your own repo file of any name but extension should be (.repo)
							===>>> gedit xyz.repo
							Step 3: Inside the xyz.repo file copy and paste the given data below:
							===>>>
							----------------------------------------------------------------------------
							[dvd1]
							baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream
							gpgcheck=0
							[dvd2]
							baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS
							gpgcheck=0
							---------------------------------------------------------------------------      
							Step 4: Save That file...
							<<<<Now You have completed the Repo work>>>>
							Now you may need some more which are not present in these Repolist::::
							So, You have SetUp two more repolist... You need not do anything I will do
							it for you.....
							PRO TIP: Use Inspite the Use of yum.. you use only dnf...
						""")
						os.system("yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")
						os.system("yum install https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm")
						print("Now YOUR YUM IS CONFIGURED !!")
					elif int(ch1)==3:
						os.system("dnf repolist")
					elif int(ch1)==4:
						print("Enter the name of the valid software: ", end=" ")
						name_soft=input()
						os.system("dnf install {}".format(name_soft))
					elif int(ch1)==5:
						print("Enter the name of the valid Software: ", end=" ")
						name_soft=input()
						os.system("rpm -e {}".format(name_soft))
					elif int(ch1)==6:
						break
			elif int(ch)==4:
				while True:
					print("""
						---------------Welcome To Networking World------------------------
						First we need to stup our lab perfectly.....Follow the steps which are given below:::
						>>>> Network Setting>> Change From NAT to Bridge >>>>
						Now your Lab is ready to use -----> Stop the wifi and then start....
						NOTE: You should have to know the IP of the System B , username ,password and your system
						should be in same network......
						You also need one Software i.e. openssh so press 0
						Press 0:To install ssh !  
						Press 1:For finding Your the IP  !
						Press 2:Ping to the System B !
						Press 3: You Want The Output Of  program From the System B (For the CLI)!
						Press 4: You Wants to transfer the file from System A to B(:/root/) (WE will use scp protocal)!
						Press 5: You Wants to run any programable file (Like written in python) !
						Press 6: You Wants to copy the file from the system  B !
						Press 7: You Wants to copy the folder from the System B !
						Press 8: You Want The Output Of  program From the System B (For the GUI)!
						Press 9: Back !
					""")
					print("Enter Your Choice: ", end=" ")
					ch1=input()
					if int(ch1)==0:
						os.system("dnf install openssh")
					elif int(ch1)==1:
						os.system("ifconfig")
					elif int(ch1)==2:
						print("Enter the IP of the System B: ", end=" ")
						ip_b=input()
						os.system("ping {}".format(ip_b))
					elif int(ch1)==3:
						print("Enter the ip of the system B  and also tell for which program that you wants output: ",end=" ")
						ip_b=input()
						name_soft=input()
						os.system("ssh {} {}".format(ip_b,name_soft))
					elif int(ch1)==4:
						print("Enter the Name of the File: ",end=" ")
						file_name=input()
						print("Enter the IP of the System B: ", end=" ")
						ip_b=input()
						os.system("scp {} {} :/root".format(file_name,ip_b))
					elif int(ch1)==5:
						print("Enter the IP of the System B: ",end=" ")
						ip_b=input()
						print("ENter complete location of that File (like: /root/my.py): ",end=" ")
						location=input()
						os.system("ssh {} python3 {}".format(ip_b,location))
					elif int(ch1)==6:
						print("Enter the IP of the System B: ",end=" ")
						ip_b=input()
						print("Enter the of the file which you wants to copy (like /root/sha.txt): ",end=" ")
						location_b=input()
						print("Enter the location of your that where you wants to copy that file(like /root/): ",end=" ")
						location_a=input()
						os.system("scp {}:{} {}".format(ip_b,location_b,location_a))
					elif int(ch1)==7:
						print("Enter the IP of the system B: ",end=" ")
						ip_b=input()
						print("Enter the location of the folder of the System B(like /root/fold1): ",end=" ")
						location_b=input()
						print("Enter the location of the system A (like /root/): ",end=" ")
						location_a=input()
						os.system("scp -r {}:{} {}".format(ip_b,location_b,location_a))
					elif int(ch1)==8:
						print("Enter the IP of the system B: ",end=" ")
						ip_b=input()
						print("Enter the valid program name: ",end=" ")
						name_soft=input()
						os.system("ssh -X {} {}".format(ip_b,name_soft))
					elif int(ch1)==9:
						break
			elif int(ch)==5:
				while True:
					print("""
						Press 1:To add user !
						Press 2: Delete The User !
						Press 3: Change The password !
						Press 4: Back !
						""")
					print("Enter Your Choice : ")
			elif int(ch)==6:
				while True:
					print("""
						Press 1: Install the HTTPD !
						Press 2: Now the MOve to that Folder where You have keep your Complete Website Folder(WE CAN ALSO CHANGE THIS BY DEFAULT FOLDER) !
						Press 3: Before starting we need to first Disable firewall by which client can access to our server(For Permanently) !
						Press 4: Stop the Firewall (For temprory) !
						Press 5: You Wants to start your Server for temprory !
						Press 6: You wants to start your Server for Permanently !
						Press 7: To see the which ports are working !
						Press 8: Back
						""" )
					print("Enter your Choice: ",end=" ")
					ch1=input()
					if int(ch1)==1:
						os.system("dnf install httpd")
					elif int(ch1)==2:
						print("Go on the loction /var/www/html by >>> cd /var/www/html")
					elif int(ch1)==3:
						os.system("systemctl disable firwalld")
					elif int(ch1)==4:
						os.sytem("systemctl stop firewalld")
					elif int(ch1)==5:
						os.system("systemctl start httpd")
						print("Now your client can access to your Webserver by using >>>> https://your_RHEL_IP:80/webpage_name")
					elif int(ch1)==6:
						os.system("systemctl enable httpd")
						print("Now your client can access to your Webserver by using >>>> https://your_RHEL_IP:80/webpage_name")
					elif int(ch1)==7:
						os.system("netsat -tnlp")
					elif int(ch1)==8:
						break
			elif int(ch)==7:
				while True:
					print("""
						Press 1:To Install NMAP !
						Press 2:Collect the IP which are connected to same Network !
						Press 3:Show the  information about port(Work With the Particular IP)!
						Press 4:Now Just Remove those ports which are inactive !
						Press 5:Now Deploy the Default Script !
						Press 6:Also scan with all the scripts(With High Speed By the use of the -T5) !
						Press 7:Back ! 
						""")
					print("Enter Your Choice: ",end=" ")
					ch1=input()
					if int(ch1)==1:
						os.system("dnf install nmap")
					elif int(ch1)==2:
						print("Enter the starting 3 decimal number(like if your IP=192.163.43.240 then only give input 192.163.43: ",end=" ")
						ip_a=input()
						os.system("nmap -sL {}.0-255".format(ip_a))
					elif int(ch1)==3:
						print("Enter the starting 3 decimal number(like if your IP=192.163.43.240 then only give input 192.163.43: ",end=" ")
						ip_vic=input()
						os.system("nmap -sn -sL {}.0-255".format(ip_vic))
					elif int(ch1)==4:
						print("Choose the victim IP from the upper output and put it here: ",end=" ")
						ip_vic=input()
						os.system("nmap -Pn {}".format(ip_vic))
					elif int(ch1)==5:
						print("Choose the victim IP from the upper output and put it here: ",end=" ")
						ip_vic=input()
						os.system("nmap -Pn --script default {}".format(ip_vic))
					elif int(ch1)==6:
						print("Choose the victim IP from the upper output and put it here: ",end=" ")
						ip_vic=input()
						os.system("nmap -Pn -T5 --script all {}".format(ip_vic))
					elif int(ch1)==7:
						break
			elif int(ch)==8:
				while True:
					print("""
						Press 1: To See The IP and the Gateway Of your Router !
						Press 2: To Remove The Enteries !
						Press 3: To add Gateway !
						Press 4: Back !
						""")
					print("Enter Your Choice : ",end=" ")
					ch1=input()
					if int(ch1)==1:
						os.system("route -n")
					elif int(ch1)==2:
						os.system("route del -net 0.0.0.0")
					elif int(ch1)==3:
						os.system("route add -net 0.0.0.0 gw 10.0.2.2")
					elif int(ch1)==4:
						break
			elif int(ch)==9:
				while True:
					print("""
						<<<<----------------- PARTITION -------------------------->>>>>
						Imp NOTE : SIze Of 1 Sector == 512 bytes == Half Of KiB 
						Press 1: To Display Information About Partition Data Space !
						Press 2: To see that How many HDD are attach with this OS !
						Press 3: For Creating New Virtual HDD (in VM)
						Press 4: List to The Particular HDD !
						Press 5: Create Partition !
						Press 6: Back !
						""")
					print("Enter Your Choice : ",end=" ")
					ch1=input()
					if int(ch1)==1:
						os.system("lvdisplay")
					elif int(ch1)==2:
						os.system("fdisk -l")
					elif int(ch1)==3:
						print("""
							For Creating New Virtual HDD need to follow these steps:
							>>>1.   ShutDown the OS!
							>>> Setting >> Storage >> Controller SATA >> Last ICON (Add New HDD) >>> 
							Create New HDD >>> VOI FORMATE >>> Dynamic Allocated >>> Put Size
							""")
					elif int(ch1)==4:
						print(" Enter information about the Particular Information(like /dev/sda): ", end=" ")
						hdd_info=input()
						os.system("fdisk -l {}".format(hdd_info))
					elif int(ch1)==5:
						print(" Enter information about the Particular HDD(like /dev/sda): ", end=" ")
						hdd_info=input()
						print("Follow the Steps : ")
						os.system("fdisk {}".format(hdd_info))
					elif int(ch1)==6:
						break
						