import socket
import requests
import whois
import dns.resolver
import nmap

# IP Lookup
def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"IP Address of {domain}: {ip}")
    except socket.gaierror:
        print(f"Unable to get IP for {domain}")

# WHOIS Lookup
def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        print(f"WHOIS info for {domain}:")
        print(w)
    except Exception as e:
        print(f"Error fetching WHOIS data: {e}")

# HTTP Headers
def get_http_headers(domain):
    try:
        response = requests.get(f"http://{domain}")
        print(f"HTTP Headers for {domain}:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
    except requests.RequestException as e:
        print(f"Failed to retrieve HTTP headers: {e}")

# DNS Lookup
def dns_lookup(domain):
    try:
        result = dns.resolver.resolve(domain, 'A')
        print(f"DNS records for {domain}:")
        for ip in result:
            print(ip.to_text())
    except Exception as e:
        print(f"Error in DNS Lookup: {e}")

# Port Scanning using nmap
def scan_ports(domain):
    nm = nmap.PortScanner()
    ip = socket.gethostbyname(domain)
    print(f"Scanning ports for {domain} ({ip}):")
    nm.scan(ip, '1-1024')
    for host in nm.all_hosts():
        print(f"Host: {host}")
        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")
            ports = nm[host][proto].keys()
            for port in ports:
                print(f"Port {port}: {nm[host][proto][port]['state']}")

if __name__ == "__main__":
    domain = input("Enter the domain: ")
    get_ip(domain)
    whois_lookup(domain)
    get_http_headers(domain)
    dns_lookup(domain)
    scan_ports(domain)

    print(f"CODE BY ADIRTTA")
