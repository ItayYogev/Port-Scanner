#!/usr/bin/env python3

import pyfiglet
import time
import ipaddress
import socket
from datetime import datetime

def print_headers():
    ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
    print(ascii_banner)
    name_banner = pyfiglet.figlet_format("by Itay Yogev", font="mini")
    print(name_banner)
    time.sleep(2)

def validate_ip():
    while True:
        ip_address = input("Enter The IP Address: ")
        try:
            ipaddress.ip_address(ip_address)
            return ip_address
        except ValueError:
            print("\033[1mInvalid IP Address format. Please try again.\033[0m")

def prompt_port_option():
    print("\nChoose Port Option:")
    print("1. Specific Ports")
    print("2. Range")
    print("3. Built-in Wordlist")
    choice = input("\nEnter your choice (1/2/3): ")
    return get_port_list(choice)

def get_port_list(choice):
    try:
        choice = int(choice)
        if choice == 1:
            return get_specific_ports()
        elif choice == 2:
            return get_port_range()
        elif choice == 3:
            return get_builtin_wordlist()
        else:
            raise ValueError
    except ValueError:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return prompt_port_option()

def get_specific_ports():
    port_list = []
    while True:
        port_num = input('Enter The Port Number, type "\033[1mfinish\033[0m" to stop: ')
        if port_num.lower() == "finish":
            if not port_list:
                print("No value, Please enter any ports\n")
            else:
                return port_list
        else:
            try:
                port_num = int(port_num)
                if 1 <= port_num <= 65536:
                    port_list.append(port_num)
                    print(f"Value {port_num} Added: {port_list}\n")
                else:
                    print("Wrong Range. Port numbers should be between 1-65536. Please Try Again")
            except ValueError:
                print("Wrong value. Please enter an integer.\n")

def get_port_range():
    min_value = get_valid_port("Enter the minimum port number: ")
    max_value = get_valid_port("Enter the maximum port number: ")
    return list(range(min_value, max_value + 1))

def get_valid_port(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 65536:
                return value
            else:
                print("Wrong Range. Port numbers should be between 1-65536. Please Try Again")
        except ValueError:
            print("Wrong Values. Please enter numbers only.")

def get_builtin_wordlist():
    return [
        20, 21, 22, 23, 25, 43, 49, 53, 67, 68, 69, 79, 80, 82, 83, 88, 110, 111,
        113, 119, 123, 135, 137, 139, 143, 161, 162, 177, 179, 201, 264, 389, 443,
        444, 445, 464, 497, 500, 513, 512, 514, 515, 520, 554, 546, 547, 587, 593,
        631, 636, 646, 873, 989, 990, 993, 995, 1337, 1194, 1433, 1434, 1701, 1723,
        1725, 1741, 1812, 1813, 1985, 2000, 2002, 2049, 2082, 2083, 2087, 2100, 2145,
        2222, 3128, 3260, 3268, 3269, 3306, 3389, 3478, 3479, 3480, 3481, 3689, 4333,
        4500, 4567, 5000, 5001, 5060, 5432, 5800, 5900, 5985, 6000, 6001, 6514, 6665,
        6666, 6667, 6668, 6669, 6881, 8000, 8008, 8080, 8081, 8089, 8443, 9080, 10000,
        11371
    ]

def print_starting_scan():
    print("\n", "-" * 50)
    print(f"Starting Scanning at: {datetime.now()}")
    print("-" * 50)

def scan_ports(ip_address, port_list):
    print("PORT       SERVICE        DESCRIPTION")
    for port in port_list:
        try:
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.settimeout(0.5)
            connection.connect((ip_address, port))
            service = socket.getservbyport(port)
            banner = connection.recv(1024).decode("utf-8").strip()
            print(f"{port:<12}{service:<16}{banner}")
        except Exception as e:
            pass

def print_scan_complete():
    print("-" * 50)
    print("Scan is complete")
    print("-" * 50)

if __name__ == '__main__':
    print_headers()
    ip_address = validate_ip()
    port_list = prompt_port_option()
    print_starting_scan()
    scan_ports(ip_address, port_list)
    print_scan_complete()
