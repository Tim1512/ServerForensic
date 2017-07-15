# ServerForensic

This repo includes some scripts for analysing and secure debian-based servers (like Ubuntu). For a short summary, look up to the code of the scripts in the first few lines. I hope it can help you anyway, if there are any issues or problems in the translation let me know it so I can do my best.
The software is licensed under GPL v3, so you are free to modify and publish the code as long as you redistribute under the same terms and same license. I will be happy if I see you credit me, but it's your choice. :)

All scripts had been tested on Ubuntu 16.04 LTS.

Deescription and manual for the scripts:



  authlog_structurizer.py:
    
    The authlog_structurizer is made to structurize the auth.log file of linux. In this file, Debian, Ubuntu and equal distributions writes the accesses and access tries to your system and all actions that handels with getting root permissions or managing users. The script removes unimportant lines and sort the lines into diffrent sections. It gives you an overview if their are too many accesses to your server, if their are more sessions than you can remember; it shows you on which users there are attacks, so you can maybe block them if they exist; and some kind of more or less mostly unnecessary stuff. If something looks suspicious to you, check it.
    
    1. You need Python3.5 or later to run the script. If it is not already installed:
    
          sudo apt install python3.5
          
    2. You need the auth.log from your server (the path is /var/logs/auth.log) and the authlog_structurizer.py in the same directory 
    (It is equal if you have both on the server or on your PC, just remember that you maybe have to change the read permissions of your auth.log if you use it at the server with sudo chmod +x /var/logs/auth.log).
    
    3. Use the following command to start the script:
    
          python3.5 authlog_structurizer.py
    
    4 . You can access the new file with the name authanalysed.log. It's your thing what you do with the information provided.
    
