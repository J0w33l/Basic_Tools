#!/bin/bash

#allinter=$(ip a | grep inet\b | awk {'print $2'} | cut -f1)  
interfaces=$(ip link show | grep -E ': lo|: eth|: wlan|: tun|: ens'  |awk '{print $2}' | cut -d/ -f1)

echo $interfaces

echo "Please write the interface ip that you want"
read inter

ask=$(ip a show $inter  | grep "inet\b" |awk '{print $2}' | cut -d/ -f1)


echo the ip of that interface is $ask 
