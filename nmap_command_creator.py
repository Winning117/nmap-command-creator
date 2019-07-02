
def main():
    ip = input("What IP are you trying to scan? ")
    print()
    print("Full TDP Scan: nmap -p- -sV " + str(ip) + " > tdp_full_scan.txt\n")
    print("Full UDP Scan: nmap -p- -sU -sV " + str(ip) + " > udp_full_scan.txt\n")
    print("OS Scan: nmap -A " + str(ip) + " > os_information.txt\n")
    print("Full services information: nmap -sV --version-intensity 5 " + str(ip) + " > full_services.txt\n")


if __name__ == "__main__":
    main()
