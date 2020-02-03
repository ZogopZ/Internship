#!/bin/bash
source /home/zois/Documents/Internship/utilities/tools  # Include tools in this file. Absolute path to tools.


user="$(sudo users)"
# Welcome message.
# Start (Do not edit this line!!!)
echo -e "[2;90mInit       |[0;90m Good morning to you too! Let's start, shall we?[0m"
echo -e "[2;90mInit       |[0;90m                    |************************************************************************************|[0m"
echo -e "[2;90mInit       |[0;90m Message of the day:|*** Keep fixing try-except statements. Maybe work on dynamically reporting workf ***|[0m"
echo -e "[2;90mInit       |[0;90m                    |*** low.                                                                         ***|[0m"
echo -e "[2;90mInit       |[0;90m                    |************************************************************************************|[0m"
# End (Do not edit this line!!!)


# Flag -m existence.
if [[ $1 == "-m" ]]; then
	ttyCurrent=$(tty)
	echo -e "${UserDim}User       |${User} Starting mail spammer...${ColorOff}"
	echo $("$pSpam" > /dev/pts/0 2>&1)
fi


# Check for mounted redmine directory and mount it if necessary.
echo -e "${UserDim}User       |${User} Redmine mount:${ColorOff}"
redmineChoice="invalid"
findRedmineMount=$(mount -l | grep -oe "root@10.10.111.77:/var/www/html/redmine/ on /home/zois/Documents/Redmine_on-server type fuse.sshfs")
if [ -z "$findRedmineMount" ]; then
	echo -e "${WarningDim}Warning!   |${Warning}  -Remote Redmine file system was not found locally."
	while [ $redmineChoice = "invalid" ]
	do
		read -p "$(echo -e "${UserDim}User       |${User}  -Would you like to mount it automatically (y/n)?${ColorOff}")" redmineChoice
		case "$redmineChoice" in
			y|Y)
				echo -e "${UserDim}User       |${User}  -Mounting remote CentOS Redmine directory locally...${ColorOff}"
				sudo -u ${user} sshfs ${remote}:/var/www/html/redmine/ /home/zois/Documents/Redmine_on-server
				;;
			n|N)
				;;
		 	*)
				redmineChoice="invalid"
				echo -e "${UserDim}User       |${User}  -Invalid selection. Please type y or n to continue...${ColorOff}"
				;;
		esac
	done
elif [ "$findRedmineMount" == "root@10.10.111.77:/var/www/html/redmine/ on /home/zois/Documents/Redmine_on-server type fuse.sshfs" ]; then
	echo -e "${UserDim}User       |${User}  -Remote CentOs Redmine directory is already mounted locally...${ColorOff}"
fi
sectionEnd


# Check for mounted python directory and mount it if necessary.
echo -e "${UserDim}User       |${User} Python mount:${ColorOff}"
pythonChoice="invalid"
findPythonMount=$(mount -l | grep -oe "root@10.10.111.77:/root/python/ on /home/zois/Documents/Python_on-server type fuse.sshfs")
if [ -z "$findPythonMount" ]; then
	echo -e "${WarningDim}Warning!   |${Warning}  -Remote Python file system was not found locally."
	while [ $pythonChoice = "invalid" ]
	do
		read -p "$(echo -e "${UserDim}User       |${User}  -Would you like to mount it automatically (y/n)?${ColorOff}")" pythonChoice
		case "$pythonChoice" in
			y|Y)
				echo -e "${UserDim}User       |${User}  -Mounting remote CentOS Python directory locally...${ColorOff}"
				sudo -u ${user} sshfs ${remote}:/root/python/ /home/zois/Documents/Python_on-server
				;;
			n|N)
				;;
			*)
				pythonChoice="invalid"
				echo -e "${UserDim}User       |${User}  -Invalid selection. Please type y or n to continue...${ColorOff}"
				;;
		esac
	done
elif [ "$findPythonMount" == "root@10.10.111.77:/root/python/ on /home/zois/Documents/Python_on-server type fuse.sshfs" ]; then
	echo -e "${UserDim}User       |${User}  -Remote CentOs Python directory is already mounted locally...${ColorOff}"
fi
sectionEnd


# Check for postgreSQL backup directory and create it if it doesn't exist.
# Give required permissions to user.
echo -e "${BackupDim}Back-up    |${Backup} Backing up postgreSQL database..."
echo -e "${BackupDim}Back-up    |${Backup}  -Checking if backup directory for postgreSQL exists"
dbDir="/home/$user/Documents/postgreSQL-backup"
if [ -d "$dbDir" ]; then
	echo -e "${BackupDim}Back-up    |${Backup}  -Directory '${dbDir}' exists!"
else
	echo -e "${CyanDim}Warning!   |${Cyan}  -Directory '${dbDir}' does not exist..."
	echo -e "${BackupDim}Back-up    |${Backup}  -Creating directory '${dbDir}'." & sleep 1
	mkdir ${dbDir}
	echo -e "${BackupDim}Back-up    |${Backup}  -Adding permissions for user:${user}"
	sudo chown -R ${user}:${user} ${dbDir}
fi


# Generate postgreSQL backup file and dump remote database in it.
read -p "$(echo -e "${UserDim}User       |${User}  -Please attach a label to the sql backup file...${ColorOff}")" label
echo -e "${BackupDim}Back-up    |${Backup}  -Creating backup file..."
backupFile="postgre-(${label})--$(date +"%Y-%m-%d(%T)").sql"
backupFileFullPath="${dbDir}/${backupFile}"
touch ${backupFileFullPath}
echo -e "${BackupDim}Back-up    |${Backup}  -Dumping remote database to '${dbDir}${backupFile}'${ColorOff}"
printf "${UserDim}User       |${User}  -" && ssh -t $remote "pg_dump -U redmine -h localhost -C --column-inserts" \ >> ${backupFileFullPath} && printf "${ColorOff}"
echo -e "${BackupDim}Back-up    |${UserBold} ---Success---"
sectionEnd


# Today todos.
/home/zois/Documents/Internship/utilities/todo -p
/home/zois/Documents/Internship/utilities/todo -c
