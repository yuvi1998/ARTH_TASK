import subprocess as sp
import os
import getpass as gp
from lxml import etree as ET




def linuxbasic(ssh):

	while True :

		os.system("clear")
		os.system("tput setaf 3")
		print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~ Welcome to Linux Basic menu ~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
		print("Before installing any software/program configure yum once if not configured : Press 34")
		os.system("tput setaf 6")
		menu="""
		\t\tPress 1 :To open file explorer
		\t\tPress 2 :To open gedit text editor
		\t\tPress 3 :To open firefox
		\t\tPress 4 :To open file in vim text editor
		\t\tPress 5 :To open Terminal window
		\t\tPress 6 :To open settings
		\t\tPress 7 :To open audio player
		\t\tPress 8 :To open calculator
		\t\tPress 9 :To open camera
		\t\tPress 10 :To open video player
		\t\tPress 11 :To open mails
		\t\tPress 12 :To open calender
		\t\tPress 13 :To open contacts
		\t\tPress 14 :To see current date and time

		\t\tPress 15:To see all disks info
		\t\tPress 16 :To see all partitions and their mount points
		\t\tPress 17:To query about a software/ program
		\t\tPress 18:To download and install software from internet link
		\t\tPress 19:To install a software

		\t\tPress 20 :To start/stop/enable/disable or check status of service
		\t\tPress 21 :To see info of memory(RAM)
		\t\tPress 22 :To see IP of a domain name 
		\t\tPress 23 :To See contents of present directory
		\t\tPress 24 :To go inside a folder
		\t\tPress 25 :To delete a file/folder

		\t\tPress 27 :To check connectivity to an server or IP
		\t\tPress 28:To check status of all network-interfaces
		\t\tPress 29:To check status of all internet connections of your system
		\t\tPress 30:To on/off your network connection
		\t\tPress 31:To see your IP and ethernet cards attached
		\t\tPress 32:To transfer file to other linux system
		\t\tPress 33:To uninstall/remove a software
		\t\tPress 34:To configure yum repository
		\t\tPress 35:To go back to main menu or exit from this menu
		\n"""
		print(menu)
		os.system("tput setaf 7")
		task = input("Enter your choice : ")

		if(ssh == ""):
			#local system
			
			if task == '1':
				output = sp.getstatusoutput("nautilus &")
			elif task == '2':
				file = input("If you want to open a file then enter 'file name' else 'press enter' : ")
				output =sp.getstatusoutput("gedit {} &".format(file) )
			elif task == '3':
				output =sp.getstatusoutput("firefox &")
			elif task == '4':
				file = input("Enter file path which you want to open : ")
				rc = os.system("vim {}".format(file))
				if(rc == 0):
					output=(0,"")
			elif task == '5':
				output =sp.getstatusoutput("gnome-terminal &")
			elif task == '6':
				output =sp.getstatusoutput("gnome-control-center &")
			elif task == '7':
				output =sp.getstatusoutput("rhythmbox &")
			elif task == '8':
				output =sp.getstatusoutput("gnome-calculator &")
			elif task == '9':
				output =sp.getstatusoutput("cheese &")
			elif task == '10':
				output =sp.getstatusoutput("totem &")
			elif task == '11':
				output =sp.getstatusoutput("evolution -c mails &")
			elif task == '12':
				output =sp.getstatusoutput("evolution -c calender &")
			elif task == '13':
				output =sp.getstatusoutput("evolution -c contacts &")
			elif task == '14':
				output =sp.getstatusoutput("date")
			elif task == '15':
				output =sp.getstatusoutput("fdisk -l")
			elif task == '16':
				output =sp.getstatusoutput("lsblk")
				print(output[1])
				output =sp.getstatusoutput("df -h")
			elif task == '17':
				software = input("Enter package/software name about which you want to query : ")
				output =sp.getstatusoutput("rpm -q {}".format(software))
			elif task == '18':
				link = input("Enter link to download : ")
				output =sp.getstatusoutput("yum install {}".format(link))
			elif task == '19':
				software = input("Enter package/software name which you want to install : ")
				os.system("yum install {}".format(software))
				ouput = output =sp.getstatusoutput("rpm -q {}".format(software))
			elif task == '20':
				status = input("Enter [start / stop / enable / disable / status] according to your requirement : ")
				service = input("Enter service name : ")
				output =sp.getstatusoutput("systemctl {} {}".format(status,service))
				output =sp.getstatusoutput("systemctl status {}".format(service))
			elif task == '21':
				output =sp.getstatusoutput("free -m")
			elif task == '22':
				domain = input("Enter domain name : ")
				output =sp.getstatusoutput("nslookup {}".format(domain))
			elif task == '23':
				print("Present directory :")
				os.system("pwd")
				output =sp.getstatusoutput("ls")
			elif task == '24':
				folder = input("Enter folder path : ")
				output =sp.getstatusoutput("cd {}".format(folder))
			elif task == '25':
				content = input("What do you want to delete [file / folder] : ")
				path = input("Enter {} path which you want to delete : ".format(content))
				if(content == 'folder'):
					output =sp.getstatusoutput("rm -rf {}".format(path))
				else:
					output =sp.getstatusoutput("rm {}".format(path))
			elif task == '26':
				output =sp.getstatusoutput("netstat -tnlp")
			elif task == '27':
				ip = input("Enter IP or domain name to which you want to check connectivity : ")
				output =sp.getstatusoutput("ping -c 4 {}".format(ip))
			elif task == '28':
				output =sp.getstatusoutput("nmcli")
			elif task == '29':
				output =sp.getstatusoutput("nmcli connection show")
			elif task == '30':
				card = input("Enter your ethernet card name : ")
				status = input("Enter ['up' for on and 'down' for off] as per requirement : ")
				output =sp.getstatusoutput("nmcli connection {} {}".format(status,card))
			elif task == '31':
				output =sp.getstatusoutput("ifconfig")
			elif task == '32':
				ip = input("Enter IP of system to which you want to send file : ")
				user = input("Enter username to to which you want to send file : ")
				src = input("Enter your source file path which you want to send : ")
				dest = input("Enter destination folder path where you want to copy : ")
				output =sp.getstatusoutput("scp {} {}@{}:{}".format(src, user,ip,dest))

			elif task == '33':
				software = input("Enter package/software name which you want to uninstall : ")
				rc = os.system("yum remove {}".format(software))
				if(rc == 0):
					output = (0, "Successfully removed!!")

			elif task == '34':
				print("Configuring yum. please Wait!!!")
				output = sp.getstatusoutput("yum install --nogpgcheck https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")
				os.system("yum repolist")


			elif task == '35':
				break;

			else:
				print("Invalid Choice!!! Try Again")
				os.system("sleep 1")
				continue

			if output[0] == 0:
				os.system("tput setaf 2")
				print("Task successfully completed !!")
				os.system("tput setaf 7")
				print(output[1])
			else:
				os.system("tput setaf 5")
				print("Oops !! Some error occurred : {}".format(output[1]))

			os.system("tput setaf 6")
			input("'Press enter' to continue :")
			os.system("tput setaf 7")
			
		else:

			#remote system

			if task == '1':
				output = sp.getstatusoutput("{} -X nautilus".format(ssh))
			elif task == '2':
				file = input("If you want to open a file then enter 'file name' else 'press enter' : ")
				output =sp.getstatusoutput("{} -X 'gedit {}'".format(ssh,file))
			elif task == '3':
				output =sp.getstatusoutput("{} -X firefox".format(ssh))
			elif task == '4':
				file = input("Enter file path which you want to open : ")
				rc = os.system("{} 'vim {}'".format(ssh,file))
				if(rc == 0):
					output=(0,"")
			elif task == '5':
				output =sp.getstatusoutput("{} -X gnome-terminal".format(ssh))
			elif task == '6':
				output =sp.getstatusoutput("{} -X gnome-control-center".format(ssh))
			elif task == '7':
				output =sp.getstatusoutput("{} -X rhythmbox".format(ssh))
			elif task == '8':
				output =sp.getstatusoutput("{} -X gnome-calculator".format(ssh))
			elif task == '9':
				output =sp.getstatusoutput("{} -X cheese".format(ssh))
			elif task == '10':
				output =sp.getstatusoutput("{} -X totem".format(ssh))
			elif task == '11':
				output =sp.getstatusoutput("{} -X evolution -c mails".format(ssh))
			elif task == '12':
				output =sp.getstatusoutput("{} -X evolution -c calender".format(ssh))
			elif task == '13':
				output =sp.getstatusoutput("{} -X evolution -c contacts".format(ssh))
			elif task == '14':
				output =sp.getstatusoutput("{} date".format(ssh))
			elif task == '15':
				output =sp.getstatusoutput("{} 'fdisk -l'".format(ssh))
			elif task == '16':
				output =sp.getstatusoutput("{} lsblk".format(ssh))
				print(output[1])
				output =sp.getstatusoutput("{} 'df -h'".format(ssh))
			elif task == '17':
				software = input("Enter package/software name about which you want to query : ")
				output =sp.getstatusoutput("{} 'rpm -q {}'".format(ssh,software))
			elif task == '18':
				link = input("Enter link to download : ")
				output =sp.getstatusoutput("{} 'yum install {}'".format(ssh,link))
			elif task == '19':
				software = input("Enter package/software name which you want to install : ")
				os.system("{} 'yum install {}'".format(ssh,software))
				ouput = output =sp.getstatusoutput("{} 'rpm -q {}'".format(ssh,software))
			elif task == '20':
				status = input("Enter [start / stop / enable / disable / status] according to your requirement : ")
				service = input("Enter service name : ")
				output =sp.getstatusoutput("{} systemctl {} {}".format(ssh,status,service))
				output =sp.getstatusoutput("{} systemctl status {}".format(ssh,service))
			elif task == '21':
				output =sp.getstatusoutput("{} free -m".format(ssh))
			elif task == '22':
				domain = input("Enter domain name : ")
				output =sp.getstatusoutput("{} 'nslookup {}'".format(ssh,domain))
			elif task == '23':
				print("Present directory :")
				os.system("{} pwd".format(ssh))
				output =sp.getstatusoutput("{} ls".format(ssh))
			elif task == '24':
				folder = input("Enter folder path : ")
				output =sp.getstatusoutput("{} 'cd {}'".format(ssh,folder))
			elif task == '25':
				content = input("What do you want to delete [file / folder] : ")
				path = input("Enter {} path which you want to delete : ".format(content))
				if(content == 'folder'):
					output =sp.getstatusoutput("{} 'rm -rf {}'".format(ssh,path))
				else:
					output =sp.getstatusoutput("{} 'rm {}'".format(ssh,path))
			elif task == '26':
				output =sp.getstatusoutput("{} 'netstat -tnlp'".format(ssh))
			elif task == '27':
				ip = input("Enter IP or domain name to which you want to check connectivity : ")
				output =sp.getstatusoutput("{} 'ping -c 4 {}'".format(ssh,ip))
			elif task == '28':
				output =sp.getstatusoutput("{} nmcli".format(ssh))
			elif task == '29':
				output =sp.getstatusoutput("{} 'nmcli connection show'".format(ssh))
			elif task == '30':
				card = input("Enter your ethernet card name : ")
				status = input("Enter ['up' for on and 'down' for off] as per requirement : ")
				output =sp.getstatusoutput("{} 'nmcli connection {} {}'".format(ssh,status,card))
			elif task == '31':
				output =sp.getstatusoutput("{} ifconfig".format(ssh))
			elif task == '32':
				ip = input("Enter IP of system to which you want to send file : ")
				user = input("Enter username to to which you want to send file : ")
				src = input("Enter your source file path which you want to send : ")
				dest = input("Enter destination folder path where you want to copy : ")
				output =sp.getstatusoutput("{} 'scp {} {}@{}:{}'".format(ssh,src, user,ip,dest))

			elif task == '33':
				software = input("Enter package/software name which you want to uninstall : ")
				rc = os.system("{} yum remove {}".format(ssh,software))
				if(rc == 0):
					output = (0, "Successfully removed!!")

			elif task == '34':
				print("Configuring yum. please Wait!!!")
				output = sp.getstatusoutput("{} 'yum install --nogpgcheck https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm'".format(ssh))
				os.system("{} 'yum repolist'".format(ssh))



			elif task == '35':
				break;

			else:
				print("Invalid Choice!!! Try Again")
				os.system("sleep 1")
				continue

			if output[0] == 0:
				os.system("tput setaf 2")
				print("Task successfully completed !!")
				os.system("tput setaf 7")
				print(output[1])
			else:
				os.system("tput setaf 5")
				print("Oops !! Some error occurred : {}".format(output[1]))

			os.system("tput setaf 6")
			input("'Press enter' to continue :")
			os.system("tput setaf 7")
			



