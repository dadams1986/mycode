#!/usr/bin/env python3
# intent is to provide troubleshooting commands for cisco IOS dependant on feedback from customer

#define variables

problem = ["interface", "Routing", "Switching", "Device Unreachable"] #problem type

interfacecommands = ["show interface", "show lacp internal", " show interface counters", "show interface statistics"] #interface troubleshooting commands

routingcommands = ["show ip route", "show ip ospf neighbor", "show ip bgp neighbor", "show ip rip" , "show ip pim", "show ip bgp summary", "show log | i bgp/opsf"] #routing troubleshooting commands

switchingcommands = ["show cdp neighbor", "show vtp status", "show vlan"]#switching troubleshooting commands

generaltroubleshootingcommands = ["show log", "show version", "show snmp"] # general troubleshooting
interfacetype = ['copper', 'fiber', 'coaxial', 'wireless']
copperinterface =['gigabit', 'ethernet', 'tengigabit', 'DSL', 'DS3']
fiberinterface = ['giabit', 'ethernet', 'Tengigabit']
coaxialinterface = ['DSL', 'DS3']
wireless = ['2G', '5G']
ethernetinterface = ['eth1/1', 'eth1/2', 'eth1/3', 'eth1/4', 'eth1/5', 'eth1/6'] 
gigabitinterfaces = ['gi1/1', 'gi1/2', 'gi1/3', 'gi1/4', 'gi1/5', 'gi1/6']
tengigabitinterfaces = ['ten1/1', 'ten1/2', 'ten1/3', 'ten1/4', 'ten1/5', 'ten1/6']


#get input

message1 = input("What issue are you having?" + str(problem))

if (message1 == problem[0]):
  print(interfacecommands)
elif (message1 == problem[1]):
  print(routingcommands)
elif (message1 == problem[2]):
  print(switchingcommands)
elif (message1 == problem[3]):
  print("call vendor for onsite support")
else:
  print(generaltroubleshootingcommands)  

message2 = input("What type of Interface are you having issues with?" + str(interfacetype))

if (message2 == interfacetype[0]):
  print(copperinterface)
elif (message2 == interfacetype[1]):
  print(fiberinterface)
elif (message2 == interfacetype[2]):
  print(coaxialinterface)
elif (message2 == interfacetype[3]):
  print(wireless)

message3 = input("please tell me what kind of interface are you looking for?")

if (message3 == "Gigabit"):
 print(gigabitinterfaces)
elif (message3 == "Ethernet"):
  print(ethernetinterface)
elif (message3 == "tengigabit"):
  print(tengigabitinterfaces)


#message = 'The movie is about to begin, we recommend '
#print('What is your connection speed in Mbps?')
#connection = float(input())
#if connection >= 25:
#    message = message + 'setting video to 4k.'
#elif connection >= 5:
#    message = message + 'setting video to 1080p.'
#elif connection >= 2:
#    message = message + 'setting video to 720p.'
#else:
#    message = message + 'finding another access network.'
#print(message)

