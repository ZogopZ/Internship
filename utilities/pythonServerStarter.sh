#!/bin/bash
source /root/tools # Include tools in this file. Absolute path to tools.


function flaskApp()
{
        export FLASK_APP=/root/python/pythonServer.py
        export FLASK_DEBUG=0
        flask run --port=5000
}


re='^[0-9]+$'
pythonServerPid=$(pgrep -f "/opt/rh/rh-python36/root/usr/bin/python3 /opt/rh/rh-python36/root/usr/bin/flask run --port=5000")
if [ -z "$pythonServerPid" ]; then
	echo -e "${UserDim}User       |${User} Starting python server...${ColorOff}"
	flaskApp
elif [[ $pythonServerPid =~ $re ]]; then
	echo -e "${WarningDim}Warning    |${Warning} Python server with pid:${pythonServerPid} is already running on port 5000...${ColorOff}"
        echo -e "${UserDim}User       |${User} Killing application with pid $pythonServerPid on port 5000...${ColorOff}"
	fuser -k 5000/tcp > /dev/null 2>&1
	echo -e "${UserDim}User       |${User} Starting python server...${ColorOff}"
	flaskApp
fi