def staticpartitions(ssh):

	while True :

		os.system("clear")
		os.system("tput setaf 3")
		print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~ Welcome to our Partition menu ~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
		os.system("tput setaf 6")
		menu="""
		\t\tPress 1 :To see all disks available
		\t\tPress 2 :To see info of all existing partitions and their mount points
		\t\tPress 3 :To create a static partition
		\t\tPress 4 :To delete a Partition
		\t\tPress 5 :To go back to main menu or exit from this menu\n"""
		print(menu)
		os.system("tput setaf 7")
		task = input("Enter your choice : ")

		if(ssh == ""):
			#local system

			if task == '1':
				output = sp.getstatusoutput("fdisk -l")
			elif task == '2':
				output =sp.getstatusoutput("lsblk")
				print(output[1])
				output =sp.getstatusoutput("df -h")
			elif task == '3':
				dname =input ("Enter disk name in which you want to create partition : ")
				mountpt = input("Enter a folder path to which you want to link partition : ")
				os.system("tput setaf 3")
				print("Enter 'n'  to create new partition")
				print(" Select Partition type as ['p' for primary / 'e' for extended] : ")
				print("Enter 'w' to save changes after creating partition.")
				os.system("tput setaf 7")
				os.system("fdisk {}".format(dname))
				print(os.system("lsblk"))
				pname = input("Enter partition name created : ")
				output = sp.getstatusoutput("mkfs.ext4 {}".format(pname))
				print(output[1],"\n") 
				if(output[0] == 0):
					os.system("mkdir {}".format(mountpt))
					output = sp.getstatusoutput("mount {} {}".format(pname,mountpt))
				info = sp.getstatusoutput("df -h")
				print(info[1])
				
			
			elif task == '4':
				dname =input ("Enter disk name in which you want to delete partition : ")
				pname = input("Enter partition name to be deleted : ")
				output = sp.getstatusoutput("umount {}".format(pname))
				os.system("tput setaf 3")
				print("Enter 'd' to delete partition")
				print("Enter 'w' to save changes after deleting partition.")
				os.system("tput setaf 7")
				if(output[0] == 0):
					os.system("fdisk {}".format(dname))
				output = sp.getstatusoutput("lsblk")

			elif task == '5':
				break;
			else:
				print("Invalid Choice!!! Try Again")
				os.system("sleep 1")
				continue

		else:
			#Remote system
			if task == '1':
				output = sp.getstatusoutput("{} 'fdisk -l'".format(ssh))
			elif task == '2':
				output =sp.getstatusoutput("{} lsblk".format(ssh))
				print(output[1])
				output =sp.getstatusoutput("{} 'df -h'".format(ssh))
			elif task == '3':
				dname =input ("Enter disk name in which you want to create partition : ")
				mountpt = input("Enter a folder path to which you want to link partition : ")
				os.system("tput setaf 3")
				print("Enter 'n'  to create new partition")
				print(" Select Partition type as ['p' for primary / 'e' for extended] : ")
				print("Enter 'w' to save changes after creating partition.")
				os.system("tput setaf 7")
				os.system("{} 'fdisk {}'".format(sshdname))
				print(os.system("{} lsblk".format(ssh)))
				pname = input("Enter partition name created : ")
				output = sp.getstatusoutput("{} 'mkfs.ext4 {}'".format(ssh,pname))
				print(output[1],"\n") 
				if(output[0] == 0):
					os.system("{} 'mkdir {}'".format(ssh,mountpt))
					output = sp.getstatusoutput("{} 'mount {} {}'".format(ssh,pname,mountpt))
				info = sp.getstatusoutput("{} 'df -h'".format(ssh))
				print(info[1])
				
			
			elif task == '4':
				dname =input ("Enter disk name in which you want to delete partition : ")
				pname = input("Enter partition name to be deleted : ")
				output = sp.getstatusoutput("{} 'umount {}'".format(ssh,pname))
				os.system("tput setaf 3")
				print("Enter 'd' to delete partition")
				print("Enter 'w' to save changes after deleting partition.")
				os.system("tput setaf 7")
				if(output[0] == 0):
					os.system("{} 'fdisk {}'".format(ssh,dname))
				output = sp.getstatusoutput("{} lsblk".format(ssh))

			elif task == '5':
				break;
			else:
				print("Invalid Choice!!! Try Again")
				os.system("sleep 1")
				continue

		if output[0] == 0:
			os.system("tput setaf 2")
			print("Task successfully completed !!")
			os.system("tput setaf 7")
			print(output[1])
		else:
			os.system("tput setaf 5")
			print("Oops !! Some error occurred : {}".format(output[1]))

		os.system("tput setaf 6")
		input("'Press enter' to continue :")
		os.system("tput setaf 7")


