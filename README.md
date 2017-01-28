# Capture
An automated script for establishing a connection to the internet on the Raspberry Pi running Kali Linux.


This script is best used as an autostart script so that if there is no connection, it will start working without any user interaction.

Support for it to prefer access points with clients attached. Set this at the top of the file by changing the "onlywithclients" variable to 1.

It will attempt to crack any handshake with all dictionaries in /root/Documents/dictionaries/ in alphabetical order

This requires crunch if you want it to also try phone numbers. 

This requires an external wireless card that can go into monitoring mode. Unless you change it, this script will always use wlan1.

Install with: git clone https://github.com/rapidwolf95/capture
Run with: bash capture
