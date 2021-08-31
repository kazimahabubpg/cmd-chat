#!/usr/bin/bash
installPython(){
  echo "This script requires python, that is not installed on the system.
    Installing python..."
  sleep 1
  pkg install python > /dev/null 2>&1
}
banner(){
  printf "\n\e[0m\e[1;92m
  =================================================\n
  ======            ================================\n
  =====     ====     ===============================\n
  =====     ====     ===============================\n
  ======        =======    ===    ==           =====\n
  ========        =====    ===    ==    ===    =====\n
  ==========        ===    ===    ==    ===    =====\n
  =====     ====     ==    ===    ==    ===    =====\n
  =====     ====     ==    ===    ==    ===    =====\n
  ======            ====          ==    ===    =====\n
  ==================================================\n
  ==================================================\n\n
  \e[0m"
}
throwNgrok(){
  printf "Ngrok isn't installed. Please install it first, from \e[0m\e[1;93mhttps://ngrok.com"
}
menu(){
  printf "\e[1;31m[\e[0m\e[1;77m0\e[0m\e[1;31m]\e[0m\e[1;93m Host\n"
  printf "\e[1;31m[\e[0m\e[1;77m1\e[0m\e[1;31m]\e[0m\e[1;93m Join\033[0;37;40m\n"
}
host(){
  printf "\n\n\033[1;36;40mStarting Server..."
  ~/ngrok tcp 5000 > /dev/null 2>&1 &
  python server.py > /dev/null 2>&1 &
  sleep 7
  clear
  
  link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "tcp://[0-9]*\.tcp.ngrok.io:[0-9]*")
  printf "\033[1;33;40mSend the link to anyone you want to chat with:\n\033[1;36;40m$link\033[0;37;40m\n\n"
  python user.py 127.0.0.1:5000
}
join(){
  clear
  python user.py
}

command -v python > /dev/null 2>&1 || installPython
killall -2 python > /dev/null 2>&1
killall -2 ngrok > /dev/null 2>&1

clear
banner
printf "\n \e[1;31m[\e[0m\e[1;77m~\e[0m\e[1;31m]\e[0m\e[1;93m Please turn on device hotspot, otherwise you won't get the link. \033[0;37;40m\n\n"

sleep 1

menu
read -p "Select an option: " option

if [[ $option == 0 ]]; then
host
elif [[ $option == 1 ]]; th
join
fi