def lvm(ssh):

	while True :


		os.system("clear")
		os.system("tput setaf 3")
		print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~ Welcome to our LVM menu ~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
		os.system("tput setaf 6")
		menu="""
		\t\tPress 1 :To see all disks available
		\t\tPress 2 :To see info of all existing virtual group
		\t\tPress 3 :To see info of a existing virtual group
		\t\tPress 4 :To see info of lv partition
		\t\tPress 5 :To see info of all partitions with their mount points\n
		\t\tPress 6 :To create virtual group
		\t\tPress 7 :To create an lv partition
		\t\tPress 8 :To resize a lv partition
		\t\tPress 9 :To remove a virtual group
		\t\tPress 10 :To delete a Partition
		\t\tPress 11 :To go back to main menu or exit from this menu\n"""
		print(menu)
		os.system("tput setaf 7")
		task = input("Enter your choice : ")

		if ssh == "":
			#local system

			if task == '1':
				output = sp.getstatusoutput("fdisk -l")
			elif task == '2':
				output = sp.getstatusoutput("vgdisplay")

			elif task == '3':
				vgname = input("Enter virtual group name : ")
				output = sp.getstatusoutput("vgdisplay {}".format(vgname))

			elif task == '4':
				vgname = input("Enter virtual group name : ")
				lvname = input("Enter logical volume name : ")
				output = sp.getstatusoutput("lvdisplay {}/{}".format(vgname,lvname))

			elif task == '5':
				output = sp.getstatusoutput("df -h")

			elif task == '6':
				vgname=input("Enter virtual group name : ")
				num = input("Enter number of physical volume you want to add : ") 
				num = int(num)
				disks = [input("Enter disk {} name : ".format(i)) for i in range(num)]
				print("disks")
				s = " "
				s = s.join(disks)
				os.system("pvcreate {}".format(s))
				output = sp.getstatusoutput("vgcreate {} {}".format(vgname,s))
				info = sp.getstatusoutput("vgdisplay {}".format(vgname))
				print(info[1])

			elif task == '7':

				vgname =input ("Enter vgname in which you want to create partition : ")
				lvname = input("Enter Logical volume name : ")
				size = input("Enter size of lv [K,M,G,T,P,E] : ")
				mountpt = input("Enter a folder path to which you want to link partition : ")
				output = sp.getstatusoutput("lvcreate -n {} --size {} {} ".format(lvname,size,vgname))
				print(output[1],"\n")
				if(output[0] == 0):
					output = sp.getstatusoutput("mkfs.ext4 /dev/{}/{}".format(vgname,lvname))
					print(output[1],"\n") 
					if(output[0] == 0):
						os.system("mkdir {}".format(mountpt))
						output = sp.getstatusoutput("mount /dev/{}/{} {}".format(vgname,lvname,mountpt))
				info = sp.getstatusoutput("lvdisplay {}/{}".format(vgname,lvname))
				print(info[1])


			elif task == '8':

				vgname =input ("Enter virtual group name in which logicl volume  partition is present : ")
				lvname =input ("Enter logival volume name : ")
				option =input("Enter 'R' to reduce and 'E' to extend size : ")
				size =input ("Enter final size [K,M,G,T,P,E] you want to achieve after extend/reduce : ")
				if option == 'R':
					mountpt = sp.getoutput("findmnt -n -o TARGET /dev/{}/{}".format(vgname,lvname))
					output = sp.getstatusoutput("umount /dev/{}/{}".format(vgname,lvname))
					print(output[1],"\n")
					if(output[0] == 0):
						x = os.system("e2fsck -f /dev/{}/{}".format(vgname,lvname))
						output = sp.getstatusoutput("resize2fs /dev/{}/{} {}".format(vgname,lvname,size))
						print(output[1],"\n")
						if(output[0] == 0):
							print("Enter y if you want to continue else enter n")
							output = sp.getstatusoutput("lvreduce -L {} /dev/{}/{}".format(size,vgname,lvname))
							if(output[0] == 0):
								output=sp.getstatusoutput("mount /dev/{}/{} {}".format(vgname,lvname,mountpt))
									

				elif option == 'E':
					output = sp.getstatusoutput("lvextend -L {} /dev/{}/{}".format(size,vgname,lvname))
					if(output[0] == 0):
						output = sp.getstatusoutput("resize2fs /dev/{}/{}".format(vgname,lvname))
				info = sp.getstatusoutput("lvdisplay {}/{}".format(vgname,lvname))
				print(info[1])

			elif task == '9':
				vgname =input("Enter virtual group name which you wish to delete : ")
				output = sp.getstatusoutput("vgchange -a n {}".format(vgname))
				if(output[0] == 0):
					output = sp.getstatusoutput("vgremove {}".format(vgname))

			elif task == '10':
				vgname =input("Enter virtual group name of which logical volume is a part : ")
				lvname =input("Enter logical volume name which you wish to delete : ")
				output = sp.getstatusoutput("umount /dev/{}/{}".format(vgname,lvname))
				if(output[0] == 0):
					output = sp.getstatusoutput("lvremove -y /dev/{}/{}".format(vgname,lvname))

			elif(task == '11'):
				break;

			else:
				print("Invalid Choice!!! Try Again")
				os.system("sleep 1")
				continue

			if output[0] == 0:
				os.system("tput setaf 2")
				print("Task successfully completed !!")
				os.system("tput setaf 7")
				print(output[1])
			else:
				os.system("tput setaf 5")
				print("Oops !! Some error occurred : {}".format(output[1]))

			os.system("tput setaf 6")
			input("'Press enter' to continue :")
			os.system("tput setaf 7")

		else:
			#remote sys
			if task == '1':
				output = sp.getstatusoutput("{} 'fdisk -l'".format(ssh))
			elif task == '2':
				output = sp.getstatusoutput("{} vgdisplay".format(ssh))

			elif task == '3':
				vgname = input("Enter virtual group name : ")
				output = sp.getstatusoutput("{} 'vgdisplay {}'".format(ssh,vgname))

			elif task == '4':
				vgname = input("Enter virtual group name : ")
				lvname = input("Enter logical volume name : ")
				output = sp.getstatusoutput("{} 'lvdisplay {}/{}'".format(ssh,vgname,lvname))

			elif task == '5':
				output = sp.getstatusoutput("{} 'df -h'".format(ssh))

			elif task == '6':
				vgname=input("Enter virtual group name : ")
				num = input("Enter number of physical volume you want to add : ") 
				num = int(num)
				disks = [input("Enter disk {} name : ".format(i)) for i in range(num)]
				print("disks")
				s = " "
				s = s.join(disks)
				os.system("{} 'pvcreate {}'".format(ssh,s))
				output = sp.getstatusoutput("{} 'vgcreate {} {}' ".format(ssh,vgname,s))
				info = sp.getstatusoutput("{} 'vgdisplay {}' ".format(ssh,vgname))
				print(info[1])

			elif task == '7':

				vgname =input ("Enter vgname in which you want to create partition : ")
				lvname = input("Enter Logical volume name : ")
				size = input("Enter size of lv [K,M,G,T,P,E] : ")
				mountpt = input("Enter a folder path to which you want to link partition : ")
				output = sp.getstatusoutput("{} 'lvcreate -n {} --size {} {}'' ".format(ssh,lvname,size,vgname))
				print(output[1],"\n")
				if(output[0] == 0):
					output = sp.getstatusoutput("{} 'mkfs.ext4 /dev/{}/{}'".format(ssh,vgname,lvname))
					print(output[1],"\n") 
					if(output[0] == 0):
						os.system("{} 'mkdir {}'".format(ssh,mountpt))
						output = sp.getstatusoutput("{} 'mount /dev/{}/{} {}'".format(ssh,vgname,lvname,mountpt))
				info = sp.getstatusoutput("{} 'lvdisplay {}/{}'".format(ssh,vgname,lvname))
				print(info[1])


			elif task == '8':

				vgname =input ("Enter virtual group name in which logicl volume  partition is present : ")
				lvname =input ("Enter logival volume name : ")
				option =input("Enter 'R' to reduce and 'E' to extend size : ")
				size =input ("Enter final size [K,M,G,T,P,E] you want to achieve after extend/reduce : ")
				if option == 'R':
					mountpt = sp.getoutput("{} 'findmnt -n -o TARGET /dev/{}/{}'".format(ssh,vgname,lvname))
					output = sp.getstatusoutput("{} umount /dev/{}/{}'".format(ssh,vgname,lvname))
					print(output[1],"\n")
					if(output[0] == 0):
						x = os.system("{} 'e2fsck -f /dev/{}/{}'".format(ssh,vgname,lvname))
						output = sp.getstatusoutput("{} 'resize2fs /dev/{}/{} {}'".format(ssh,vgname,lvname,size))
						print(output[1],"\n")
						if(output[0] == 0):
							print("Enter y if you want to continue else enter n")
							output = sp.getstatusoutput("{} 'lvreduce -L {} /dev/{}/{}'".format(ssh,size,vgname,lvname))
							if(output[0] == 0):
								output=sp.getstatusoutput("{} 'mount /dev/{}/{} {}'".format(ssh,vgname,lvname,mountpt))
									

				elif option == 'E':
					output = sp.getstatusoutput("{} 'lvextend -L {} /dev/{}/{}'".format(ssh,size,vgname,lvname))
					if(output[0] == 0):
						output = sp.getstatusoutput("{} 'resize2fs /dev/{}/{}'".format(ssh,vgname,lvname))
				info = sp.getstatusoutput("{} 'lvdisplay {}/{}'".format(ssh,vgname,lvname))
				print(info[1])

			elif task == '9':
				vgname =input("Enter virtual group name which you wish to delete : ")
				output = sp.getstatusoutput("{} 'vgchange -a n {}'".format(ssh,vgname))
				if(output[0] == 0):
					output = sp.getstatusoutput("{} 'vgremove {}'".format(ssh,vgname))

			elif task == '10':
				vgname =input("Enter virtual group name of which logical volume is a part : ")
				lvname =input("Enter logical volume name which you wish to delete : ")
				output = sp.getstatusoutput("{} 'umount /dev/{}/{}'".format(ssh,vgname,lvname))
				if(output[0] == 0):
					output = sp.getstatusoutput("{} 'lvremove -y /dev/{}/{}'".format(ssh,vgname,lvname))

			elif(task == '11'):
				break;

			else:
				print("Invalid Choice!!! Try Again")
				os.system("sleep 1")
				continue

			if output[0] == 0:
				os.system("tput setaf 2")
				print("Task successfully completed !!")
				os.system("tput setaf 7")
				print(output[1])
			else:
				os.system("tput setaf 5")
				print("Oops !! Some error occurred : {}".format(output[1]))

			os.system("tput setaf 6")
			input("'Press enter' to continue :")
			os.system("tput setaf 7")
			

			



