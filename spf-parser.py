from sys import stdin
import ipaddress
import json

class Record:
    def __init__(self, record):
        self.chunks = record.replace('" "', "").replace('"', "").split()[5:]
        self.ipv4_vals = []
        self.domain_vals = []
        self.mechanisms = {
            'ip4:': self.parse_ipv4,
            'ptr:': self.parse_ipv4,
            'a:': self.parse_domain,
            'include:': self.parse_domain,
            'mx:': self.parse_domain,
            'exists:': self.parse_domain,
            'redirect=': self.parse_domain,
        }

    def parse_domain(self, chunk):
        self.domain_vals.append(chunk.lower().rstrip("."))

    def parse_ipv4(self, chunk):
        try:
            self.ipv4_vals.append(
                str(ipaddress.IPv4Address(chunk))
                )
        except:
            self.ipv4_vals += list(
                ipaddress.ip_network(chunk).hosts()
            )

    def remove_qualifiers(self, chunk):
        for i in ["+", "-", "~", "?"]:
            if chunk.startswith(i):
                chunk = chunk.lstrip(i)
        return chunk
    
    def make_json(self):
        return json.dumps({
            "ip": self.ipv4_vals,
            "domains": self.domain_vals
        })

    def parse(self):
        for c in self.chunks:
            self.remove_qualifiers(c)
            for m in self.mechanisms.keys():
                if c.startswith(m):
                    c = c.lstrip(m)
                    self.mechanisms[m](c)
        return self.make_json()

if __name__ == "__main__":
    parser = Record(stdin.readline())
    
    print(parser.parse())