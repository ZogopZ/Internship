#!/bin/bash
source /home/zois/Documents/classified/Utilities/tools # Include tools in this file. Absolute path to tools.


ttyCurrent=$(tty)
echo -e "${UserDim}User       |${User} Spamming mails using python...${ColorOff}"
echo $(python3 /home/zois/Documents/classified/Utilities/assets/spamMail/SoManyToday.py > $ttyCurrent)