def hadoop(ssh,user,rsip):

	while True:

		os.system("clear")
		os.system("tput setaf 3")
		print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~ Welcome to our hadoop menu ~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
		os.system("tput setaf 6")
		menu = """
		\t\tPress 1 : Configure system as Namenode / Datanode
		\t\tPress 2 : Start Namenode / Datanode
		\t\tPress 3 : Configure system as Client
		\t\tPress 4 : See Cluster Information\n
		\t\tPress 5 : Client Operation : Upload File 
		\t\tPress 6 : Client Operation : Read File
		\t\tPress 7 : Client Operation : Create an Empty file
		\t\tPress 8 : Client Operation : Delete a file
		\t\tPress 9 : Client Operation : list all contents in Cluster
		\t\tPress 10 : Stop Namenode / Datanode
		\t\tPress 11 : To go back to main menu or exit from this menu\n"""

		print(menu)

		os.system("tput setaf 7")
		task = input("\t\t\tWhat do you want to do ? : ")

		if ssh == "":
			#local

			if(task == '1'):
				node = input("Enter 'master'/'slave' if you want to configure as 'namenode' / 'datanode' : ")
				folder = input("Enter datanode / namenode folder path : ")
				ip = input("Enter namenode IP address : ")
				sp.getstatusoutput("mkdir {}".format(folder))

				#hdfs-site configure
				htree = ET.parse("/etc/hadoop/hdfs-site.xml")
				hroot = htree.getroot()
				if(len(hroot) == 0):
					hp = ET.SubElement(hroot, 'property')
				else:
					hp = hroot[0]
				if(len(hp) == 0):
					hn = ET.SubElement(hp, 'name')
					hv = ET.SubElement(hp,'value')
				else:
					hn = hp[0]
					hv = hp[1]

				

				#core-site configure
				ctree = ET.parse("/etc/hadoop/core-site.xml")
				croot = ctree.getroot()
				if len(croot == 0):
					cp = ET.SubElement(croot, 'property')
				else:
					cp = croot[0]
				if(len(cp) == 0):
					cn = ET.SubElement(cp, 'name')
					cv = ET.SubElement(cp,'value')
				else:
					cn = cp[0]
					cv = cp[1]

				
				cn.text = "fs.default.name"
				cv.text = "hdfs://{}:9001".format(ip)

				ctree.write("/etc/hadoop/core-site.xml",pretty_print=True)

				if node == 'master':
					hn.text = "dfs.name.dir"
					hv.text =  folder
					htree.write("/etc/hadoop/hdfs-site.xml",pretty_print=True)

					print("Namenode configured !!!")
					print("Enter password to start Namenode folder formatting....")

					rc = os.system("hadoop namenode -format")
					if(rc == 0):
						output = sp.getstatusoutput("hadoop-daemon.sh start namenode")
				else:
					hn.text = "dfs.data.dir"
					hv.text =  folder
					htree.write("/etc/hadoop/hdfs-site.xml",pretty_print=True)
					output = sp.getstatusoutput("hadoop-daemon.sh start datanode")
			

			elif(task == '2'):
				node = input("Enter 'master'/'slave' if you want to start  'namenode' / 'datanode' ")
				if(node == 'master'):
					output = sp.getstatusoutput("hadoop-daemon.sh start namenode")
				else:
					output = sp.getstatusoutput("hadoop-daemon.sh start datanode")

			elif(task =='3'):
				ip = input("Enter namenode IP address : ")
				ctree = ET.parse("/etc/hadoop/core-site.xml")
				croot = ctree.getroot()
				if(len(croot) == 0):
					cp = ET.SubElement(croot, 'property')
				else:
					cp = croot[0]
				if(len(cp) == 0):
					cn = ET.SubElement(cp, 'name')
					cv = ET.SubElement(cp,'value')
				else:
					cn = cp[0]
					cv = cp[1]

				
				cn.text = "fs.default.name"
				cv.text = "hdfs://{}:9001".format(ip)

			elif(task == '4'):
				output = sp.getstatusoutput("hadoop dfsadmin -report | less")

			elif(task == '5'):
				file = input("Enter path of the file which you want to upload : ")
				print("Uploading may take several seconds... Please be patient!!")
				output = sp.getstatusoutput("hadoop fs -put {} /".format(file))


			elif(task == '6'):
				file = input("Enter path of file  which you want to read: ")
				output = sp.getstatusoutput("hadoop fs -cat {}".format(file))

			elif(task == '7'):
				file = input("Enter file path with name which you want to create (eg - /<foldername>/<filename>) : ")
				output = sp.getstatusoutput("hadoop fs -touchz {}".format(file))

			elif(task == '8'):
				file = input("Enter path of file  which you want to remove from cluster : ")
				output = sp.getstatusoutput("hadoop fs -rm {}".format(file))

			elif(task =='9'):
				output = sp.getstatusoutput("hadoop fs -ls /")

			elif(task == '10'):
				node = input("Enter 'master'/'slave' if you want to stop  'namenode' / 'datanode' ")
				if(node == 'master'):
					output = sp.getstatusoutput("hadoop-daemon.sh stop namenode")
				else:
					output = sp.getstatusoutput("hadoop-daemon.sh stop datanode")

			elif(task == '11'):
				break;

			else:
				print("Invalid Option!!")
				os.system("sleep 2")
				continue

			if output[0] == 0:
				os.system("tput setaf 2")
				print("Task successfully completed !!")
				os.system("tput setaf 7")
				print(output[1])
			else:
				os.system("tput setaf 5")
				print("Oops !! Some error occurred : {}".format(output[1]))

			os.system("tput setaf 6")
			input("'Press enter' to continue :")
			os.system("tput setaf 7")

		else:
			#remote sys
			if(task == '1'):
				node = input("Enter 'master'/'slave' if you want to configure as 'namenode' / 'datanode' : ")
				folder = input("Enter datanode / namenode folder path : ")
				ip = input("Enter namenode IP address : ")
				print("Enter password to create namenode folder....")
				sp.getstatusoutput("{} 'mkdir {}'".format(ssh,folder))

				#hdfs-site configure
				sp.getstatusoutput("touch hdfs-site.xml")
				sp.getstatusoutput("echo '<configuration>\n</configuration>' > hdfs-site.xml")
				htree = ET.parse("hdfs-site.xml")
				hroot = htree.getroot()
				
				hp = ET.SubElement(hroot, 'property')
				hn = ET.SubElement(hp, 'name')
				hv = ET.SubElement(hp,'value')
				

				

				#core-site configure
				sp.getstatusoutput("touch core-site.xml")
				sp.getstatusoutput("echo '<configuration>\n</configuration>' > core-site.xml")
				ctree = ET.parse("core-site.xml")
				croot = ctree.getroot()
				
				cp = ET.SubElement(croot, 'property')
				cn = ET.SubElement(cp, 'name')
				cv = ET.SubElement(cp,'value')

				print("Enter password to configure hadoop files....")
				sp.getstatusoutput("{} 'rm /etc/hadoop/hdfs-site.xml /etc/hadoop/core-site.xml'".format(ssh))
				
				
				cn.text = "fs.default.name"
				cv.text = "hdfs://{}:9001".format(ip)


				ctree.write("core-site.xml",pretty_print=True)
				sp.getstatusoutput("scp core-site.xml {}@{}:/etc/hadoop/".format(user,rsip))

				if node == 'master':
					hn.text = "dfs.name.dir"
					hv.text =  folder
					htree.write("hdfs-site.xml",pretty_print=True)
					sp.getstatusoutput("scp hdfs-site.xml {}@{}:/etc/hadoop/".format(user,rsip))
					print("Namenode configured !!!")
					print("Enter password to start Namenode folder formatting....")


					rc = os.system("{} 'hadoop namenode -format'".format(ssh))
					if(rc== 0):
						output = sp.getstatusoutput("{} 'hadoop-daemon.sh start namenode'".format(ssh))
				else:
					hn.text = "dfs.data.dir"
					hv.text =  folder
					htree.write("hdfs-site.xml",pretty_print=True)
					sp.getstatusoutput("scp hdfs-site.xml {}@{}:/etc/hadoop/".format(user,rsip))
					output = sp.getstatusoutput("{} 'hadoop-daemon.sh start datanode'".format(ssh))

				sp.getstatusoutput("rm hdfs-site.xml")
				sp.getstatusoutput("rm core-site.xml")
			

			elif(task == '2'):
				node = input("Enter 'master'/'slave' if you want to start  'namenode' / 'datanode' ")
				if(node == 'master'):
					output = sp.getstatusoutput("{} hadoop-daemon.sh start namenode".format(ssh))
				else:
					output = sp.getstatusoutput("{} hadoop-daemon.sh start datanode".format(ssh))

			elif(task =='3'):
				ip = input("Enter namenode IP address : ")

				sp.getstatusoutput("touch core-site.xml")
				sp.getstatusoutput("echo '<configuration>\n</configuration>' > core-site.xml")
				sp.getstatusoutput("{} 'rm /etc/hadoop/core-site.xml'".format(ssh))
				ctree = ET.parse("core-site.xml")
				croot = ctree.getroot()
				
				cp = ET.SubElement(croot, 'property')
				cn = ET.SubElement(cp, 'name')
				cv = ET.SubElement(cp,'value')
				

				cn.text = "fs.default.name"
				cv.text = "hdfs://{}:9001".format(ip)
				ctree.write("core-site.xml",pretty_print=True)

				output =sp.getstatusoutput("scp core-site.xml {}@{}:/etc/hadoop/".format(user,rsip))
				sp.getstatusoutput("rm core-site.xml")

			elif(task == '4'):
				output = sp.getstatusoutput("{} 'hadoop dfsadmin -report | less'".format(ssh))

			elif(task == '5'):
				file = input("Enter path of the file which you want to upload : ")
				print("Uploading may take several seconds... Please be patient!!")
				output = sp.getstatusoutput("{} 'hadoop fs -put {} /'".format(ssh,file))


			elif(task == '6'):
				file = input("Enter path of file  which you want to read: ")
				output = sp.getstatusoutput("{} 'hadoop fs -cat {}'".format(ssh,file))

			elif(task == '7'):
				file = input("Enter file path with name which you want to create (eg - /<foldername>/<filename>) : ")
				output = sp.getstatusoutput("{} 'hadoop fs -touchz {}'".format(ssh,file))

			elif(task == '8'):
				file = input("Enter path of file  which you want to remove from cluster : ")
				output = sp.getstatusoutput("{} 'hadoop fs -rm {}'".format(ssh,file))

			elif(task =='9'):
				output = sp.getstatusoutput("{} 'hadoop fs -ls /'".format(ssh))

			elif(task == '10'):
				node = input("Enter 'master'/'slave' if you want to stop  'namenode' / 'datanode' ")
				if(node == 'master'):
					output = sp.getstatusoutput("{} hadoop-daemon.sh stop namenode".format(ssh))
				else:
					output = sp.getstatusoutput("{} hadoop-daemon.sh stop datanode".format(ssh))

			elif(task == '11'):
				break;

			else:
				print("Invalid Option!!")
				os.system("sleep 2")
				continue

			if output[0] == 0:
				os.system("tput setaf 2")
				print("Task successfully completed !!")
				os.system("tput setaf 7")
				print(output[1])
			else:
				os.system("tput setaf 5")
				print("Oops !! Some error occurred : {}".format(output[1]))

			os.system("tput setaf 6")
			input("'Press enter' to continue :")
			os.system("tput setaf 7")

