#!/bin/bash
source /home/zois/Documents/classified/Utilities/tools  # Include tools in this file. Absolute path to tools.


scp $pTools $remote:
scp $pPys $remote:
ssh $remote ./pythonServerStarter.sh
wait
ssh $remote rm tools
ssh $remote rm pythonServerStarter.sh
