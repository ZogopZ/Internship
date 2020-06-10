#!/bin/bash
source /home/zois/Documents/Internship/utilities/tools # Include tools in this file. Absolute path to tools.


ttyCurrent=$(tty)
echo -e "${UserDim}User       |${User} Spamming mails using python...${ColorOff}"
echo $(python3 /home/zois/Documents/Internship/utilities/assets/spamMail/so_many_today.py > $ttyCurrent)