def aws(ssh):

	

	while True:

		os.system("clear")
		os.system("tput setaf 3")
		print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~ Welcome to our AWS menu ~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
		os.system("tput setaf 6")

		mainmenu="""
		\t\tPress 1 : Login to aws account
		\t\tPress 2 : Create key pair
		\t\tPress 3 : Create security group
		\t\tPress 4 : Add inbound rules
		\t\tPress 5 : Launch EC2 instance
		\t\tPress 6 : Create EBS volume
		\t\tPress 7 : Attach EBS to EC2 instance
		\t\tPress 8 : Create S3 bucket
		\t\tPress 9: Launch Distribution
		\t\tPress 10: Shows all existing EC2 instances
		\t\tPress 11: Shows all existing key-pairs
		\t\tPress 12: Shows all existing security-groups
		\t\tPress 13: To stop instance
		\t\tPress 14: To start existing instance
		\t\tPress 15: To change the bucket permission 
		\t\tPress 16: To upload image in S3 bucket
		\t\tPress 17 :To go back to main menu or exit from this menu\n"""
		print(mainmenu)

		os.system("tput setaf 7")
		task = input("Enter your choice : ")
		
		if ssh == "":
			#local sys

			if task == '1':
				rc=os.system("aws configure")
				if(rc == 0):
					output=(0,'Login Successful')

			elif task == '2':
				keyname = input("Enter Key name : ")
				output = sp.getstatusoutput("aws ec2 create-key-pair --key-name {}".format(keyname))
			elif task == '3':
				grpname = input("Enter Security group name : ")
				description = input("Give Description of your security group : ")
				output = sp.getstatusoutput("aws ec2 create-security-group --group-name {} --description {} --vpc-id vpc-c62ecead".format(grpname,description))
			elif task == '4':
				grpid = input("Enter groyp id : ")
				protocol = input("Enter protocol you want to add : ")
				port = input("Enter port number : ")
				output = sp.getstatusoutput("aws ec2 authorize-security-group-ingress --group-id {} --protocol {} --port {} --cidr 0.0.0.0/0".format(grpid,protocol,port))
			elif task == '5':
				image = input("Enter image id : ")
				instance = input("Enter instance-type : ")
				count = input("Enter no.of instance you want to launch : ")
				sgid = input("Enter security group id : ")
				keyname = input("Enter Key name : ")

				output = sp.getstatusoutput("aws ec2 run-instances --image-id  {} --instance-type {} --count {}  --security-groups {} --key-name {}".format(image,instance,count,sgid,keyname))
			elif task == '6':
				size = input("Enter size of youe ebs volume : ")
				az = input("Enter availability-zone in which you want to create volume : ")
				ebsname = input("Enter a name which you want to give to your volume : ")
				output = sp.getstatusoutput("aws ec2 create-volume --volume-type gp2 --size {} --availability-zone {} --tag-specifications 'ResourceType=volume,Tags=['{'Key=name,Value= {}}]'".format(size,az,ebsname))
			elif task == '7':
				print("Before attaching EBS volume to an instance make sure your EBS volume and instance are in the same availability zone")
				instance = input("Enter instance-id to which you want to attach: ")
				volid = input("Enter volume-id which you want to attach : ")
				output = sp.getstatusoutput("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf".format(volid,instance))
			elif task == '8':
				bucketname = input("Enter bucket name : ")
				region = input("Enter region in which you want to create bucket : ")
				output = sp.getstatusoutput("aws s3 mb s3://{} --region {}".format(bucketname,region))
			elif task == '9':
				bucketname = input("Enter bucket name : ")
				output = sp.getstatusoutput("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com".format(bucketname))
			elif task == '10':
				output = sp.getstatusoutput("aws ec2 describe-instances")
			elif task == '11':
				output = sp.getstatusoutput("aws ec2 describe-key-pairs")
			elif task == '12':
				output = sp.getstatusoutput("aws ec2 describe-security-groups")
			elif task == '13':
				instance = input("Enter the instance id which you want to stop: ")
				output = sp.getstatusoutput("aws ec2 stop-instances --instance-ids {}".format(instance))

			elif task == '14':
				instance = input("Enter the instance id which you want to start: ")
				output = sp.getstatusoutput("aws ec2 start-instances --instance-ids {}".format(instance))
			elif task == '15':
				b_name = input("Enter bucket name: ")
				img_name = input("Enter image file name: ")
				permission = input("Enter permission you want to give eg.,public-read: ")
				ouput = sp.getstatusoutput("aws s3api put-object-acl --bucket {} --key {} --acl {}".format(b_name,img_name,permission))

			elif task == '16':
				img_path = input("Enter the complete path of the image you want to upload: ")
				b_name = input("Enter name of the bucket: ")
				output = sp.getstatusoutput("aws s3 sync \"{}\" s3\:\/\/{}\ ".format(img_path,b_name))

			elif task == '17':
				break;

			else:
				print("Invalid Option!!")
				os.system("sleep 1")
				continue

			if output[0] == 0:
				os.system("tput setaf 2")
				print("Task successfully completed !!")
				os.system("tput setaf 7")
				print(output[1])
			else:
				os.system("tput setaf 5")
				print("Oops !! Some error occurred : {}".format(output[1]))

			os.system("tput setaf 6")
			input("'Press enter' to continue :")
			os.system("tput setaf 7")

		else:
			#remote
			if task == '1':
				rc=os.system("{} 'aws configure'".format(ssh))
				if(rc == 0):
					output=(0,'Login Successful')

			elif task == '2':
				keyname = input("Enter Key name : ")
				output = sp.getstatusoutput("{} 'aws ec2 create-key-pair --key-name {}'".format(ssh,keyname))
			elif task == '3':
				grpname = input("Enter Security group name : ")
				description = input("Give Description of your security group : ")
				output = sp.getstatusoutput("{} 'aws ec2 create-security-group --group-name {} --description {} --vpc-id vpc-c62ecead'".format(ssh,grpname,description))
			elif task == '4':
				grpid = input("Enter groyp id : ")
				protocol = input("Enter protocol you want to add : ")
				port = input("Enter port number : ")
				output = sp.getstatusoutput("{} 'aws ec2 authorize-security-group-ingress --group-id {} --protocol {} --port {} --cidr 0.0.0.0/0'".format(ssh,grpid,protocol,port))
			elif task == '5':
				image = input("Enter image id : ")
				instance = input("Enter instance-type : ")
				count = input("Enter no.of instance you want to launch : ")
				sgid = input("Enter security group id : ")
				keyname = input("Enter Key name : ")

				output = sp.getstatusoutput("{} 'aws ec2 run-instances --image-id  {} --instance-type {} --count {}  --security-groups {} --key-name {}'".format(ssh,image,instance,count,sgid,keyname))
			elif task == '6':
				size = input("Enter size of youe ebs volume : ")
				az = input("Enter availability-zone in which you want to create volume : ")
				ebsname = input("Enter a name which you want to give to your volume : ")
				output = sp.getstatusoutput("{} 'aws ec2 create-volume --volume-type gp2 --size {} --availability-zone {} --tag-specifications \'ResourceType=volume,Tags=[\'{\'Key=name,Value= {}}]\''".format(ssh,size,az,ebsname))
			elif task == '7':
				print("Before attaching EBS volume to an instance make sure your EBS volume and instance are in the same availability zone")
				instance = input("Enter instance-id to which you want to attach: ")
				volid = input("Enter volume-id which you want to attach : ")
				output = sp.getstatusoutput("{} 'aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf'".format(ssh,volid,instance))
			elif task == '8':
				bucketname = input("Enter bucket name : ")
				region = input("Enter region in which you want to create bucket : ")
				output = sp.getstatusoutput("{} 'aws s3 mb s3://{} --region {}'".format(ssh,bucketname,region))
			elif task == '9':
				bucketname = input("Enter bucket name : ")
				output = sp.getstatusoutput("{} 'aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com'".format(ssh,bucketname))
			elif task == '10':
				output = sp.getstatusoutput("{} 'aws ec2 describe-instances'".format(ssh))
			elif task == '11':
				output = sp.getstatusoutput("{} 'aws ec2 describe-key-pairs'".format(ssh))
			elif task == '12':
				output = sp.getstatusoutput("{} 'aws ec2 describe-security-groups'".format(ssh))

			elif task == '13':
				instance = input("Enter the instance id which you want to stop: ")
				output = sp.getstatusoutput("{} 'aws ec2 stop-instances --instance-ids {}'".format(ssh,instance))

			elif task == '14':
				instance = input("Enter the instance id which you want to start: ")
				output = sp.getstatusoutput("{} 'aws ec2 start-instances --instance-ids {}'".format(ssh,instance))
			elif task == '15':
				b_name = input("Enter bucket name: ")
				img_name = input("Enter image file name: ")
				permission = input("Enter permission you want to give eg.,public-read: ")
				ouput = sp.getstatusoutput("{} 'aws s3api put-object-acl --bucket {} --key {} --acl {}'".format(ssh,b_name,img_name,permission))

			elif task == '16':
				img_path = input("Enter the complete path of the image you want to upload: ")
				b_name = input("Enter name of the bucket: ")
				output = sp.getstatusoutput("{} 'aws s3 sync \"{}\" s3\:\/\/{}\ '".format(ssh,img_path,b_name))
			elif task == '17':
				break;

			else:
				print("Invalid Option!!")
				os.system("sleep 1")
				continue

			if output[0] == 0:
				os.system("tput setaf 2")
				print("Task successfully completed !!")
				os.system("tput setaf 7")
				print(output[1])
			else:
				os.system("tput setaf 5")
				print("Oops !! Some error occurred : {}".format(output[1]))

			os.system("tput setaf 6")
			input("'Press enter' to continue :")
			os.system("tput setaf 7")





