#!/bin/bash
source /home/zois/Documents/Internship/utilities/tools # Include tools in this file. Absolute path to tools.
source $ptfTodoFunctions

ttyCurrent=$(tty)
while [ $# -gt 0 ] ; do
	case $1 in
		-n | --new-todo) todoFunction="new" optionsArray+=("$1") functionIndex=$((${#optionsArray[@]}-1)) ;;
		-r | --remove-todo) todoFunction="remove" optionsArray+=("$1") functionIndex=$((${#optionsArray[@]}-1)) ;;
		-C | --complete-todo) todoFunction="complete" optionsArray+=("$1") functionIndex=$((${#optionsArray[@]}-1)) ;;

		-p | --personal) todoType="personal" optionsArray+=("$1") typeIndex=$((${#optionsArray[@]}-1)) ;;
		-c | --company) todoType="company" optionsArray+=("$1") typeIndex=$((${#optionsArray[@]}-1)) ;;

		-vh | --very-high) optionsArray+=("$1") todoCriticality="VERY-HIGH" criticalityIndex=$((${#optionsArray[@]}-1)) ;;
		-h | --high) optionsArray+=("$1") todoCriticality="HIGH" criticalityIndex=$((${#optionsArray[@]}-1)) ;;
		-m | --medium) optionsArray+=("$1") todoCriticality="MEDIUM" criticalityIndex=$((${#optionsArray[@]}-1)) ;;
		-l | --low) optionsArray+=("$1") todoCriticality="LOW" criticalityIndex=$((${#optionsArray[@]}-1)) ;;
		-vl | --very-low) optionsArray+=("$1") todoCriticality="VERY-LOW" criticalityIndex=$((${#optionsArray[@]}-1)) ;;

		*) optionsArray+=("$1") labelNoIndex=$((${#optionsArray[@]}-1)) re='^[0-9]+$' ;;
	esac
	shift
done

if [[ ${#optionsArray[@]} == 1 ]]; then  # Display a todo.
        if [[ ${optionsArray[0]} == "-p" || ${optionsArray[0]} == "--personal" ]] || [[ ${optionsArray[0]} == "-c" || ${optionsArray[0]} == "--company" ]]; then
		displayTodo
	else
		echo -e "${Error}Error      | Invalid parameters...${DefaultBd}${ColorOff}"
        fi
elif [[ ${#optionsArray[@]} == 2 ]]; then  # Complete a todo.
        if [[ "${optionsArray[@]}" =~ "-p" || "${optionsArray[@]}" =~ "--personal" ]] && [[ "${optionsArray[@]}" =~ "C" || "${optionsArray[@]}" =~ "--complete-todo" ]]; then
		echo "Completes personal todo"
                todoType="personal"
        elif [[ "${optionsArray[@]}" =~ "-c" || "${optionsArray[@]}" =~ "--company" ]] && [[ "${optionsArray[@]}" =~ "C" || "${optionsArray[@]}" =~ "--complete-todo" ]]; then
		echo "Completes company todo"
                todoType="company"
	fi
elif [[ ${#optionsArray[@]} == 3 ]]; then
	if [[ "${optionsArray[@]}" =~ "-p" || "${optionsArray[@]}" =~ "--personal" ]] || [[ "${optionsArray[@]}" =~ "c" || "${optionsArray[@]}" =~ "--company" ]]; then
		unset 'optionsArray[typeIndex]'
		if [[ "${optionsArray[@]}" =~ "-vh" || "${optionsArray[@]}" =~ "--very-high" ]] || [[ "${optionsArray[@]}" =~ "-h" || "${optionsArray[@]}" =~ "--high" ]] || 
           	   [[ "${optionsArray[@]}" =~ "-m" || "${optionsArray[@]}" =~ "--medium" ]] || [[ "${optionsArray[@]}" =~ "-l" || "${optionsArray[@]}" =~ "--low" ]] ||
		   [[ "${optionsArray[@]}" =~ "-vl" || "${optionsArray[@]}" =~ "--very-low" ]]; then
			unset 'optionsArray[criticalityIndex]'
			if [[ "${optionsArray[@]}" =~ "-n" || "${optionsArray[@]}" =~ "--new-todo" ]]; then
				newTodo
			elif [[ "${optionsArray[@]}" =~ "-C" || "${optionsArray[@]}" =~ "--complete-todo" ]]; then
				completeTodo
			else
				echo -e "${Error}Error      | Invalid parameters...${DefaultBd}${ColorOff}"
			fi
		elif [[ "${optionsArray[@]}" =~ "-r" || "${optionsArray[@]}" =~ "--remove" ]] && [[ "${optionsArray[labelNoIndex]}" =~ $re ]]; then
			labelNo="${optionsArray[labelNoIndex]}"
                	removeTodo
		elif [[ "${optionsArray[@]}" =~ "-C" || "${optionsArray[@]}" =~ "--complete-todo" ]] && [[ "${optionsArray[labelNoIndex]}" =~ $re ]]; then
                        labelNo="${optionsArray[labelNoIndex]}"
                        completeTodo
		else
			echo -e "${Error}Error      | Invalid parameters...${DefaultBd}${ColorOff}"
		fi
	else
		echo -e "${Error}Error      | Invalid parameters...${DefaultBd}${ColorOff}"
	fi
fi
