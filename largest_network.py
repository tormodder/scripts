import ipaddress
import argparse


def largest_network(file):

    addresses = []

    with open(file) as f:
        addresses = f.read().split("\n")

    addresses = list(filter(None, addresses))

    # Remove ipv6 and parse address strings
    for k, v in enumerate(addresses):
        if ":" in v:
            addresses.pop(k)
            continue
        addresses[k] = v.strip()

    networks = [ipaddress.ip_network(ip, strict=False) for ip in addresses]

    largest_network = min(networks, key=lambda net: net.prefixlen)

    print(f"largest network: {largest_network}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find the largest network range from an arbitrary list of ipv6 addresses in CIDR notation")
    parser.add_argument('file', type=str, help='path to the file of ipv6 addresses')
    args = parser.parse_args()
    largest_network(args.file)
