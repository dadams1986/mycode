#!/usr/bin/env pyhton3
my_list = ["192.168.0.5", 5060, "UP"]
print("the first item in the list (IP): " + my_list[0])
print("the second item in the list (port): " + str(my_list[1]) )
print("the last item in the list (state): " + my_list[2])
new_list = [5060, "80", 55, "10.0.0.1", "ssh"]
print("when I " + new_list[4] + " into IP address: " + new_list[3] + " I am unable to ping ports " + str(new_list[0])+" " + new_list[1] +" " + str(new_list[2]))
