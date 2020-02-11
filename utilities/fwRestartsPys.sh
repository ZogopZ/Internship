#!/bin/bash
source /home/zois/Documents/Internship/utilities/tools # Include tools in this file. Absolute path to tools.

ssh $remote systemctl restart flask.service
