#Dictionaries


device_dict = {"Device1" : 123,
               "Device2" : 456,
               "Device3" : 789,
               "Device4" : 8910,
               "Yuva": 2.13
               }

#print(device_dict["Yuva"])

#name = input()
#print(device_dict[name])

print("Enter new device:")
new_name = input()
print("Enter new value:")
new_value = int(input())
device_dict[new_name] = new_value

print(device_dict.keys())
print(device_dict.values())

for key, value in device_dict.items():
    print(key, value)