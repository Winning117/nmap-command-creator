
def main():
    ip = input("What IP are you trying to scan? ")
    print()
    print_section("Full TDP Scan: ", "nmap -p- -sV " + str(ip) + " > tdp_full_scan.txt\n")
    print_section("Full UDP Scan: ", "nmap -p- -sU -sV " + str(ip) + " > udp_full_scan.txt\n")
    print_section("OS Scan: ", "nmap -A " + str(ip) + " > os_information.txt\n")
    print_section("Full services information: ", "nmap -sV --version-intensity 5 " + str(ip) + " > full_services.txt\n")


def print_section(header, command):
    BOLD_TEXT = "\033[1m"
    END_BOLD_TEXT = "\033[m"
    print(BOLD_TEXT + header + END_BOLD_TEXT + command)


if __name__ == "__main__":
    main()
