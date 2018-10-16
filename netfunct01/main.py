#!/usr/bin/env python3

#function to push commands
def commandpush(devicemd): #devicemd==list
  for coffeetime in devicemd.keys():
    print('Handshaking. .. ... connecting with ' + coffeetime)
    #we'll learn to write code that connect to devices here
  for mycmds in devicemd[coffeetime]:
    print('Attempting to send command -->' + mycmds)
    #we'll learn to write code that sends cmds to device here

def devicereboot(devicemd):
  for coffeetime in devicemd:
    print('Connecting to..' + "Rebooting NOW")


###start our script
workdo = {"10.1.0.1":["interface eth1/2", "no shut"], "10.2.0.1":["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} #data that replaces data stored in file
print("Welcome to the network device command pusher")#welcome message

rebootlist = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

##get data set

print("\nData set found\n")

##run
commandpush(workdo)#call function to push commands to devices
devicereboot(rebootlist)