def docker(ssh):
	rc= sp.getstatusoutput("systemctl status docker")
	if(rc != 0):
		rc= sp.getstatusoutput("systemctl start docker")
	if(rc == 0):
		print("Docker running successfully!!")

	while True :

		os.system("clear")
		os.system("tput setaf 3")
		print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~ Welcome to our DOCKER menu ~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
		os.system("tput setaf 6")
		menu="""
		\t\tPress 1 :To install docker
		
		\t\tPress 2 :To download a docker image
		\t\tPress 3 :To see docker images available
		\t\tPress 4 :To launch a docker container
		\t\tPress 5 :To start a container\n
		\t\tPress 6 :To stop a container
		\t\tPress 7 :To attach to container
		\t\tPress 8 :To remove a docker container
		\t\tPress 9 :To remove all conatiners
		\t\tPress 10 :To see info of all running containers
		\t\tPress 11 :To see info of all existing containers
		\t\tPress 12 :To see logs of a container
		\t\tPress 13 :To see logs of all container
		\t\tPress 14 :To see all info about the container
		\t\tPress 15 :To search for docker images

		\t\tPress 16 :To go back to main menu or exit from this menu\n"""
		print(menu)
		os.system("tput setaf 7")
		task = input("Enter your choice : ")

		if ssh == {}:


			if(task == '1'):
				os.system("touch /etc/yum.repos.d/docker-ce.repo".format(ssh))
				output = sp.getstatusoutput("echo '[docker]\nbaseurl = https://download.docker.com/linux/centos/7/x86_64/stable/Packages/\ngpgcheck=0' > /etc/yum.repos.d/docker-ce.repo")
				if(output[0] == 0):
					output = sp.getstatusoutput("yum install docker-ce --nobest")
				os.system("docker info")

			elif(task == '2'):
				image = input("Enter docker image name : ")
				output = sp.getstatusoutput("docker pull {}".format(image))
			elif(task == '3'):
				output = sp.getstatusoutput("docker images")
			elif(task == '4'):
				image = input("Enter docker image name as (<image_name>:<version>) : ")
				cname = input("Enter container name : ")
				print("Enter 'exit' to exit container")
				rc = os.system("docker run -it --name {} {}".format(cname,image))
				if rc == 0:
					output = (0,"")
			elif(task == '5'):
				cname = input("Enter container name : ")
				output = sp.getstatusoutput("docker start {}".format(cname))
			elif(task == '6'):
				cname = input("Enter container name : ")
				output = sp.getstatusoutput("docker stop {}".format(cname))
			elif(task == '7'):
				cname = input("Enter container name : ")
				print("Enter 'exit' to exit container")
				rc = os.system("docker attach {}".format(cname))
				if rc == 0:
					output = (0,"")
			elif(task == '8'):
				cname = input("Enter container name : ")
				output = sp.getstatusoutput("docker rm {}".format(cname))
			elif(task == '9'):
				output = sp.getstatusoutput("docker rm -f `docker ps -a -q`")
			elif(task == '10'):
				output = sp.getstatusoutput("docker ps")
			elif(task == '11'):
				output = sp.getstatusoutput("docker ps -a")
			elif(task == '12'):
				cname = input("Enter container name : ")
				output = sp.getstatusoutput("docker logs {}".format(cname))
			elif(task == '13'):
				output = sp.getstatusoutput("docker logs")
			elif(task == '14'):
				cname = input("Enter container name : ")
				output = sp.getstatusoutput("docker inspect {}".format(cname))
			elif(task == '15'):
				image = input("Enter docker image name which you wanr to search: ")
				output = sp.getstatusoutput("docker search {}".format(image))

			elif task == '16':
				break;

			else:
				print("Invalid Option!!")
				os.system("sleep 1")
				continue

			if output[0] == 0:
				os.system("tput setaf 2")
				print("Task successfully completed !!")
				os.system("tput setaf 7")
				print(output[1])
			else:
				os.system("tput setaf 5")
				print("Oops !! Some error occurred : {}".format(output[1]))

			os.system("tput setaf 6")
			input("'Press enter' to continue :")
			os.system("tput setaf 7")

		else:

			if(task == '1'):
				os.system("{} 'touch /etc/yum.repos.d/docker-ce.repo'".format(ssh))
				output = sp.getstatusoutput("{} \'echo '[docker]\nbaseurl = https://download.docker.com/linux/centos/7/x86_64/stable/Packages/\ngpgcheck=0' > /etc/yum.repos.d/docker-ce.repo\'".format(ssh))
				if(output[0] == 0):
					output = sp.getstatusoutput("{} 'yum install docker-ce --nobest'".format(ssh))
				os.system("{} 'docker info'".format(ssh))

			elif(task == '2'):
				image = input("Enter docker image name : ")
				output = sp.getstatusoutput("{} 'docker pull {}'".format(ssh,image))
			elif(task == '3'):
				output = sp.getstatusoutput("{} 'docker images'".format(ssh))
			elif(task == '4'):
				image = input("Enter docker image name as (<image_name>:<version>) : ")
				cname = input("Enter container name : ")
				print("Enter 'exit' to exit container")
				rc = os.system("{} 'docker run -it --name {} {}'".format(ssh,cname,image))
				if rc == 0:
					output = (0,"")
			elif(task == '5'):
				cname = input("Enter container name : ")
				output = sp.getstatusoutput("{} 'docker start {}'".format(ssh,cname))
			elif(task == '6'):
				cname = input("Enter container name : ")
				output = sp.getstatusoutput("{} 'docker stop {}'".format(ssh,cname))
			elif(task == '7'):
				cname = input("Enter container name : ")
				print("Enter 'exit' to exit container")
				rc = os.system("{} 'docker attach {}'".format(ssh,cname))
				if rc == 0:
					output = (0,"")
			elif(task == '8'):
				cname = input("Enter container name : ")
				output = sp.getstatusoutput("{} 'docker rm {}'".format(ssh,cname))
			elif(task == '9'):
				output = sp.getstatusoutput("{} 'docker rm -f `docker ps -a -q`'".format(ssh))
			elif(task == '10'):
				output = sp.getstatusoutput("{} docker ps".format(ssh))
			elif(task == '11'):
				output = sp.getstatusoutput("{} 'docker ps -a'".format(ssh))
			elif(task == '12'):
				cname = input("Enter container name : ")
				output = sp.getstatusoutput("{} 'docker logs {}'".format(ssh,cname))
			elif(task == '13'):
				output = sp.getstatusoutput("{} 'docker logs'".format(ssh))
			elif(task == '14'):
				cname = input("Enter container name : ")
				output = sp.getstatusoutput("{} 'docker inspect {}'".format(ssh,cname))
			elif(task == '15'):
				image = input("Enter docker image name which you wanr to search: ")
				output = sp.getstatusoutput("{} 'docker search {}'".format(ssh,image))

			elif task == '16':
				break;

			else:
				print("Invalid Option!!")
				os.system("sleep 1")
				continue

			if output[0] == 0:
				os.system("tput setaf 2")
				print("Task successfully completed !!")
				os.system("tput setaf 7")
				print(output[1])
			else:
				os.system("tput setaf 5")
				print("Oops !! Some error occurred : {}".format(output[1]))

			os.system("tput setaf 6")
			input("'Press enter' to continue :")
			os.system("tput setaf 7")


		


