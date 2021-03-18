from ipaddress import IPv4Network
import random


def ip_and_mask_random():
    ip = random.randint(0x0b000000, 0xdf000000)
    mask = random.randint(8, 24)
    return ip, mask


class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        IPv4Network.__init__(self, (ip_and_mask_random()), strict=False)

    def is_regular_network(self):
        return self.is_global and not \
            (self.is_multicast or self.is_link_local or
             self.is_loopback or self.is_private or self.is_reserved or self.is_unspecified)


networks = []

while len(networks) < 20:
    random_network = IPv4RandomNetwork()
    if random_network.is_regular_network() and random_network not in networks:
        networks.append(random_network)

for network in sorted(networks):
    print(network)
