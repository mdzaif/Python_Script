#!/bin/bash
# install python virtualenv

#Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
RESET='\033[0m'


echo "Check virtual environment setup...."
sleep 2
if [[ $(virtualenv --version &> /dev/null) -eq 0 ]]; then
    echo -e "${GREEN} Already Installed ${RESET}"
else
    sudo apt update && sudo apt install python3-virtualenv

    if [[ $(virtualenv --version &> /dev/null) -eq 0 ]]; then
        echo -e "${GREEN} Installed ${RESET}"
    else
        echo -e "${RED} Something else! not installed ${RESET}"
        echo -e "${YELLOW} Stop install.sh ${RESET}"
        return 1
    fi
fi
echo "Check the virtualenv vironment setup..."
sleep 2

# setup virtualenv
read -p "Do you want to setup virtual envirotment for this directory[y/n]: " input

case $input in

[yY]* )
    echo "No virtual environment..."
    echo "Creating virtual environment...."
    sleep 2
    virtualenv -p /usr/bin/python3 venv

    if [[ -d "venv" ]]; then
        echo -e "${GREEN} Virtual environment directory:venv created! ${RESET}"
    else
        echo -e "${RED} Virtualenv faild to create venv directory! ${RESET}"
    fi
    ;;

[nN]* )
    echo -e "${YELLOW} Abort ${RESET}"
    ;;
*)
    echo -e "${RED}Invalid input. Please enter y/n.{$RESET}"
    ;;
esac

read -p "Do you want to activate the virtual environment(prefer to no if there already exixsted your own virtual enviroment[y/n]: " per

case $per in

[yY]* )
    source venv/bin/activate
    echo -e "${GREEN} Activated ${RESET}"
    ;;

[nN]* )
    echo -e "${YELLOW} Abort ${RESET}"
    ;;
*)
    echo -e "${RED}Invalid input. Please enter y/n.{$RESET}"
    ;;

esac

#install requirement.txt

read -p "Do you want to install required python libraries[y/n](not prefer if your not activate virtual environment): " rq

case $rq in

[yY]* )
    pip3 install -r requirement.txt

    if [ $? -eq 0]; then
        echo -e "${GREEN} Completed ${RESET}"
    else
        echo -e "${RED} Installation faild, try again ${RESET}"
    fi
    ;;
[nN]* )
    echo -e "${YELLOW} Abort ${RESET}"
    ;;
*)
    echo -e "${RED}Invalid input. Please enter y/n.{$RESET}"
    ;;
esac

if [ $? -eq 0 ]; then
    echo -e "${GREEN} You are Done! ${RESET}"
    echo -e "${YELLOW} Final tip: Check README.md to set the PYTHONPATH Variable! ${RESET}"
else
    echo -e "${RED}Something missed! try later.{$RESET}"
fi