def server(ssh):

	while True:

		os.system("clear")
		os.system("tput setaf 3")
		print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~ Welcome to our Server menu ~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
		print("Before Configuring webserver, configure yum once if not configured : Press 5")
		os.system("tput setaf 6")

		mainmenu="""
		\t\tPress 1 : Configure Apache Web Server on linux
		\t\tPress 2 : Start Apache Web Server on linux
		\t\tPress 3 : Host webpage Apache Web Server
		\t\tPress 4 : Configure yum repository
		\t\tPress 5:To go back to main menu or exit from this menu\n"""
		print(mainmenu)

		os.system("tput setaf 7")
		task = input("Enter your choice : ")

	

		if ssh =="":
			#local sys
			if task == '1':

				print("Installing httpd software... Be patient!!")
				rc = os.system("yum install httpd")
				if(rc == 0):
					webpage = input("Enter webpage file path  which you want to host: ")
					os.system("cp {} /var/www/html".format(webpage))
				output = sp.getstatusoutput("systemctl start httpd")

			elif task == '2':
				output = sp.getstatusoutput("systemctl start httpd")
				output = sp.getstatusoutput("systemctl status httpd")

			elif task == '3':
				webpage = input("Enter webpage file path  which you want to host: ")
				os.system("cp {} /var/www/html".format(webpage))
				ouput = (0, "WEBPAGE hosted!!!")

			elif task == '4':
				print("Configuring yum. please Wait!!!")
				output = sp.getstatusoutput("yum install --nogpgcheck https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")
				os.system(" yum repolist")


			elif task == '5':
				break;

			else:
				print("Invalid Option!!")
				os.system("sleep 1")
				continue

			if output[0] == 0:
					os.system("tput setaf 2")
					print("Task successfully completed !!")
					print("Web Server configured!! Services started successfully !!! ")
					os.system("tput setaf 7")
					print(output[1])
			else:
				os.system("tput setaf 5")
				print("Oops !! Some error occurred : {}".format(output[1]))

			os.system("tput setaf 6")
			input("'Press enter' to continue :")
			os.system("tput setaf 7")

		else:
			#remote sys
			if task == '1':

				print("Installing httpd software... Be patient!!")
				rc = os.system("{} 'yum install httpd'".format(ssh))
				print("Installing httpd software... Be patient!!")
				if(rc== 0):
					webpage = input("Enter webpage file path  which you want to host: ")
					os.system("{} 'cp {} /var/www/html'".format(ssh,webpage))
				output = sp.getstatusoutput("{} 'systemctl start httpd'".format(ssh))

			elif task == '2':
				output = sp.getstatusoutput("{} systemctl start httpd".format(ssh))
				output = sp.getstatusoutput("{} systemctl status httpd".format(ssh))

			elif task == '3':
				webpage = input("Enter webpage file path  which you want to host: ")
				os.system("{} 'cp {} /var/www/html'".format(ssh,webpage))
				ouput = (0, "WEBPAGE hosted!!!")

			elif task == '4':
				print("Configuring yum. please Wait!!!")
				output = sp.getstatusoutput("{} 'yum install --nogpgcheck https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm'".format(ssh))
				os.system("{} 'yum repolist'".format(ssh))


			elif task == '5':
				break;

			else:
				print("Invalid Option!!")
				os.system("sleep 1")
				continue

			if output[0] == 0:
					os.system("tput setaf 2")
					print("Task successfully completed !!")
					print("Web Server configured!! Services started successfully !!! ")
					os.system("tput setaf 7")
					print(output[1])
			else:
				os.system("tput setaf 5")
				print("Oops !! Some error occurred : {}".format(output[1]))

			os.system("tput setaf 6")
			input("'Press enter' to continue :")
			os.system("tput setaf 7")
				



