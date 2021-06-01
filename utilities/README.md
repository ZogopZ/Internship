# This directory contains multiple utilities for linux, written in bash.

- ### to-do list
files([todo](https://github.com/ZogopZ/Internship/blob/master/utilities/todo), [edit-todo](https://github.com/ZogopZ/Internship/blob/master/utilities/edit-todo), [todo-functions](https://github.com/ZogopZ/Internship/blob/master/utilities/todo-functions), [bash_completion.sh](https://github.com/ZogopZ/Internship/blob/master/utilities/bash_completion.sh))
A batch of scripts that when used together implement a todo list and can add, remove or edit a list of things todo using the terminal.

- ### aliases
files([aliases](https://github.com/ZogopZ/Internship/blob/master/utilities/aliases))
An easy way to add, remove or edit existing aliases within Linux.

- ### day message
files([good-morning.sh](https://github.com/ZogopZ/Internship/blob/master/utilities/good-morning.sh), [edit-day-message](https://github.com/ZogopZ/Internship/blob/master/utilities/edit-day-message))
A batch of scripts that plays a good morning message and performs important operations from the remote server onto the local machine. It also automatically backs up the database of the remote machine.<br>*Example usage: `./good-morning.sh`*

- ### Redmine updater
files([updater](https://github.com/ZogopZ/Internship/blob/master/utilities/updater), [update-redmine](https://github.com/ZogopZ/Internship/blob/master/utilities/update-redmine)) Checks for updates of Redmine and applies it to the remote machine.

- ### Other
  #### 1. adjust-brightness
  files([adjust-brightness](https://github.com/ZogopZ/Internship/blob/master/utilities/adjust-brightness))
  Since the functions keys on the keyboard do not work correctly, this is a simple implementation to adjust the laptop's brightness using the terminal. The script gets numbers 0-9 as input.<br>*Example usage: `/adjust_brightness 3`*
  #### 2. restart flask service
   files([fwRestartsPys.sh](https://github.com/ZogopZ/Internship/blob/master/utilities/fwRestartsPys.sh)) Restarts the flask service on the remote machine.
  #### 3. start python server
   files([start-remote-python-server.sh](https://github.com/ZogopZ/Internship/blob/master/utilities/start-remote-python-server.sh)) Starts the python server on the remote machine.
  #### 4. python-server-starter
   files([pythonServerStarter.sh](https://github.com/ZogopZ/Internship/blob/master/utilities/pythonServerStarter.sh)) Starts the python server on the local machine.
  #### 5. toggle-touchpad
   files([toggle-touchpad](https://github.com/ZogopZ/Internship/blob/master/utilities/toggle-touchpad)) Toggles the touchpad of the laptop on and off.<br>*Example usage: `/toggle-touchpad`*
  #### 6. tools
   files([tools](https://github.com/ZogopZ/Internship/blob/master/utilities/tools)) A helper script to provide file locations, color modes and trusted keys.
