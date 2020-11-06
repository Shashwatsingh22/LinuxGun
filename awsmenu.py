import os
import getpass

print("\t\t\tWelcome to the LINUX EDITOR using AWS-CLI")

print("\t\t\t--------------------------------------")



print("\t\t\t\t\tMenu")
print("\t\t\t\t\t----")
print("""
 Press  1 : To Login into AWS CLI
 Press  2 : To Launch a instance
 Press  3 : To Start a Instance
 Press  4 : To Stop a Instance 
 Press  5 : To Describe All Instances 
 Press  6 : To Create a Volume
 Press  7 : To Attach volume with instance
 Press  8 : For Partitioning the attached volume
 Press  9 : To configure Web Server
 Press 10 : To Format Partition
 Press 11 : To Mount the Web Server to Volume
 Press 12 : To create a S3 Bucket
 Press 13 : To Upload a local file(or image) to the s3 bucket
 Press 14 : To create CloudFront Distribution using origin as S3 Object-url
 Press 15 : Exit
""")

print("Enter Your Choice : ",end="")

ch=input()


if int(ch) == 1:

    os.system("aws configure")

elif int(ch) == 2:
    print("""
            Press 1:AWS Linux
            Press 2:Redhat Linux
            """)
    print("Enter your Choice :  ",end="")
    img=input()
    if int(img) ==1:
        print("Enter Your Key name: ",end ="")
        key = input()
        os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --subnet-id subnet-ba5b5cd2 --instance-type t2.micro --key-name {} --security-group-ids sg-0c111e5b44f074df9 --count 1".format(key))
    elif int(img) == 2:
        print("Enter Your Key name: ",end ="")
        key = input()
        os.system("aws ec2 run-instances --image-id ami-052c08d70def0ac62 --subnet-id subnet-ba5b5cd2 --instance-type t2.micro --key-name {} --security-group-ids sg-0c111e5b44f074df9 --count 1".format(key))
    print("Successfully launched instance!")

elif int(ch) == 3:

    print("Enter Instance Id : ",end = "")
    uid = input()
    os.system(" aws ec2 start-instances --instance-id {}".format(uid))


elif int(ch) == 4:
    
    print("Enter Instance Id : ",end = "")
    uid = input()
    os.system(" aws ec2 stop-instances --instance-id {}".format(uid))


elif int(ch) == 5:

    os.system("aws ec2 describe-instances")

    
elif int(ch) == 6:

    
    print("Enter Size : ",end = "")
    size = input()
    print("Enter availability zone : ",end = "")
    zone = input()
    print("Enter volume type : ",end= "")
    vtype = input()
    os.system(" aws ec2 create-volume  --availability-zone {} --size {} --volume-type {}".format(zone,size,vtype))


elif int(ch) == 7:


    os.system("tput setaf 3")
    print("\t\t\tVolume Zone & Instance Zone Must be same !!!")
    print("\t\t\t--------------------------------------------")
    os.system("tput setaf 7")
    print("Enter volume-id : ",end = "")
    vid = input()
    print("Enter instance-id : ",end = "")
    iid = input()
    print("Enter device : /dev/",end= "")
    device = input()
    os.system(" aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/{} ".format(vid,iid,device))


elif int(ch) == 8:

    print("Enter IP : ",end = "")
    ip = input()
    print("Enter key : ",end = "")
    key = input()
    print("Enter device : /dev/",end= "")
    device = input()
    os.system(" ssh -l ec2-user {} -i {}.pem sudo fdisk /dev/{} ".format(ip,key,device))



elif int(ch) == 9:

    os.system("tput setaf 3")
    print("\t\t\tHTTPD must be installed...")
    print("\t\t\t--------------------------")
    os.system("tput setaf 7")
    print("Enter IP : ",end = "")
    ip = input()
    print("Enter key : ",end = "")
    key = input()
    os.system(" ssh -l ec2-user {} -i {}.pem sudo systemctl start httpd ".format(ip,key))


elif int(ch) == 10:

    print("Enter IP : ",end = "")
    ip = input()
    print("Enter key : ",end = "")
    key = input()
    print("Enter Device : /dev/",end="")
    device = input()
    os.system(" ssh -l ec2-user {} -i {}.pem sudo mkfs.ext4 /dev/{} ".format(ip,key,device))


elif int(ch) == 11:

    print("Enter IP : ",end = "")
    ip = input()
    print("Enter key : ",end = "")
    key = input()
    print("Enter Device : /dev/",end="")
    device = input()
    os.system(" ssh -l ec2-user {} -i {}.pem sudo mount /dev/{} /var/www/html/ ".format(ip,key,device))


elif int(ch) == 12:
    
    print("Enter region : ",end = "")
    region_name = input()
    print("Enter your bucket name: ",end ="")
    bname= input()
    os.system(" aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}".format(bname,region_name,region_name))


elif int(ch) == 13:

    print("Enter local file path: ",end ="")
    path = input()
    print("Enter your s3 bucket name: ",end= "")
    bname = input()
    os.system(" aws s3 sync {} s3://{} ".format(path,bname))


elif int(ch) == 14:
    
    print("Enter your s3 bucket name: ",end= "")
    bname = input()
    print("Enter region where s3 create a bucket (such as ap-south-1): ",end = "")
    region_name = input()
    os.system(" aws cloudfront create-distribution --origin-domain-name {}.s3.{}.amazonaws.com ".format(bname,region_name))


elif int(ch) == 15:
    exit()
    
else:
    print("You Entered Wrong Choice ...")