def main():

	print("Hello !! ENTER PASSWORD TO ACCESS MENU : ")

	passwd = gp.getpass()
	if(passwd != '18205'):
		print("Wrong Password !! Better luck next time")
		exit()

	sys = input("Where do you want to run this [local] / [remote] system?")
	ssh=""
	ip=""
	user=""
	if(sys == 'remote'):
			ip = input("Enter remote system IP : ")
			user = input("Enter remote system user name :")
			ssh="ssh {}@{} ".format(user,ip)

	while True:

		os.system("clear")
		os.system("tput setaf 3")
		print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~ Welcome to our main menu ~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
		os.system("tput setaf 6")

		

		

		mainmenu="""
		\t\tPress 1 : Linux Basic Operations
		\t\tPress 2 : Static Partitions
		\t\tPress 3 : Logical Volume Management
		\t\tPress 4 : Hadoop Operations
		\t\tPress 5 : AWS Operations
		\t\tPress 6 : Docker Operations
		\t\tPress 7 : Configure Server
		\t\tPress 8 : Exit\n"""
		print(mainmenu)

		os.system("tput setaf 7")
		task = input("\t\t\tChoose the area in which you want to do Task : ")

		if(task == '1'):
			linuxbasic(ssh)

		elif(task == '2'):
			staticpartitions(ssh)

		elif(task =='3'):
			lvm(ssh)

		elif(task == '4'):
			hadoop(ssh,user,ip)

		elif(task == '5'):
			aws(ssh)

		elif(task == '6'):
			docker(ssh)
		elif(task == '7'):
			server(ssh)
		elif(task == '8'):
			exit()
		else:
			print("Invalid Option!!")
			os.system("sleep 1")
			continue



if __name__=="__main__": 
    main() 
	

