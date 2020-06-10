#!/bin/bash
source /home/zois/Documents/Internship/utilities/tools # Include tools in this file. Absolute path to tools.


function  displayTodo()
{
	if [[ $todoType == "personal" ]]; then # Displays the oldest personal todo to the user.
		label=$(grep personal $ptfPersonal | awk '{print $2}' | sort -n  | awk 'NR==1{print $1}') && label="${label}$" # grep all personal labels and select the one with the smallest issue number.
		label="personal ${label}" # Prepend "personal " to label, to correctly grep the issue.
		echo > $ttyCurrent 2>&1
		grep -A3 "$label" $ptfPersonal > $ttyCurrent 2>&1 # Find the labeled issue and grep it with the three lines below. Each issue consists of four lines.
		echo > $ttyCurrent 2>&1
	elif [[ $todoType == "company" ]]; then # Displays the oldest company todo to the user.
		label=$(grep company $ptfCompany | awk '{print $2}' | sort -n  | awk 'NR==1{print $1}') && label="${label}$"
		label="company ${label}" # Prepend "company " to label, to correctly grep the issue.
		echo > $ttyCurrent 2>&1
		grep -A3 "$label" $ptfCompany > $ttyCurrent 2>&1 # Find the labeled issue and grep it with the three lines below. Each issue consists of four lines.
		echo > $ttyCurrent 2>&1
	fi
	if [[ $label == "personal $" ]] || [[ $label == "company $" ]]; then # Could not grep anything from todo files, because there are no issues left.
		echo -e "${UserDim}User       |${User}   Nothing to do for $todoType...${ColorOff}" > $ttyCurrent 2>&1 # No personal or company todos found.
	fi
}


function completeTodo()
{
	label="$todoType"" ""$labelNo"
        ptfTemp="$ptdTodos""completingTodos.tmp"
        ptfToEdit="$ptdTodos""$todoType"
	ptfToAppend="$ptdTodos""completed""${todoType^}"
	grep -A3 "$label" $ptfToEdit >> $ptfToAppend && echo >> $ptfToAppend
	awk "/$label/{getline;getline;getline;getline;next} 1" $ptfToEdit > $ptfTemp
        cp $ptfTemp $ptfToEdit
        rm $ptfTemp
	echo -e "${UserDim}User       |${User}    -Dummy succefully completed.${ColorOff}" # TODO
}

function newTodo()
{
	echo -e "${UserDim}User       |${User}   Adding new ${Underline}${todoType}${ColorOff}${User} todo with ${Underline}${todoCriticality}${ColorOff}${User} criticality.${ColorOff}"
	date=$(date "+%d-%m-%Y")
	pathToPersonal="/home/zois/Documents/Internship/utilities/todos/personal"
	pathToCompany="/home/zois/Documents/Internship/utilities/todos/company"
	pathToTemp="/home/zois/Documents/Internship/utilities/todos/tempTodos.tmp"
	read -ep "$(echo -e "${UserDim}User       |${User}    -Please add todo text:${ColorOff}")" todoText
	read -ep "$(echo -e "${UserDim}User       |${User}    -Please add current functionality:${ColorOff}")" currentFunc
	if [ $todoType == "company" ]; then
		increasingNumber=$(($(grep -e "^# Current" $pathToCompany | grep -Eo [0-9]+)+1))
		label="company $increasingNumber"
		todoCriticality="\\[${todoCriticality}]\\" # Add [] characters to criticality. This is done in order to differentiate between LOW, VERY-LOW and HIGH, VERY-HIGH. The [] characters need escaping when using sed.
		sed "s/\(""${todoCriticality}"":\)\(.*\)/\1\n\n""${label}""\n""${todoCriticality}"" ->\tto-do:\t\t""${todoText}""\n(""${date}"")\tcurrent:\t""$currentFunc""\n""$(printf "_%0.s" {1..160})""\2/" $pathToCompany > $pathToTemp
		cp $pathToTemp $pathToCompany
		sed "s/\(# Current \)\([0-9]*$\)/\1${increasingNumber}/" $pathToCompany > $pathToTemp
		cp $pathToTemp $pathToCompany
		cat $pathToCompany
	elif [ $todoType == "personal" ]; then
		increasingNumber=$(($(grep -e "^# Current" $pathToPersonal | grep -Eo [0-9]+)+1))
		label="personal $increasingNumber"
		todoCriticality="\\[${todoCriticality}]\\" # Add [] characters to criticality. This is done in order to differentiate between LOW, VERY-LOW and HIGH, VERY-HIGH. The [] characters need escaping when using sed.
		sed "s/\(""${todoCriticality}"":\)\(.*\)/\1\n\n""${label}""\n""${todoCriticality}"" ->\tto-do:\t\t""${todoText}""\n(""${date}"")\tcurrent:\t""$currentFunc""\n""$(printf "_%0.s" {1..160})""\2/" $pathToPersonal > $pathToTemp
		cp $pathToTemp $pathToPersonal
		sed "s/\(# Current \)\([0-9]*$\)/\1${increasingNumber}/" $pathToPersonal > $pathToTemp
		cp $pathToTemp $pathToPersonal
		cat $pathToPersonal
	fi
	rm $pathToTemp
	echo -e "${UserDim}User       |${User}    -Dummy succefully added.${ColorOff}" # TODO
}

function removeTodo()
{
	label="$todoType"" ""$labelNo"
	ptfTemp="$ptdTodos""removingTodos.tmp"
	ptfToEdit="$ptdTodos""$todoType"
	awk "/$label/{getline;getline;getline;getline;next} 1" $ptfToEdit > $ptfTemp
	cp $ptfTemp $ptfToEdit
	rm $ptfTemp
}
