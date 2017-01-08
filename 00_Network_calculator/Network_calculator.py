import re

def convert_to_ip(bin_ip):
    bin_ip = '{:0>32}'.format(bin_ip)
    ip = ""
    for i in range(4):
        ip += str(int(bin_ip[:8], 2))
        if i != 3:
            ip += '.'
        bin_ip = bin_ip[8:]
    return ip

print("Please enter the IP address (with dots or other special characters):")
raw_ip = input("> ")
subnet = input("Please enter the subnet prefix: ")

ip = re.split("\D", raw_ip)
try:
    ip = [int(x) for x in ip]
except ValueError:
    print("One of the characters was not a number...")
    exit

int_ip = ""
for section in ip:
    if section > 255:
        print("One of your sections is too long")
        exit
    else:
        int_ip += '{:0>8}'.format(bin(section)[2:])

int_ip = int(int_ip, 2)

subnet = int(''.join(x for x in subnet if x.isdigit()))
subnet = int((subnet * '1') + ((32 - subnet) * '0'), 2)
invert_subnet = int(''.join('1' if x == '0' else '0' for x in bin(subnet)[2:]), 2)

print(20 * "-")
print("IP:")
print(convert_to_ip(bin(int_ip)[2:]))
print()
print("Subnet mask:")
print(convert_to_ip(bin(subnet)[2:]))
print()
print("Network address:")
print(convert_to_ip(bin(int_ip & subnet)[2:]))
print()
print("Broadcast address:")
print(convert_to_ip(bin(int_ip | invert_subnet)[2:]))
print()
print("First host:")
print(convert_to_ip(bin(int_ip & (subnet + 1))[2:]))
print()
print("Last host:")
print(convert_to_ip(bin(int_ip | (invert_subnet - 1))[2:]))
print(20 * "-")
