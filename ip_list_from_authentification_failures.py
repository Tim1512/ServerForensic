#!/usr/bin/python

#Use this script to select al IPs inside a file called "raw" and print python list with all IPs. To generate "raw", use the command "sudo grep 'authentication failures' /var/log/auth.log > raw"
try:
    rawfile = open("raw", "r")
    ips = []
    for line in rawfile.readlines():
        add = True
        point = line.find("rhost=")
        point2 = line.find(" user=")
        if point != -1:
            length = len(line)
            newip = line[point+6:point2-1]
            try:
                for ip in ips:
                    if ip == newip:
                        add = False

            except:
                pass
            if add == True:
                ips.append(newip)

        iplist = []
        for ip in ips:
            iplist.append(ip)
    print(iplist)

    rawfile.close()

except FileNotFoundError:
    print("The file 'raw' does not exist. Create it with ''sudo grep 'authentication failures' /var/log/auth.log > raw'' and be sure you are in the same directory")
